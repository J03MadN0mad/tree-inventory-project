# Changelog

All notable changes to this project's schema and methodology are tracked here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/): dated, human-readable, newest first.

## [Unreleased]

### Added
- Initial repository scaffold: README, project status tracker, license, citation file
- Full project overview populated from the project proposal (`docs/overview.md`)
- Reconciled data dictionary resolving conflicts across `SCHEMA.txt`, `Field_Guide_Reference.txt`, and the live MASTERDATASHEET (`docs/data-dictionary.md`)
- GPS best practices cheat sheet, including a new Garmin GPSMAP 65s hardware workflow section (`protocols/gps_best_practices_cheat_sheet.md`)
- Field data collection protocol, formalized from the existing team workflow (`protocols/field_data_collection_protocol.md`)

### Changed
- Point validation methodology and script rewritten to populate the schema's own `Status` field (rather than a separate custom field), using real field names and the schema's own GPS accuracy tiers (`protocols/point_validation_SOP.md`, `scripts/point_validation_toolkit.py`)

### Fixed (documentation, not yet in live data)
- Identified `DBH_in` units error in `Field_Guide_Reference.txt` (says centimeters; actual protocol and field name confirm inches)
- Identified naming drift in `Status` domain value (`New_2025` vs `New_Tree2025`)
- Identified that `Status`, defined as required in `SCHEMA.txt`, is not yet present in the live dataset

### Pending
- First live validation run results against the actual inventory
- Decision on adding the recommended `Duplicate_Candidate` Status value to the live schema
- Sample MASTERGISSHEET rows to test the updated script logic against real data
