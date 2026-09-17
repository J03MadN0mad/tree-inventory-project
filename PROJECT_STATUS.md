# Project Status

Last updated: 2026-08-22

**NOTE TO FELLOW OR PROJECT LEAD**
This living document file exists so this repository never overstates where the project actually is. Update it honestly as work happens. 


**Below are the current 8 Objectives for our project and what they aim to achieve:**
| # | Objective | Status | Notes |
|---|---|---|---|
| 1 | GPS Accuracy Testing & Integration | 🟡 In progress | Validation methodology and ArcPy script built and updated to match the real schema (`protocols/point_validation_SOP.md`, `scripts/point_validation_toolkit.py`). Garmin GPSMAP 65s now in the toolkit as a dedicated hardware track alongside smartphone GNSS. First live run against the real inventory not yet completed. |
| 2 | Spatial Accuracy Finalization | ⚪ Not started | Depends on results of Objective 1's first run. |
| 3 | Field Data Collection Optimization (Fall Readiness) | 🟡 In progress | Existing in-field protocol formalized into `protocols/field_data_collection_protocol.md`. Field-tested once informally; not yet run against the standardized version in this repo. |
| 4 | GIS Protocol Standardization | 🟡 In progress | Reconciled three previously-conflicting schema sources into `docs/data-dictionary.md` -- isolated and resolved a DBH unit error, a three-way GPS accuracy inconsistency, a naming drift, and identified that the schema's own `Status` field isn't yet implemented in the live data. |
| 5 | Web Map & Visualization Stability | ⚪ Not started | |
| 6 | Multi-Stakeholder Integration | ⚪ Not started | |
| 7 | Mentorship & Shadowing Program (Fall Launch) | ⚪ Not started | Planned for fall; out of scope for the summer push. |
| 8 | Documentation & Knowledge Repository | 🟡 In progress | This repository is that objective, actively being built. |

**Legend:** ⚪ Not started · 🟡 In progress · 🟢 Complete

## Current Blockers
- **ESRI/ArcGIS Pro access pending.** Waiting on the campus GIS department to resolve licensing 
before `point_validation_toolkit.py` can be run against the official MASTERSHEET in *ArcGIS Pro*. Script logic has been tested against a 2-row csv sample outside ArcGIS Pro to confirm the checks behave correctly; the full run against real production data is queued for as soon as license access is restored.

## Data quality issues found during sample testing (conducting check)
## *Final review needed*
- Tree_ID 2: Species "Quercia macrocarpa" -- likely typo for Quercus macrocarpa (bur oak)
- Trailing whitespace present on some Species/Condition values. Worth a trim pass before final QA

## Access tiers (as currently planned)

- **Public web map** -- graphical point display, read-only
- **Datasheet + raw GIS resources** (.shp, geodatabase, .tiff) -- fully public, extractable, once the inventory is validated. Deliberately open to any community college wanting to replicate this workflow, not gated to internal academics only.
- **Facilities** -- needs elevated access to the web map for active management (likely edit-level, not just viewing). Specifics pending the department's ESRI licensing decision -- revisit once that's settled.

## What's tangible at this time

- A triage methodology and ArcPy script that populate the project's own existing `Status` field, matched against the actual live schema
- A reconciled data dictionary that resolved four concrete discrepancies across the project's three schema documents (see `docs/data-dictionary.md`)
- The full in-field data collection protocol and GPS best practices cheat sheet, formalized from existing working documents, including a new Garmin GPSMAP 65s GNSS hardware workflow
- A documentation practice split across the project team's internal documentation and this public repo, with a defined rule for when something graduates from draft to public record
- The recommended schema addition (`Duplicate_Candidate`) is a formally approved change to the live schema

## What's not real yet (and won't be claimed as such)

- No live validation run has been executed against the actual inventory dataset. The script is written and matched to the real schema, but untested against real rows
- Objectives 5, 6, 7 have no documented output in this repo yet (To Be Initiated Late October 2026)
- The field collection protocol has been tested on multiple ocasions, informally & formally, prior to this repo's existence; not yet re-validated against the version written here
- (`Collection_Method`) is defined in the schema but not yet added to the live mastersheet.

## What I'd do differently
**(NOTE TO FELLOW: revisit once the first live validation run gives real results to reflect and consolidate on.)**

**Lessons from this phase:**

- The three-way schema drift (SCHEMA.md, Field_Guide_Reference.md, and the live sheet quietly disagreeing with each other) happened because nothing was validating new reference documents against the ones already in use. Next time, any new protocol or reference doc gets checked against the existing ones *before* it's adopted, not reconciled after the fact.
- **origin of diligence reporting in relation to LLM usage within this project**: With a limited, defined number of authorized work hours as a fellow, the highest-leverage split wasn't "AI vs. me"  it was mechanical work vs. judgment calls. Delegating fast, well-defined tasks (reconciling documents, drafting and troubleshooting of established scripts, formatting) freed my actual hours for the prioritized tasks that needed a person: deciding which schema value wins when two documents disagree, judging whether a protocol is field-ready, deciding what's true enough to publish. Criteria that must be reviewed and finalized by the fellow/project team. 
- The real fix for schema drift is an automated validation step between Arboreal exports and the MASTERDATASHEET that checks incoming data against one canonical schema before it's merged in, so a fourth conflicting version can't quietly form the same way the first three did.

**Priorities before the next community data collection day:**

- Technology limitations need to be addressed *before* a collection day, not discovered during one -- specifically, confirming GPS accuracy expectations (phone vs. Garmin, when to use which) are understood by every volunteer beforehand, not troubleshot tree-by-tree in the field -- which may introduce collector fatigue. 
- Data quality depends as much on consistent execution across volunteer sessions as it does on the schema itself. Building a small network of trained, reliable student leaders -- trained specifically on `field_data_collection_protocol.md` -- matters as much as any tooling decision.
- A deliberate partnership with the campus's newly developing GIS department is worth pursuing now rather than letting it happen informally --internally, it's a path to longer-term technical support and hosting; a working, documented tree inventory is a genuine contribution to a department still establishing itself.
