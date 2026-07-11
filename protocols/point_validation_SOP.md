# GPS Accuracy Testing & Point Validation Methodology
**Tree Inventory GIS Project — Week 1 Priority**
**Objective ties:** GPS Accuracy Testing & Integration · Spatial Accuracy Finalization

## 1. Purpose

Every point currently in the GIS must end this week in one of two states:

1. **Verified** — spatially accurate and defensible, kept as-is, or
2. **Flagged** — labeled with a specific reason and a remediation path (field remeasurement or remote/desktop verification).

No point should remain in an ambiguous or unreviewed state. This methodology defines the checks, thresholds, and status labels used to sort the entire existing inventory, so the dataset going into fall field season is clean and its accuracy is documented rather than assumed.

## 2. Why this matters beyond internal QA

A tree inventory that reports up into a climate action plan, canopy goal, or grant narrative is only as credible as its underlying spatial and attribute accuracy. Structured, well-documented datasets are what let this kind of data actually be used for comparison and reporting across time or across jurisdictions — poorly documented, inconsistent data is a recurring bottleneck in urban forestry and climate reporting more broadly. This validation pass is what makes your dataset defensible when someone asks "how do you know these points are accurate?"

## 3. Status field (add to feature class)

| Field | Type | Purpose |
|---|---|---|
| `Validation_Status` | Text (40) | One of the four statuses below |
| `Validation_Notes` | Text (255) | Which check(s) triggered the flag |
| `Validation_Date` | Date | When the point was last run through this workflow |
| `Remediation_Method` | Text (20) | Field / Remote / N/A — filled in once a flagged point is resolved |

**Status domain:**
- `Verified` — passed all automated checks, retained as-is
- `Needs Remote Verification` — resolvable from Google Earth / aerial imagery without a site visit
- `Needs Field Remeasurement` — cannot be resolved remotely, must be re-logged in situ
- `Flagged for Removal` — duplicate, erroneous, or otherwise not a real, distinct tree record

## 4. Validation checks, in priority order

Run in this order — the first check a point fails determines its status (don't let a later check override an earlier, more serious flag).

### Check 1 — Geometry validity
- Null or empty geometry
- Coordinates at (0,0) or clearly outside your project/service area extent
- **On fail →** `Needs Field Remeasurement` ("No geometry captured")

### Check 2 — Duplicate / near-duplicate location
- Two or more points within a set tolerance of each other (start with **1 meter** — tighten or loosen once your GPS accuracy testing objective gives you a real device error range)
- Distinguish **true duplicates** (same tree logged twice, e.g., by two crew members or a re-log without deleting the original) from **legitimately close trees** (e.g., a planted row) — use judgment on borderline cases rather than auto-deleting
- **On fail →** `Flagged for Removal` ("Duplicate location within X m")

### Check 3 — Positional plausibility
- Point falls outside the expected project/parcel boundary
- (Optional, if you have building footprint / street centerline / hydrology layers) point falls inside a building, in the middle of a street, or in water
- **On fail →** `Needs Remote Verification` ("Falls outside expected area" / "Implausible location")

### Check 4 — Recorded GPS accuracy
- If your collection protocol logs an estimated horizontal error per point, flag anything above your threshold
- Start with a conservative threshold (e.g., **3 m**) and revise once your GPS Accuracy Testing objective produces real numbers for your device(s) — the two objectives should feed each other directly
- **On fail →** `Needs Remote Verification` ("Recorded error exceeds threshold")

### Check 5 — Required attribute completeness
- Minimum viable record, consistent with standard urban forestry inventory practice (i-Tree Eco's own minimum import requirement is just species + DBH): unique Tree ID, Species, DBH
- **On fail →** `Needs Field Remeasurement` ("Missing required attribute")

### Check 6 — Temporal duplicate
- Same Tree ID appears in multiple records with different capture dates (re-logged without archiving the original)
- Keep the most recent, move the older record to an archive table rather than deleting outright (defensibility — you may need to show your edit history later)

## 5. Remote verification protocol (Google Earth)

A flagged point can be resolved remotely — no field visit needed — only if **all** of the following are true:
- The tree is visible and identifiable in current aerial/street-level imagery
- Its canopy position clearly corresponds to a single, distinct tree at that location
- There's no ambiguity about which tree the record refers to (not one of several closely spaced trees)

If any of these fail, downgrade the point to `Needs Field Remeasurement` rather than guessing. Log which imagery date you used in `Validation_Notes` for defensibility.

## 6. Weekly workflow

1. Run the validation script (see `point_validation_toolkit.py`) against a **copy** of your feature class first
2. Review the summary counts by status
3. Export the flagged subset to a working table — this becomes your remote-verification queue and your field re-log punch list
4. Work the remote-verification queue first (fastest wins)
5. Whatever remains becomes the field crew's re-log list going into the Field Data Collection Optimization objective
6. Track weekly: **% of inventory with an assigned Validation_Status** — target 100% by end of this week, not 100% "Verified" (that's a later-summer goal as remeasurement happens)

## 7. Standards this approach draws on

- **Metadata structure** — the check categories above (positional accuracy, attribute accuracy, lineage/date) mirror the core building blocks of the ISO 19115 / FGDC CSDGM geospatial metadata standards, which is worth knowing since your GIS Protocol Standardization objective will need to produce metadata records eventually anyway
- **Minimum attribute floor** — species + DBH as the non-negotiable minimum record mirrors i-Tree Eco's own inventory import requirements, a widely used urban forestry standard
- **Positional accuracy reporting** — once your GPS Accuracy Testing objective produces real error figures, consider reporting them in the National Standard for Spatial Data Accuracy (NSSDA) style (accuracy at a stated confidence level, e.g., 95%) rather than a bare "meters" number — it's the more defensible convention for describing dataset-wide accuracy
