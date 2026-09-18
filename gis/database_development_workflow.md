# Master GIS Database Development Workflow

**Campus Tree Inventory Project**

## Overview

This document describes the project's field data processing as the raw data becomes part of the authoritative GIS dataset -- from the moment it leaves a data source (a legacy spreadsheet, an Arboreal export, a handheld GPS unit) to the moment it is merged into the live feature class (GIS data table). It's the operational counterpart to `docs/SCHEMA.md`: the schema that defines *what* a valid record looks like field-by-field; this `Master GIS Database Development Workflow` document defines *how* a raw, messy batch of new data actually gets turned into desired GIS ready data.

> **A note on scope, so this doesn't drift out of sync with the schema:** `docs/SCHEMA.md` is the single authoritative source for field data collection definitions, the `Status` domain, spatial accuracy tiers, coordinate system standards, and data governance rules. This document *does not redefine any of those -- it references them.* 
    Note to Internal Team:
    That's a deliberate choice, not an oversight: this project already went through one painful reconciliation of three documents project origin ero documents (see `docs/data-dictionary.md`), and the whole point of that exercise was to stop letting new reference material duplicate values that could drift, causing us lots of headaches... Where this document needs one of those values, it links to `SCHEMA.md` rather than restating it.

## Core Principle

**The GIS feature class is the authoritative dataset. Spreadsheets (CSV/Excel) are staging environments only.**

This is worth stating plainly because it's easy to accidentally forget this in practice -- especially when Excel is where most of the actual cleaning work happens, which can make it *feel* like the source of truth. Excel is *where raw, messy data gets prepared to become trustworthy; the feature class in ArcGIS Pro is where it actually becomes trustworthy.* Edits to *tree locations, attributes, or status happen in the GIS environment.* A CSV is a snapshot passing through, never a place to edit geometry directly -- see `SCHEMA.md`'s Data Governance Rules for the formal version of this rule.

---

<details>
<summary><strong>1. Data Sources</strong></summary>

The dataset is assembled from several sources that don't share a common origin or format (2022, 2025, 2026, and so forth) which is exactly why the staging and reconciliation steps below exist -- none of these can be trusted to already agree with each other or with the live schema:

- **Legacy dataset (2022 inventory)** -- the original baseline this whole project is modernizing. Oldest and least standardized source; expect the most schema drift here.
- **December 2025 collection dataset** -- first in-situ community data collection day referenced in `docs/data-dictionary.md`'s note on when `SCHEMA.md` was created.
- **April 2026 field collection dataset** -- second in-situ collection day, same note.
- **Arboreal exports (CSV)** -- the ongoing, primary collection method described in `protocols/field_data_collection_protocol.md`. This is the main pipeline going forward.
- **GPS data (mobile / external units)** — smartphone GNSS and, since the Garmin GPSMAP 65s was added to the toolkit, handheld unit readings. See `protocols/gps_best_practices_cheat_sheet.md` Section 6, and `SCHEMA.md`'s `Collection_Method` field, for how the two device types are distinguished once data reaches the schema.

</details>

<details>
<summary><strong>2. Data Staging Workflow</strong></summary>

**Step 1 — Import into Excel structure**

Every incoming batch, regardless of source, passes through three tiers before it's eligible for GIS integration:

| Tier | Purpose |
|---|---|
| **Historical** | Raw archive -- unaltered, exactly as received. This is the "what did we actually get" record, kept even after cleaning happens downstream, so a cleaning mistake is always recoverable. |
| **Working** | Active cleaning and comparison against the existing Master dataset. Nothing here is trusted yet. |
| **Master** | GIS-ready. Only data that's passed cleaning *and* reconciliation (Section 3) reaches this tier. |

