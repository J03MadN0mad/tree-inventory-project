# Project Status

Last updated: 2026-08-22

**NOTE TO FELLOW OR PROJECT LEAD**
This living document file exists as an up-to-date status page of the project's 8 Objectives. It is our goal for this repository to never overstate where the project actually is currently for the purpose of transperacncy and repeatability. We plan to update it as work happens. 


**Below are the current 8 Objectives for our project and what they aim to achieve:**
| # | Objective | Status | Notes |
|---|---|---|---|
| 1 | GPS Accuracy Testing & Integration | 🟡 In progress | Validation methodology (`protocols/point_validation_SOP.md`) including a tentative ArcPy script deployement (`scripts/point_validation_toolkit.py`) built and updated to match the project's master data-sheet dataset schema as shown in`docs/SCHEMA.md`. Garmin GPSMAP 65s now in the toolkit as a dedicated hardware track alongside smartphone GNSS -- *First live run against the real inventory not yet completed.* |
| 2 | Spatial Accuracy Finalization | ⚪ Not started | Depends on results of Objective 1's first run. |
| 3 | Field Data Collection Optimization (Fall Readiness) | 🟡 In progress | Existing in-field protocol formalized into `protocols/field_data_collection_protocol.md`. Field-tested once informally; not yet run against the standardized version in this repo. |
| 4 | GIS Protocol Standardization | 🟡 In progress | Finalizing final GIS software mapping workflow that will be public facing within the repo and as an instructral how-to Google Doc. 
Reconciled three previously-conflicting schema sources into `docs/data-dictionary.md` -- isolated and resolved a DBH unit error, a three-way GPS accuracy inconsistency, a naming drift, and identified that the schema's own `Status` field isn't yet implemented in the live data. |
| 5 | Web Map & Visualization Stability | ⚪ Not started | |To be started after the public launch of the Github Repo & the projects data hub (November 2026). |
| 6 | Multi-Stakeholder Integration | ⚪ Not started | | Depends on the success of a webmap and utilizing ESRI products for Live organizational utilization for the multi-stakeholder tree management goals of the project. |
| 7 | Mentorship & Shadowing Program (Fall Launch) | ⚪ Not started |  Objective fiesability for the Fal to be determined. |
| 8 | Documentation & Knowledge Repository | 🟡 In progress | This repository is that objective, actively being built and being prepared for public view (by end of October 2026). |

**Legend:** ⚪ Not started · 🟡 In progress · 🟢 Complete

## Current Blockers 

|| **RESOLVED 2026-07 License extension granted, although, full run against real production data is still queued (no estimate date of implementation yet) ||**

- ESRI/ArcGIS Pro access pending. || Waiting on the campus GIS department to resolve licensing 
before `point_validation_toolkit.py` can be run against the official MASTERSHEET in *ArcGIS Pro*. Script logic has been tested against a 2-row csv sample outside ArcGIS Pro to confirm the checks behave correctly; the full run against real production data is queued for as soon as license access is restored.

## Data quality issues found during sample testing (conducting check)
|| **Final review needed as of 2026-10-9**

- Tree_ID 2: Species "Quercia macrocarpa" -- likely typo for Quercus macrocarpa (bur oak)
- **RESOLVED 2026-09-26** Trailing whitespace present on some Species/Condition values. Worth a trim pass before final QA

## Access tiers (as currently planned)

- **Public Github repo** -- Documented transcribe of the project to be used as a reference to any community college wanting to replicate this workflow.
**Public web map** -- graphical point display, read-only
- **Datasheet + raw GIS resources** (.shp, geodatabase, .tiff) -- fully public, extractable, once the inventory is validated. Deliberately open to any community college wanting to replicate this workflow, not gated to internal academics only.
- **Facilities** -- needs elevated access to the web map for active management (likely edit-level, not just viewing). Specifics pending the department's ESRI licensing decision -- *##Revisit once that's settled.*

## What's tangible at this time

- A triage methodology and ArcPy script that populate the project's own existing `Status` field, matched against the actual live schema
- A reconciled data dictionary that resolved four concrete discrepancies across the project's three schema documents (see `docs/data-dictionary.md`)
- The full in-field data collection protocol and GPS best practices cheat sheet, formalized from existing working documents, including a new Garmin GPSMAP 65s GNSS hardware workflow *## UPDATE THIS*
- A documentation practice split across the project team's internal documentation and this public repo, with a defined rule for when something graduates from draft to public record
- The recommended schema addition (`Duplicate_Candidate`) is a formally approved change to the live schema *## CONFIRM*

## What's hasn't been implemented yet

- No live validation run has been executed against the actual inventory dataset. The script is written and matched to the real schema, but untested against real rows
- Objectives 5, 6, 7 have no documented output in this repo yet (To Be Initiated Late October 2026)
- The field collection protocol has been tested on multiple ocasions, informally & formally, prior to this repo's existence; *not yet re-validated against the version written here*
- **|| RESOLVED 2026-09 ||** (`Collection_Method`) is defined in the schema but not yet added to the live mastersheet.

## What I'd (the original project manager) do differently

**Lessons from the Validation phase:**

- The three-way schema drift (SCHEMA.md, Field_Guide_Reference.md, and the live sheet quietly disagreeing with each other) happened because nothing was validating new reference documents against the ones already in use. Next time, any new protocol or reference doc gets checked against the existing ones *before* it's adopted, not reconciled after the fact.
- **origin of diligence reporting in relation to LLM usage within this project**: With a limited, defined number of authorized work hours as a fellow, the highest-leverage split wasn't "AI vs. me"  it was mechanical work vs. judgment calls. Delegating fast, well-defined tasks (reconciling documents, drafting and troubleshooting of established scripts, formatting done within isolated draft documents (i.e. docs), and vetting reference literature) freed my actual hours for the prioritized tasks that needed a person: deciding which schema value wins when two documents disagree, judging (based on my GIS/forestry experience and the context of this project) whether a protocol is field-ready, deciding what's valid/relavent enough to publish. Criteria that must be reviewed and finalized by the fellow/project team. 
- The real fix (based on research of similar projects) for schema drift is an *automated validation step between Arboreal exports and the MASTERDATASHEET that checks incoming data against one canonical schema before it's merged in*, so a fourth conflicting version can't quietly form the same way the first three did during the project pilot year.

**Priorities before the next community data collection day (anticipated 2026-12) or your first collection day (if you are replicating this project at your home institution):**

- Technology limitations need to be addressed *before* a collection day, not discovered during one -- specifically, confirming GPS accuracy expectations (phone vs. Garmin, when to use which) are understood by every volunteer lead beforehand, not troubleshot tree-by-tree in the field -- which may introduce collector fatigue. 
- Data quality depends as much on consistent execution across volunteer sessions as it does on the schema itself. Building a small network of trained, reliable consistent group of student leaders, faculty, campus community members -- trained specifically on `field_data_collection_protocol.md` -- matters as much as any tooling decision. These leaders are the backbone of your project and will help ensure that volunteers collect accurate data and ensure a disconect between the collection protocols and said volunteers is avoided. 
- A deliberate partnership with the campus's newly developing GIS department is worth pursuing now rather than letting it happen informally --internally, it's a path to longer-term technical support and hosting; a working, documented tree inventory is a genuine contribution to a department still establishing itself. Treat your partnerships with care and proper communication, these are people who care about your work and take time out their schedules to help. 
