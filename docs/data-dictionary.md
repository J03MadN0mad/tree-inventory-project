# Data Dictionary — Reconciled Schema

**Status:** Living document. This reconciles three internal sources that currently disagree with each other in places: `SCHEMA.txt` (the designated authoritative schema), `Field_Guide_Reference.txt` (an older field reference), and the actual live MASTERDATASHEET column headers currently in use. This document states which one takes authority; the GIS Protocol Standardization deliverable.

## Fields currently active in the live dataset

| Field | Type / Units | In `SCHEMA.txt`? | In `Field_Guide_Reference.txt`? | Notes |
|---|---|---|---|---|
| `Tree_ID` | Text, unique, permanent | ✅ | ✅ | Primary key. Never reassigned. |
| `Tag_ID` | Text | ✅ | ✅ | Physical tag number. `"None"` if missing. |
| `Species` | Text, scientific name | ✅ | ✅ | e.g. *Acer saccharum* |
| `Common_Name` | Text | ✅ | ✅ | Optional, public-facing |
| `DBH_in` | Float | ✅ | ⚠️ conflict | **See "Resolved conflict #1" below** |
| `Condition` | Text, domain-controlled | ✅ (as `Condition`) | ⚠️ named `Health` | Good / Fair / Poor / Dead / Remove |
| `Latitude` / `Longitude` | Float, decimal degrees, WGS 84 | ✅ | ✅ | |
| `Altitude_m` | Float, meters | ✅ | — | |
| `GPS_Accuracy_m` | Float, meters | ✅ | — | **See "Resolved conflict #2" below** |
| `Perpendicular_Height_m`, `Inclination_deg`, `Inclined_Height_m` | Float | ✅ | ⚠️ Field_Guide only has flat `Height_m` | SCHEMA.txt's lean-adjusted model is more precise and is what's actually live — treat `Field_Guide_Reference.txt`'s simpler version as outdated |
### NOTE
SCHEMA was created after the first 1/2 in-situ community data collection days (Dec. 2025 & April 2026)
| `Crown_Width_m`, `Crown_Base_Height_m` | Float, meters | ✅ | — | |
| `Date`, `Time` | Date / Text | ✅ | — | |
| `Notes` | Text | ✅ | — | Currently also carries surveyor name and structured comments as free text. This field may be removed from public facing datasets for the interrest of privacy. See "Worth doing later" |
| `Photo` | Text (path/URL) | ✅ (as `Photo`) | ⚠️ named `Photo_URL` | Live sheet uses `Photo` |

## Fields defined in the schema but NOT yet present in the live dataset

| Field | Defined in | Status |
|---|---|---|
| `Status` | `SCHEMA.txt` (marked **Required**) | **Not yet implemented in the live sheet.** This is the single biggest gap between the schema-as-written and the schema-as-lived. The validation script in `scripts/point_validation_toolkit.py` is written to populate this field for the first time, not to compete with an existing one. |
| `Surveyor_Name` | `SCHEMA.txt` | Not a separate column yet — currently embedded as the first line of the free-text `Notes`/comment field per the in-field collection protocol (e.g., "Team A, LEAD"). Worth eventually splitting into its own field, but that's a later cleanup, not urgent. This field may be removed from public facing datasets for the interrest of privacy. |

## Fields in `Field_Guide_Reference.txt` that don't appear live or in `SCHEMA.txt`

`Genus`, `Condition_Notes`, `Xcoord`/`Ycoord`, `Last_Verified` exist only in the older reference doc. TASK PRIOR TO FALL: retire or update `Field_Guide_Reference.txt` to match `SCHEMA.txt`, since the live data already tracks `SCHEMA.txt` almost exactly.

## Resolved conflict #1 — DBH units

`Field_Guide_Reference.txt` says `DBH_in` is measured in **centimeters**, contradicting its own field name (`_in` = inches) and contradicts `SCHEMA.txt`. The field data collection protocol settles it directly: volunteers are instructed to measure trunk diameter and enter it in **inches**. **`SCHEMA.txt` is correct. `Field_Guide_Reference.txt` has a units error and should be corrected or retired.**

## Resolved conflict #2 — GPS accuracy has three different numbers, and that's actually fine

Across the documents, "accuracy" appears as ±2 m (project proposal's overall target), ±1–3 m (equipment description), a ≤3 m / 3–5 m / >5 m tier (`SCHEMA.txt`), and ≤5 m preferred / retake above 10 m (field collection cheat sheet). Separate what each one is measuring to avoid contradictions:

| Tier | Value | Purpose |
|---|---|---|
| **Collection-time floor** | Retake if reading is worse than ~5 m (10 m hard-stop) | What a volunteer accepts *in the moment*, per the GPS Best Practices Cheat Sheet 
### NOTE:
Ensure protocol is set and followed regarding ensuring hard-stop is strictly followed in-situ.
 |
| **Dataset classification** | ≤3 m Verified · 3–5 m Conditional · >5 m Needs correction | How `GPS_Accuracy_m` is interpreted *after* collection, per `SCHEMA.txt` 
### NOTE: 
5m may be too conservative based on future avaiablity of additional GPS & based on validity of Garmin 65S unit during testing phase. |
| **Project-level goal** | ±2 m | The aggregate accuracy target for the finished, defensible dataset, per the project proposal's Measurable Outcomes |

This table itself is the fix and ensures a concrete GPS accuracy scale.

## Recommended schema addition

`Status`'s current allowed values (`Existing`, `Needs_Verification`, `Missing_Tag`, `New_2025`, `Uncertain_Location`, `Removed`) have no value for **exact or near-duplicate coordinate records** — a real, distinct QA case (instance of the same tree logged twice) that isn't the same as `Removed` (physically confirmed gone). Recommend adding:

- **`Duplicate_Candidate`** — flagged by automated QA as a likely duplicate location; requires human review before deletion, never auto-removed.

## One naming inconsistency to fix

`SCHEMA.txt` uses `New_2025` as a `Status` value; `Field_Guide_Reference.txt` uses `New_Tree2025`. Pick one; `SCHEMA.txt`'s `New_2025` since that document is designated authoritative.

## Automated desk-based QA's advantages and disadvantages

A desk-based check against existing coordinates can flag *possible* issues (poor recorded accuracy, duplicate locations, missing attributes) but **cannot** confirm field-truth states like `Missing_Tag` that specifically means a crew physically found the tree but not its tag, a descreptancy which only in-situ validation can establish. The script leaves `Status` alone in that case rather than asserting something it can't know, and just notes the gap.

## Coordinate system note

Per `SCHEMA.txt` and the project proposal: primary storage is WGS 84 (EPSG:4326) decimal degrees, but analysis must happen in the working projection, **UTM Zone 11N (WGS 84)**. Run the validation script against the UTM 11N projected feature class, not the raw lat/long storage layer; the script's distance-based checks (duplicate tolerance) assume projected meters, and will silently misbehave against unprojected degree coordinates.

## Photo field name resolution
only the Phot vs 'Photo' header spelling. That's a structural naming issue, the same category as the other four discrepancies already in that file.