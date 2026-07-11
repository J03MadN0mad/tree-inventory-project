# Project Status

Last updated: 2026-07-11

This file exists so this repository never overstates where the project actually is. Update it honestly as work happens — a "Not started" row is not a failure, it's information.

| # | Objective | Status | Notes |
|---|---|---|---|
| 1 | GPS Accuracy Testing & Integration | 🟡 In progress | Validation methodology and ArcPy triage script built (`protocols/point_validation_SOP.md`, `scripts/point_validation_toolkit.py`). First live run against the real inventory not yet completed. |
| 2 | Spatial Accuracy Finalization | ⚪ Not started | Depends on results of Objective 1's first run. |
| 3 | Field Data Collection Optimization (Fall Readiness) | ⚪ Not started | Protocol previously field-tested once outside this repo; not yet formalized here. |
| 4 | GIS Protocol Standardization | ⚪ Not started | |
| 5 | Web Map & Visualization Stability | ⚪ Not started | |
| 6 | Multi-Stakeholder Integration | ⚪ Not started | |
| 7 | Mentorship & Shadowing Program (Fall Launch) | ⚪ Not started | Planned for fall; out of scope for the summer push. |
| 8 | Documentation & Knowledge Repository | 🟡 In progress | This repository is that objective, actively being built. |

**Legend:** ⚪ Not started · 🟡 In progress · 🟢 Complete

## What's real right now

- A tested triage methodology for classifying every existing GIS point as Verified, Needs Remote Verification, Needs Field Remeasurement, or Flagged for Removal
- A working ArcPy script implementing that methodology, ready to run against the live feature class
- A documentation practice split across a private working vault (Obsidian) and this public repo, with a defined rule for when something graduates from draft to public record

## What's not real yet (and won't be claimed as such)

- No live validation run has been executed against the actual inventory dataset
- Objectives 2–7 have no documented output in this repo yet
- The field collection protocol referenced in earlier planning has been tested once, informally, but not written up here

## What I'd do differently

*(Fill this in honestly once there's enough completed to reflect on — a fellowship-style project is more credible with one real lesson learned than with a longer feature list.)*
