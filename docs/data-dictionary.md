# Data Dictionary — Reconciled Schema

**Status:** Living document — now a reconciliation *record* rather than an open reconciliation. As of 2026-07-20, `SCHEMA.txt` (v2) is the single authoritative schema and `Field_Guide_Reference.txt` has been formally retired (see its deprecation notice for details). This document preserves the reasoning behind each resolved conflict between `SCHEMA.txt`, the now-retired `Field_Guide_Reference.txt`, and the live MASTERDATASHEET column headers — the GIS Protocol Standardization deliverable.

## Fields currently active in the live dataset

| Field | Type / Units | In `SCHEMA.txt`? | In `Field_Guide_Reference.txt`? *(retired 2026-07-20)* | Notes |
|---|---|---|---|---|
| `Tree_ID` | Text, unique, permanent | ✅ | ✅ | Primary key. Never reassigned. |
| `Tag_ID` | Text | ✅ | ✅ | Physical tag number. `"None"` if missing. |
| `Species` | Text, scientific name | ✅ | ✅ | e.g. *Acer saccharum* |
| `Common_Name` | Text | ✅ | ✅ | Optional, public-facing |
| `DBH_in` | Float | ✅ | ⚠️ conflict *(resolved)* | **Resolved 2026-07-20 — see "Resolved conflict #1" below** |
| `Condition` | Text, domain-controlled | ✅ (as `Condition`) | ⚠️ named `Health` *(resolved)* | Good / Fair / Poor / Dead / Remove — naming difference only, resolved 2026-07-20 |
| `Latitude` / `Longitude` | Float, decimal degrees, WGS 84 | ✅ | ✅ | |
| `Altitude_m` | Float, meters | ✅ | — | |
| `GPS_Accuracy_m` | Float, meters | ✅ | — | **See "Resolved conflict #2" below** |
| `Perpendicular_Height_m`, `Inclination_deg`, `Inclined_Height_m` | Float | ✅ | ⚠️ Field_Guide only had flat `Height_m` *(resolved)* | SCHEMA.txt's consolidated-adjusted model is more precise and reflects actual live protocols -- `Field_Guide_Reference.txt`'s simpler version is retired [^1] |
| `Crown_Width_m`, `Crown_Base_Height_m` | Float, meters | ✅ | — | |
| `Date`, `Time` | Date / Text | ✅ | — | |
| `Notes` | Text | ✅ | — | Currently also carries surveyor name and structured comments as free text. This field may be removed from public facing datasets for the interrest of privacy. See "Worth doing later" |
| `Photo` | Text (path/URL) | ✅ (as `Photo`) | ⚠️ named `Photo_URL` *(resolved)* | Both live sheet and SCHEMA.txt use `Photo` -- resolved 2026-07-20, keeping `Photo` |

[^1]: SCHEMA.txt was created after the first two in-situ community data collection days (Dec. 2025 & April 2026), which is why its lean-adjusted height model postdates and supersedes Field_Guide_Reference.txt's simpler flat-height field.

## Fields defined in the schema but NOT yet present in the live dataset

| Field | Defined in | Status |
|---|---|---|
| `Status` | `SCHEMA.txt` (marked **Required**) | **Not yet implemented in the live sheet.** This is the most substantial gap between the schema-as-written and the schema-as-lived. The validation script in `scripts/point_validation_toolkit.py` is written to populate this field for the first time, not to compete with an existing field. As of SCHEMA.txt v2 (2026-07-20), the domain includes `Duplicate_Candidate`-- previously just a recommendation within this document, now formally adopted (see "Recommended schema addition" below, updated to reflect this). |
| `Surveyor_Name` | `SCHEMA.txt` | Not a separate column yet — currently embedded as the first line of the free-text `Notes`/comment field per the in-field collection protocol (e.g., "Team A, LEAD"). Worth eventually splitting into its own field, but that's a later cleanup, not urgent. This field may be removed from public facing datasets for the interrest of privacy. |

## Fields that existed only in `Field_Guide_Reference.txt` (retired)

`Genus`, `Condition_Notes`, `Xcoord`/`Ycoord`, `Last_Verified` existed only in the older reference doc and were never carried into the live schema. **RESOLVED 2026-07-20:** `Field_Guide_Reference.txt` has been formally retired (kept in the repo only as a deprecated historical record with its own deprecation notice) since the live data already tracked `SCHEMA.txt` almost exactly and these four fields were never adopted.

