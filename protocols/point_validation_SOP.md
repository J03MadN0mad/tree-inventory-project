# GPS Accuracy Testing & Point Validation Methodology
**Tree Inventory GIS Project -- Objective 1 & 2 support**

## 1. Purpose

Every point currently in the GIS ends up in one of two states: **classified with a `Status` value already in the schema**, or genuinely unresolvable at a desk and passed to the field-verification queue. This document defines exactly how that classification happens, using the project's own existing `Status` field domain rather than inventing a parallel one, which may lead to problems down the line. 

## 2. Why this matters beyond internal QA

A tree inventory feeding into climate action, canopy analysis, or grant reporting is only as credible as its underlying spatial and attribute accuracy. This validation pass is what makes the dataset defensible when someone asks "how do you know these points are accurate?" -- and it directly produces the "Data Integration & Quality" outcome in the project proposal.

## 3. The `Status` field (already defined in `SCHEMA.md`, not yet populated in the live sheet)

| Value | Meaning | Set by this process when... |
|---|---|---|
| `Existing` | Verified in field, matches ID and tag | Field crew confirms -- not something a desk check can assert |
| `Needs_Verification` | Default for legacy data not yet field-checked | Default state; also assigned when required attributes are missing |
| `Missing_Tag` | Tag missing/damaged/illegible | **Field-confirmed only** -- see Section 6 |
| `New_2025` | Newly added tree | Set at time of new-tree entry, not by this validation pass |
| `Uncertain_Location` | GPS error >3–5 m, unclear placement, or implausible position | Assigned by the checks below |
| `Removed` | Tree no longer present | Field-confirmed only |
| `Duplicate_Candidate` *(recommended addition -- see data dictionary)* | Likely duplicate coordinate record | Assigned by the duplicate check below; never auto-deleted |

## 4. Validation checks, in priority order

Run against the **UTM Zone 11N projected** feature class (not raw WGS 84 lat/long -- see coordinate system note in the data dictionary).

### Check 1 — Geometry validity
Null/empty geometry, or coordinates outside the campus extent. → `Needs_Verification`, note "no geometry captured."

### Check 2 — Duplicate / near-duplicate location
Two or more points within a set tolerance (start at 1 m, revise once GPS Accuracy Testing produces real device-comparison numbers). → `Duplicate_Candidate`, flagged for human review -- never auto-removed, since a true duplicate (same tree logged twice) looks identical at this stage to two legitimately close trees.

### Check 3 — Positional plausibility
Point falls outside the expected campus boundary, or (if building footprint layers are available) inside a building or roadway. → `Uncertain_Location`, note the specific reason.

### Check 4 — Recorded GPS accuracy
Using the schema's own tiering: `GPS_Accuracy_m` ≤3 m passes untouched; 3–5 m → `Uncertain_Location` ("conditional accuracy, recommend recheck"); >5 m → `Uncertain_Location` ("exceeds even the field collection floor, needs remeasurement").

### Check 5 — Required attribute completeness
Missing `Species`, `DBH_in`, or `Condition`. → `Needs_Verification`, note which field is missing.

### Check 6 — Tag_ID blank
This is **not** the same as `Missing_Tag` (see Section 6). A blank `Tag_ID` just gets noted -- it does not change `Status` on its own, since a desk check can't tell "field never checked" apart from "tag confirmed absent."

## 5. Remote verification protocol (Google Earth)

A point flagged `Uncertain_Location` can be resolved without a field visit only if: the tree is visible and identifiable in current imagery, its canopy clearly corresponds to one distinct tree, and there's no ambiguity about which tree the record refers to. If any of those fail, it goes to the field queue instead of being guessed at. Log the imagery date used, in `Notes`, for defensibility.

## 6. What automated desk-based QA cannot determine 

`Missing_Tag` and `Removed` are field-truth states -- they mean a crew physically checked and found a specific condition. A desk-based script has no way to confirm either, so it never sets these values. A blank `Tag_ID` in the data is left as `Needs_Verification` (or whatever it already was) with a note, not silently upgraded to a claim the automation can't back up.

## 7. Weekly workflow

1. Run `scripts/point_validation_toolkit.py` against a **copy** of the UTM 11N feature class first
2. Review summary counts by `Status`
3. Export everything not `Existing`/passing to a working table -- this is both the remote-verification queue and the field re-log punch list
4. Work remote verification first, then hand the remainder to the field crew
5. Track weekly: % of inventory with a `Status` value assigned -- not % `Existing`, since that's a later-summer 2026 target as remeasurement happens

## 8. Standards this approach draws on
See `docs/REFERENCES.md` for full citations and what each source informed.

- **Metadata structure** (positional accuracy, attribute accuracy, lineage/date) mirrors the core building blocks of ISO 19115 / FGDC CSDGM
- **Accuracy reporting** — once GPS Accuracy Testing has real device-comparison numbers, consider stating dataset-wide accuracy in the NSSDA style (accuracy at a stated confidence level) alongside the project's ±2 m target, rather than a bare meters figure