**Where this fits relative to the repo's `data/` folder:** this three-tier staging happens *before* anything reaches the GIS or this repository -- it's a pre-processing stage, typically in Excel, on whatever machine or shared drive the cleaning work happens on. None of these three tiers correspond to `data/production/`, `data/sample/`, or `data/exports/` (see `data/README.md`); those folders describe a *later* stage, after data has already been through this Excel staging **and** validated against the schema. Put another way: raw data → (this section's Historical/Working/Master staging, outside git) → GIS feature class → validated export → `data/exports/` (inside git, public-tier). This section is entirely upstream of the repo's own data folder.

**Step 2 — Schema standardization**

Before anything moves from Working to Master, incoming data must be aligned to `docs/SCHEMA.md` -- not to whatever format the source (*remember, source equals raw data coming straight from the in field data collection*) shappened to use:

- Field names must match `SCHEMA.md` exactly (not "close enough" -- a renamed column is exactly how the original three-way schema drift this project already cleaned up once got started, again.. a major headache to resolve..)
- Units must be consistent: `DBH_in` in inches, height fields in meters -- see `SCHEMA.md`'s Resolved Conflict on DBH units in `data-dictionary.md` for why this specific field is worth double-checking on every import
- No mixed formats within a field (a `DBH_in` column with `"12 cm"` next to `"45.5 in"` is a failure state, not just messy data -- it needs correcting before Working → Master, not silently averaged or guessed; data consistency and integrity is key here)

**Step 3 — Data cleaning**

- Remove duplicates *within the incoming batch itself* (this is separate from Section 3's reconciliation against the *existing* Master dataset -- a batch can have internal duplicates even before it's compared to anything already on file)
- Standardize `Tree_ID` format (see `SCHEMA.md`: permanent, unique, never reassigned -- get this right before Master, since fixing it after integration means changing a key that downstream records may already reference)
- Extract structured values out of free-text notes/comments where needed (e.g., a surveyor name embedded in a comment string, per the format `field_data_collection_protocol.md` specifies)
- Resolve text-vs-numeric formatting issues (a DBH_in value stored as text instead of a number will silently fail numeric comparisons downstream, including in point_validation_toolkit.py's attribute-completeness check)

</details>

<details>
<summary><strong>3. Data Reconciliation (Critical)</strong></summary>

All new data must be compared against the existing Master dataset before it's merged in -- this is what prevents the same tree from quietly existing twice, or an update silently overwriting the wrong record.

**Decision logic (Tree_ID as primary key):**

| Scenario | Action |
|---|---|
| Same `Tree_ID`, same tree | Update attributes if needed |
| Same `Tree_ID`, different species recorded | Flag as `Needs_Verification` |
| Same `Tree_ID`, different location recorded | Flag as `Uncertain_Location` |
| New `Tree_ID`, no match found | Add as `New_2025` |
| Tree expected but not found in field | Mark as `Removed` -- **field-confirmed only**, per `SCHEMA.md` and `point_validation_SOP.md` Section 6; a desk-based reconciliation pass cannot assign this on its own |
| Same coordinates and/or same `Tag_ID` as another existing record | Flag as `Duplicate_Candidate` -- automated, never auto-deleted, requires human review (see `SCHEMA.md`) |
**Note to Internal Team**
*That last row is new relative to the original draft -- Duplicate_Candidate didn't exist as a Status value when this document was first written, but it's now a formally adopted part of the schema, and duplicate detection is already core to point_validation_toolkit.py's logic and our general data collection protocol. That said -- per PROJECT_STATUS.md, the script has only been tested against a small sample outside ArcGIS Pro so far; its first full run against live production data hasn't happened yet. Leaving Duplicate_Candidate out here would still describe an outdated version of the reconciliation process -- but don't read this row as confirmation that the script has actually been run against real inventory data yet. That is still pending.*

</details>

<details>
<summary><strong>4. Status Assignment During Reconciliation</strong></summary>

This step assigns or updates the `Status` field as part of reconciliation. The full domain of valid `Status` values -- what each one means, and who's allowed to set it (desk-based QA vs. field-confirmed only) -- is defined authoritatively in `docs/SCHEMA.md`'s **Condition & Status** section.

What *is* specific to this stage: reconciliation (Section 3 above) is one of the two places `Status` actually gets set -- the other being the automated desk-based checks in `point_validation_toolkit.py` (see `protocols/point_validation_SOP.md`). Reconciliation handles the "is this a new tree, an update, or a possible duplicate" question; the validation toolkit handles "does this record's data quality hold up" independent of whether it's new or existing.

</details>

<details>
<summary><strong>5. Integration into GIS</strong></summary>

Once a batch has cleared staging (Section 2) and reconciliation (Section 3), it's ready to move from the Master Excel tier into the actual GIS environment:

1. Import the cleaned Master table into ArcGIS Pro
2. Convert to a point feature class if it isn't one already (see `gis/arcgis_pro_workflow.md` Section 1 for the CSV → XY point procedure)
3. Append to, or update, the existing authoritative feature class -- never create a second parallel feature class, even temporarily; that's how a fourth conflicting source of truth would start (save yourself from massive headaches by avoiding this)
4. Confirm after the merge that `Tree_ID` integrity held (no duplicated or dropped IDs) and that every incoming record has a `Status` value assigned, not left blank

*This step is where "the feature class is authoritative" (Core Principle, above) actually takes effect — before this point, everything is still staging.*

</details>

<details>
<summary><strong>6. Spatial Accuracy Standards</strong></summary>

Accuracy tiers (≤3m / 3–5m / >5m) are defined in `SCHEMA.md`, with the full reasoning behind them in `data-dictionary.md`'s "Resolved conflict #2." This workflow uses those same tiers -- the ones point_validation_toolkit.py enforces automatically -- so manual reconciliation and automated validation hold every point to the same standard.

</details>

<details>
<summary><strong>7. Troubleshooting Log</strong></summary>

Practical issues encountered doing this work, and what's fixed each one so far. This section is meant to grow -- add to it as new issues come up, rather than re-solving the same problem twice a season apart to save time, and headache.

**Duplicate records**
- *Cause:* Overlapping entries between legacy data and newly collected data (most common when the same tree was captured in both the 2022 baseline and a later collection day without anyone realizing it already existed).
- *Solution:* Compare by `Tree_ID` (see the flagged matching-key note in Section 3) and remove duplicates at the Working tier, before they ever reach Master.

**Mixed DBH units**
- *Cause:* Source data mixing centimeters, inches, and occasionally circumference measurements buried in free-text notes.
- *Solution:* Standardize everything to inches, numeric only -- this is the same units resolution `data-dictionary.md` already settled for the schema itself; this is just where it gets enforced during import rather than assumed.

**#VALUE! errors in Excel**
- *Cause:* Empty cells or stray text landing in a numeric field (a common side effect of copy-pasting from Arboreal's export format).
- *Solution:* Use conditional formulas that explicitly handle blanks rather than letting a formula fail silently across an entire column.

**GPS inaccuracy (10m+)**
- *Cause:* Mobile device limitations -- the exact scenario the Garmin GPSMAP 65s was added to the toolkit to address (see `gps_best_practices_cheat_sheet.md` Section 6).
- *Solution:* Flag as `Uncertain_Location`; re-capture using the improved GPS workflow (Garmin fallback if it's a repeat retake); adjust using high-resolution imagery only if the remote-verification conditions in `point_validation_SOP.md` Section 5 are actually met -- otherwise it goes to the field queue.

**Tag conflicts**
- *Cause:* The same `Tag_ID` physically assigned to two different trees (a field-crew error, not a data-entry one).
- *Solution:* Requires field verification -- this can't be resolved at a desk, since it's a physical-world discrepancy, not a data one.
*A great way to prevent this is have only 1 physical tag coresponding to one number; no number repeats*

</details>

<details>
<summary><strong>8. Data Governance Rules</strong></summary>

`SCHEMA.md`'s own "Data Governance Rules" section is the authoritative version of this -- `Tree_ID` as the authoritative key, CSVs as read-only for geometry, edits happening in the GIS environment rather than raw files. This document doesn't restate that list a second time for the same reason Section 4 (Status) and Section 6 (accuracy tiers) don't: one authoritative copy, everything else points to it.

**Closing the loop** -- how a GIS edit reaches the mastersheet: 
Say a vector point for one of our trees gets nudged in ArcGIS Pro to more accurately reflect the tree's real-world location, checked against imagery. That new Latitude/Longitude is in the feature class's attribute table the moment the edit is made. The mastersheet does not get manually re-edited to match it. Instead, per `data/README.md`'s exports/ convention, a periodic validated export gets generated from the feature class and becomes the current mastersheet snapshot (tree_inventory_YYYY-MM-DD.csv). Within the GIS (ArcPro for our project), edits only ever flow one direction -- feature class → exported mastersheet, never the reverse -- so there's never a scenario where two people are independently editing the same tree's coordinates in two different places at once. The tradeoff, already spelled out in data/README.md, is that the mastersheet is only ever accurate "as of" its export date -- never assume it reflects same-day edits still sitting in ArcGIS Pro. In other words, it would be good practice to ensure replace the mastersheet as soon as you finish edits and log the changes you've made.

</details>

<details>
<summary><strong>9. Version Control</strong></summary>

Covered by `SCHEMA.md`'s "Versioning & Updates" section -- preserving previous records each update cycle, logging `Status` changes, and (per `SCHEMA.md`'s forward-looking note) a possible future verification-date field. Same reasoning as Section 8: not duplicated here.

</details>

<details>
<summary><strong>10. References &amp; Best Practices</strong></summary>

This document originally ended with its own standalone reference list (ESRI Urban Forestry Data Models, i-Tree Eco Methodology, OpenTreeMap Data Structure, campus GIS inventory standards). This repo already has a dedicated home for exactly that: `docs/REFERENCES.md`, which requires every entry to state what it is and which specific decision in the repo it informed -- a stricter and more useful standard than a bare list. **Recommendation:** fold these four into `docs/REFERENCES.md` rather than duplicating a reference list here; I can draft the entries in that file's format if you want. This document links out to `docs/REFERENCES.md` instead of maintaining a second list that can drift out of sync with the first.

</details>

---

## Summary

`SCHEMA.md` already states what this workflow is ultimately in service of -- data consistency, defensible spatial accuracy, scalable field workflows, long-term usability. This document is the operational path from raw, disagreeing data sources to a dataset ready to be used by the team and public: stage it, standardize it against the schema, reconcile it against what's already on file, validate it, and only then let it become part of the authoritative feature class.