## Resolved conflict #1 — DBH units

`Field_Guide_Reference.txt` said `DBH_in` was measured in **centimeters**, contradicting its own field name (`_in` = inches) and contradicting `SCHEMA.txt`. The field data collection protocol settles it directly: volunteers are instructed to measure trunk diameter and enter it in **inches**. **`SCHEMA.txt` was correct -- the live mastersheet already used inches, so no data changed.** `Field_Guide_Reference.txt` has been retired (2026-07-20) with this units error documented in its deprecation notice, rather than left to confuse a future reader.

## Resolved conflict #2 — GPS accuracy has three different numbers, and that's actually fine

Across the documents, "accuracy" appears as ±2 m (project proposal's overall target), ±1–3 m (equipment description), a ≤3 m / 3–5 m / >5 m tier (`SCHEMA.txt`), and ≤5 m preferred / retake above 10 m (field collection cheat sheet). Separate what each one is measuring to avoid contradictions:

| Tier | Value | Purpose |
|---|---|---|
| **Collection-time floor** | Retake if reading is worse than ~5 m (10 m hard-stop) | What a volunteer accepts *in the moment*, per the GPS Best Practices Cheat Sheet [^2] |
| **Dataset classification** | ≤3 m Verified · 3–5 m Conditional · >5 m Needs correction | How `GPS_Accuracy_m` is interpreted *after* collection, per `SCHEMA.txt` [^3] |
| **Project-level goal** | ±2 m | The aggregate accuracy target for the finished, defensible dataset, per the project proposal's Measurable Outcomes |

This table itself fixes and ensures a concrete GPS accuracy scale.

[^2]: Open item -- confirm the ~5 m / 10 m hard-stop is actually being followed in-situ during collection days, not just jotten down.
[^3]: The 3–5 m / >5 m thresholds may prove too conservative once GPS Accuracy Testing (Objective 1) produces real device-comparison numbers, particularly given early indications on Garmin GPSMAP 65s accuracy -- revisit after that testing, not prior.

## Recommended schema addition

`Status`'s current allowed values (`Existing`, `Needs_Verification`, `Missing_Tag`, `New_2025`, `Uncertain_Location`, `Removed`) have no value for **exact or near-duplicate coordinate records** — a real, distinct QA case (instance of the same tree logged twice) that isn't the same as `Removed` (physically confirmed gone). Recommend adding:

- **`Duplicate_Candidate`** — flagged by automated QA as a likely duplicate location; requires human review before deletion, never auto-removed.

## One naming inconsistency -- resolved

`SCHEMA.txt` used `New_2025` as a `Status` value; `Field_Guide_Reference.txt` used `New_Tree2025`. **Resolved 2026-07-20:** `SCHEMA.txt`'s `New_2025` stands, since that document is authoritative -- and since `Field_Guide_Reference.txt` is now retired, there's no longer a second version in circulation to conflict with it.

## Automated desk-based QA's advantages and disadvantages

A desk-based check against existing coordinates can flag *possible* issues (poor recorded accuracy, duplicate locations, missing attributes) but **cannot** confirm field-truth states like `Missing_Tag` that specifically means a crew physically found the tree but not its tag, a descreptancy which only in-situ validation can establish. The script leaves `Status` alone in that case rather than asserting something it can't know, and just notes the gap.

## Coordinate system note

Per `SCHEMA.txt` and the project proposal: primary storage is WGS 84 (EPSG:4326) decimal degrees, but analysis must happen in the working projection, **UTM Zone 11N (WGS 84)**. Run the validation script against the UTM 11N projected feature class, not the raw lat/long storage layer; the script's distance-based checks (duplicate tolerance) assume projected meters, and will silently misbehave against unprojected degree coordinates.

## Photo field name -- resolved

The only discrepancy was `Photo` (`SCHEMA.txt`, live sheet) vs. `Photo_URL` (`Field_Guide_Reference.txt`) -- a naming difference only, no underlying data change. **Resolved 2026-07-20:** the field stays `Photo`, matching both `SCHEMA.txt` and the live mastersheet; `Field_Guide_Reference.txt`'s `Photo_URL` naming is retired along with the rest of that document.