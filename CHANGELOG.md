# Changelog

All notable changes to this project's schema and methodology are tracked here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/): dated, human-readable, newest first.

### Pending
- First live validation run results against the actual inventory
- Sample MASTERGISSHEET rows to test the updated script logic against real data
(*Both to be complete by December 2026*)

## [2026-09-11]
### Added
- `Collection_Method` field added to SCHEMA.md -- records phone vs. Garmin GPSMAP 65s per point, enabling Objective 1's device-accuracy comparison

## [2026-07-20]
### Added
- Initial repository scaffold: README, project status tracker, license, citation file
- Full project overview populated from the project proposal (`docs/overview.md`)
- Reconciled data dictionary resolving conflicts across `SCHEMA.md`, `Field_Guide_Reference.md`, and the live MASTERDATASHEET (`docs/data-dictionary.md`)
- GPS best practices cheat sheet, including a new Garmin GPSMAP 65s hardware workflow section (`protocols/gps_best_practices_cheat_sheet.md`)
- Field data collection protocol, formalized from the existing team workflow (`protocols/field_data_collection_protocol.md`)

### Changed
- Point validation methodology and script rewritten to populate the schema's own `Status` field (rather than a separate custom field), using real field names and the schema's own GPS accuracy tiers (`protocols/point_validation_SOP.md`, `scripts/point_validation_toolkit.py`)
- SCHEMA v2, retiring Field_Guide_Reference.md, adding REFERENCES.md
- Decision on adding the recommended `Duplicate_Candidate` Status value to the live schema changed to resolved