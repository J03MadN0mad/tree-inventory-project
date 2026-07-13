"""
Tree Inventory Point Validation Toolkit
=========================================
Run inside ArcGIS Pro's Python window, or as a standalone script tool,
against the tree inventory point feature class — projected to
UTM Zone 11N (WGS 84), per the project's coordinate system standard.
Distance-based checks below assume projected meters; running this
against the raw WGS 84 lat/long storage layer will silently misbehave.

WHAT IT DOES
------------
Populates the existing `Status` field (already defined in SCHEMA.txt,
not yet populated in the live sheet) rather than inventing a parallel
status field. Values used:
    - Needs_Verification    (default / legacy / missing attributes)
    - Uncertain_Location    (poor GPS accuracy / implausible position)
    - Duplicate_Candidate   (recommended new value — see data dictionary;
                             flagged for human review, never auto-deleted)
Left untouched (field-truth states this script cannot determine):
    - Existing, Missing_Tag, Removed, New_2025

BEFORE YOU RUN THIS
--------------------
1. TEST ON A COPY of the feature class first, not production data.
2. Confirm the feature class is the UTM 11N projected version.
3. Field names below already match the live MASTERDATASHEET schema —
   only change CONFIG if your actual feature class differs from it.
4. If `Status` doesn't yet exist as a field, this script adds it and
   is your first real population of it.

NATIVE ARCGIS PRO ALTERNATIVE
------------------------------
"Check Geometry"/"Repair Geometry" (invalid geometry), "Find Identical"
(duplicates), and "Select Layer By Location" (boundary checks) can do
pieces of this natively if you'd rather not run custom code. This
script chains the equivalent logic together with the schema's own
Status values, plus the attribute-completeness and accuracy-tier
checks, which don't have single built-in tools.
"""

import arcpy
import datetime
import collections

# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------
FC_PATH = r"C:\path\to\your\TreeInventory.gdb\TreePoints_UTM11N"  # UTM 11N projected fc
BOUNDARY_FC = None   # optional campus boundary polygon fc, or None

FIELD_TREE_ID = "Tree_ID"
FIELD_TAG_ID = "Tag_ID"
FIELD_SPECIES = "Species"
FIELD_DBH = "DBH_in"
FIELD_CONDITION = "Condition"
FIELD_GPS_ACC = "GPS_Accuracy_m"

# Schema's own accuracy tiers (see data-dictionary.md) — not arbitrary
GPS_ACC_CONDITIONAL_M = 3.0   # >3m and <=5m -> conditional
GPS_ACC_FAIL_M = 5.0          # >5m -> needs correction

DUPLICATE_TOLERANCE_M = 1.0   # points within this distance = duplicate candidates

FIELD_STATUS = "Status"
FIELD_NOTES = "Notes"          # existing free-text field; validation notes are appended

STATUS_NEEDS_VERIFICATION = "Needs_Verification"
STATUS_UNCERTAIN_LOCATION = "Uncertain_Location"
STATUS_DUPLICATE_CANDIDATE = "Duplicate_Candidate"   # recommended new domain value

# Field-truth states this script NEVER sets (see SOP Section 6):
# Existing, Missing_Tag, Removed, New_2025

# ----------------------------------------------------------------------


def ensure_fields(fc):
    existing = [f.name for f in arcpy.ListFields(fc)]
    if FIELD_STATUS not in existing:
        arcpy.management.AddField(fc, FIELD_STATUS, "TEXT", field_length=40)


def find_duplicate_oids(fc):
    """Return OIDs that share a near-identical projected location with another point."""
    buckets = {}
    dup_oids = set()
    with arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@XY"]) as cursor:
        for oid, (x, y) in cursor:
            if x is None or y is None:
                continue
            key = (round(x / DUPLICATE_TOLERANCE_M), round(y / DUPLICATE_TOLERANCE_M))
            buckets.setdefault(key, []).append(oid)
    for oid_list in buckets.values():
        if len(oid_list) > 1:
            dup_oids.update(oid_list)
    return dup_oids


def load_boundary_polygons(boundary_fc):
    if not boundary_fc:
        return None
    with arcpy.da.SearchCursor(boundary_fc, ["SHAPE@"]) as cursor:
        return [poly for (poly,) in cursor]


