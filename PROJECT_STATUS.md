# Project Status

Last updated: 2026-07-11

This file exists so this repository never overstates where the project actually is. Update it honestly as work happens — a "Not started" row is not a failure, it's information.

| # | Objective | Status | Notes |
|---|---|---|---|
| 1 | GPS Accuracy Testing & Integration | 🟡 In progress | Validation methodology and ArcPy script built and updated to match the real schema (`protocols/point_validation_SOP.md`, `scripts/point_validation_toolkit.py`). Garmin GPSMAP 65s now in the toolkit as a dedicated hardware track alongside smartphone GNSS. First live run against the real inventory not yet completed. |
| 2 | Spatial Accuracy Finalization | ⚪ Not started | Depends on results of Objective 1's first run. |
| 3 | Field Data Collection Optimization (Fall Readiness) | 🟡 In progress | Existing in-field protocol formalized into `protocols/field_data_collection_protocol.md`. Field-tested once informally; not yet run against the standardized version in this repo. |
| 4 | GIS Protocol Standardization | 🟡 In progress | Reconciled three previously-conflicting schema sources into `docs/data-dictionary.md` — resolved a DBH unit error, a three-way GPS accuracy inconsistency, a naming drift, and identified that the schema's own `Status` field isn't yet implemented in the live data. |
| 5 | Web Map & Visualization Stability | ⚪ Not started | |
| 6 | Multi-Stakeholder Integration | ⚪ Not started | |
| 7 | Mentorship & Shadowing Program (Fall Launch) | ⚪ Not started | Planned for fall; out of scope for the summer push. |
| 8 | Documentation & Knowledge Repository | 🟡 In progress | This repository is that objective, actively being built. |

**Legend:** ⚪ Not started · 🟡 In progress · 🟢 Complete

## What's real right now

- A triage methodology and ArcPy script that populate the project's own existing `Status` field, matched against the actual live schema (not a guessed-at one)
- A reconciled data dictionary that resolved four concrete, real discrepancies across the project's own three schema documents (see `docs/data-dictionary.md`)
- The full in-field data collection protocol and GPS best practices cheat sheet, formalized from existing working documents, including the new Garmin GPSMAP 65s hardware workflow
- A documentation practice split across a private working vault (Obsidian) and this public repo, with a defined rule for when something graduates from draft to public record

## What's not real yet (and won't be claimed as such)

- No live validation run has been executed against the actual inventory dataset — the script is written and matched to the real schema, but untested against real rows
- Objectives 2, 5, 6, 7 have no documented output in this repo yet
- The recommended schema addition (`Duplicate_Candidate`) is a recommendation in this repo, not yet an approved change to the live schema
- The field collection protocol has been tested once, informally, prior to this repo's existence — not yet re-validated against the version written up here

## What I'd do differently

*(Fill this in honestly once there's enough completed to reflect on — a fellowship-style project is more credible with one real lesson learned than with a longer feature list.)*
