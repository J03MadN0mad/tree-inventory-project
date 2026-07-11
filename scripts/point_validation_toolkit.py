"""
Tree Inventory Point Validation Toolkit
=========================================
Run this inside ArcGIS Pro's Python window, or as a standalone script tool,
against your existing tree inventory point feature class.

WHAT IT DOES
------------
Classifies every point into one of four statuses so that, by the end of
this week, nothing in the inventory is unreviewed:
    - Verified                    (passed all checks, keep as-is)
    - Needs Remote Verification   (resolvable from Google Earth / imagery)
    - Needs Field Remeasurement   (must be re-logged in situ)
    - Flagged for Removal         (duplicate / erroneous record)

BEFORE YOU RUN THIS
--------------------
1. TEST ON A COPY of your feature class first, not your production data.
2. Edit the CONFIG block below so the field names match your schema.
3. If you don't log a GPS accuracy/error field per point, set
   FIELD_GPS_ACC = None and that check will be skipped.
4. If you have a project or service-area boundary polygon, point
   BOUNDARY_FC at it. If not, leave it as None and that check is skipped.

NATIVE ARCGIS PRO ALTERNATIVE
------------------------------
Everything here can also be done with built-in geoprocessing tools if you'd
rather not run custom code:
    - "Check Geometry" / "Repair Geometry"  -> null/invalid geometry
    - "Find Identical"                       -> exact or near-duplicate points
    - "Select Layer By Location" (boundary)  -> positional plausibility
This script just chains the equivalent logic together with status labels
in one pass, plus the attribute-completeness and accuracy-threshold checks,
which don't have single built-in tools.
"""

import arcpy
import datetime
import collections

# ----------------------------------------------------------------------
# CONFIG — edit these to match your data before running
# ----------------------------------------------------------------------
FC_PATH = r"C:\path\to\your\TreeInventory.gdb\TreePoints"   # your point feature class
BOUNDARY_FC = None   # optional polygon fc (project/parcel boundary), or None

FIELD_TREE_ID = "TreeID"          # unique tree identifier field
FIELD_SPECIES = "Species"         # species field
FIELD_DBH = "DBH"                 # diameter at breast height field
FIELD_GPS_ACC = "GPS_Accuracy"    # recorded horizontal error field, or None if not present
GPS_ACC_THRESHOLD_M = 3.0         # flag points with recorded error above this
                                   # (revise once GPS Accuracy Testing objective has real numbers)

DUPLICATE_TOLERANCE_M = 1.0       # points within this distance of each other = duplicates

FIELD_STATUS = "Validation_Status"
FIELD_NOTES = "Validation_Notes"
FIELD_DATE = "Validation_Date"

STATUS_VERIFIED = "Verified"
STATUS_REMOTE_VERIFY = "Needs Remote Verification"
STATUS_FIELD_REMEASURE = "Needs Field Remeasurement"
STATUS_REMOVE = "Flagged for Removal"

# ----------------------------------------------------------------------


def ensure_fields(fc):
    """Add the validation fields if they don't already exist."""
    existing = [f.name for f in arcpy.ListFields(fc)]
    if FIELD_STATUS not in existing:
        arcpy.management.AddField(fc, FIELD_STATUS, "TEXT", field_length=40)
    if FIELD_NOTES not in existing:
        arcpy.management.AddField(fc, FIELD_NOTES, "TEXT", field_length=255)
    if FIELD_DATE not in existing:
        arcpy.management.AddField(fc, FIELD_DATE, "DATE")


def find_duplicate_oids(fc):
    """Return the set of OIDs that share a near-identical location with another point."""
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
    polys = []
    with arcpy.da.SearchCursor(boundary_fc, ["SHAPE@"]) as cursor:
        for (poly,) in cursor:
            polys.append(poly)
    return polys


def point_in_boundary(x, y, sr, boundary_polys):
    """True if no boundary was supplied (check skipped) or the point falls inside one."""
    if boundary_polys is None:
        return True
    pt = arcpy.PointGeometry(arcpy.Point(x, y), sr)
    return any(poly.contains(pt) for poly in boundary_polys)


def run_validation():
    ensure_fields(FC_PATH)
    dup_oids = find_duplicate_oids(FC_PATH)
    sr = arcpy.Describe(FC_PATH).spatialReference
    boundary_polys = load_boundary_polygons(BOUNDARY_FC)

    fields = ["OID@", "SHAPE@XY", FIELD_TREE_ID, FIELD_SPECIES, FIELD_DBH]
    gps_acc_index = None
    if FIELD_GPS_ACC:
        gps_acc_index = len(fields)
        fields.append(FIELD_GPS_ACC)
    fields += [FIELD_STATUS, FIELD_NOTES, FIELD_DATE]

    counts = collections.Counter()

    with arcpy.da.UpdateCursor(FC_PATH, fields) as cursor:
        for row in cursor:
            oid = row[0]
            x, y = row[1]
            tree_id, species, dbh = row[2], row[3], row[4]
            notes = []
            status = STATUS_VERIFIED

            if x is None or y is None:
                status = STATUS_FIELD_REMEASURE
                notes.append("No geometry captured")
            else:
                if oid in dup_oids:
                    status = STATUS_REMOVE
                    notes.append(f"Duplicate location within {DUPLICATE_TOLERANCE_M} m of another point")
                elif not point_in_boundary(x, y, sr, boundary_polys):
                    status = STATUS_REMOTE_VERIFY
                    notes.append("Falls outside expected project boundary")

                if gps_acc_index is not None and status == STATUS_VERIFIED:
                    acc_val = row[gps_acc_index]
                    if acc_val is not None and acc_val > GPS_ACC_THRESHOLD_M:
                        status = STATUS_REMOTE_VERIFY
                        notes.append(f"Recorded GPS error {acc_val} m exceeds {GPS_ACC_THRESHOLD_M} m threshold")

                if not tree_id:
                    status = STATUS_FIELD_REMEASURE
                    notes.append("Missing Tree ID")
                if not species:
                    if status == STATUS_VERIFIED:
                        status = STATUS_FIELD_REMEASURE
                    notes.append("Missing species")
                if dbh is None:
                    if status == STATUS_VERIFIED:
                        status = STATUS_FIELD_REMEASURE
                    notes.append("Missing DBH")

            row[-3] = status
            row[-2] = "; ".join(notes) if notes else "Passed all automated checks"
            row[-1] = datetime.datetime.now()
            cursor.updateRow(row)
            counts[status] += 1

    print("Validation complete. Status breakdown:")
    total = sum(counts.values())
    for status in (STATUS_VERIFIED, STATUS_REMOTE_VERIFY, STATUS_FIELD_REMEASURE, STATUS_REMOVE):
        n = counts.get(status, 0)
        pct = (n / total * 100) if total else 0
        print(f"  {status:32s} {n:6d}  ({pct:.1f}%)")


def export_flagged(fc, out_gdb, out_name="Points_NeedsReview"):
    """Export everything that isn't Verified into a separate working table/fc."""
    out_fc = f"{out_gdb}\\{out_name}"
    where = f"{FIELD_STATUS} <> '{STATUS_VERIFIED}'"
    arcpy.analysis.Select(fc, out_fc, where)
    print(f"Exported flagged points to {out_fc}")


if __name__ == "__main__":
    run_validation()
    # Uncomment once you're ready to produce the field/remote working list:
    # export_flagged(FC_PATH, r"C:\path\to\your\Working.gdb")
