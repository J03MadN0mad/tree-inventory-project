# Data Folder -- What Belongs Here

This folder holds **point-in-time copies** of tree inventory data -- never live,
actively-edited dataset. See `docs/SCHEMA.md`'s Data Governance Rules and
`gis/README.md` for where the live data is stored.

```
data/
  production/  ← raw/sensitive location data -- excluded from git entirely, never committed
  sample/      ← very small test fixtures used to validate scripts/logic
  exports/     ← periodic, timestamped, validated exports (the public-tier datasheet)
```

## `production/`

Raw, unvalidated location data pulled directly from source (e.g., a fresh Arboreal
export before QAQC). Excluded from version control entirely by `.gitignore` -- this folder
should never appear in a commit, by design. If you need to share something from here,
it needs to go through validation first and be inputed into `exports/` instead.

## `sample/`

Small, deliberately minimal files used to test logic before running against production
data -- e.g., a 2-row CSV sample already used to confirm `point_validation_toolkit.py`'s
checks behave correctly (see `PROJECT_STATUS.md`, Current Blockers). Not real tree
records; safe to keep tiny and disposable. Note: singular `sample`, not `samples` -- this
matches the exception already written into `.gitignore` (`!data/sample/*.csv`), so keep
the folder name exact or the CSVs in it will be silently git-ignored.

## `exports/`

Once the inventory has been validated (per the workflow in `protocols/point_validation_SOP.md`) per example,
periodic exports of the real dataset go here -- this is what becomes the "fully public,
extractable" tier described in `PROJECT_STATUS.md`'s Access Tiers section.

**Naming convention:** `tree_inventory_YYYY-MM-DD.csv` (or `.gpkg`), one file per export,
never overwritten -- so the history of exports itself becomes a record of the dataset's
progress over time.

**Important:** anything in this folder is a **snapshot, not a live sync.** If someone asks
"is this current," the answer is always "as of the date in the filename" -- **never assume
it reflects same-day edits happening in ArcGIS Pro.** 