def point_in_boundary(x, y, sr, boundary_polys):
    if boundary_polys is None:
        return True  # check skipped if no boundary supplied
    pt = arcpy.PointGeometry(arcpy.Point(x, y), sr)
    return any(poly.contains(pt) for poly in boundary_polys)


def run_validation():
    ensure_fields(FC_PATH)
    dup_oids = find_duplicate_oids(FC_PATH)
    sr = arcpy.Describe(FC_PATH).spatialReference
    boundary_polys = load_boundary_polygons(BOUNDARY_FC)

    fields = ["OID@", "SHAPE@XY", FIELD_TREE_ID, FIELD_TAG_ID, FIELD_SPECIES,
              FIELD_DBH, FIELD_CONDITION, FIELD_GPS_ACC, FIELD_STATUS, FIELD_NOTES]

    counts = collections.Counter()
    tag_blank_count = 0

    with arcpy.da.UpdateCursor(FC_PATH, fields) as cursor:
        for row in cursor:
            (oid, (x, y), tree_id, tag_id, species, dbh, condition,
             gps_acc, current_status, notes) = row

            new_status = None   # None = leave existing Status untouched
            new_notes = []

            if x is None or y is None:
                new_status = STATUS_NEEDS_VERIFICATION
                new_notes.append("Automated QA: no geometry captured")
            elif oid in dup_oids:
                new_status = STATUS_DUPLICATE_CANDIDATE
                new_notes.append(f"Automated QA: duplicate location within {DUPLICATE_TOLERANCE_M} m — human review required before removal")
            elif not point_in_boundary(x, y, sr, boundary_polys):
                new_status = STATUS_UNCERTAIN_LOCATION
                new_notes.append("Automated QA: falls outside expected campus boundary")
            else:
                if gps_acc is not None:
                    if gps_acc > GPS_ACC_FAIL_M:
                        new_status = STATUS_UNCERTAIN_LOCATION
                        new_notes.append(f"Automated QA: GPS accuracy {gps_acc} m exceeds field collection floor of {GPS_ACC_FAIL_M} m")
                    elif gps_acc > GPS_ACC_CONDITIONAL_M:
                        new_status = STATUS_UNCERTAIN_LOCATION
                        new_notes.append(f"Automated QA: GPS accuracy {gps_acc} m in conditional range ({GPS_ACC_CONDITIONAL_M}-{GPS_ACC_FAIL_M} m), recommend recheck")

                missing = []
                if not species:
                    missing.append("Species")
                if dbh is None:
                    missing.append("DBH_in")
                if not condition:
                    missing.append("Condition")
                if missing and new_status is None:
                    new_status = STATUS_NEEDS_VERIFICATION
                    new_notes.append(f"Automated QA: missing required attribute(s): {', '.join(missing)}")

            # Tag_ID blank is noted, never used to assert Missing_Tag (field-truth only)
            if not tag_id:
                tag_blank_count += 1
                new_notes.append("Automated QA: Tag_ID blank in dataset (not asserting Missing_Tag — field confirmation required)")

            if new_status is not None:
                row[8] = new_status
                counts[new_status] += 1
            else:
                counts[current_status or "(unchanged)"] += 1

            if new_notes:
                combined = (notes + " | " if notes else "") + "; ".join(new_notes)
                row[9] = combined[:255]  # respect Notes field length if constrained

            cursor.updateRow(row)

    print("Validation complete. Status assignments made this run:")
    for status, n in counts.items():
        print(f"  {status:28s} {n:6d}")
    print(f"\nRecords with blank Tag_ID (noted, not auto-classified): {tag_blank_count}")


def export_flagged(fc, out_gdb, out_name="Points_NeedsReview"):
    """Export everything with a Status other than Existing to a working table."""
    out_fc = f"{out_gdb}\\{out_name}"
    where = f"{FIELD_STATUS} IS NOT NULL AND {FIELD_STATUS} <> 'Existing'"
    arcpy.analysis.Select(fc, out_fc, where)
    print(f"Exported flagged points to {out_fc}")


if __name__ == "__main__":
    run_validation()
    # Uncomment once ready to produce the field/remote working list:
    # export_flagged(FC_PATH, r"C:\path\to\your\Working.gdb")
