# Tree Inventory GIS Modernization

A from-scratch effort to bring any community college campus tree inventory to a spatially accurate, standardized, and stakeholder-ready state -- GPS workflow, field protocol, GIS system, and web map -- documented as it's built rather than after the fact, to support transparency, repeatability, and defensibility.

🚧 **This project is in progress.** See [`PROJECT_STATUS.md`](./PROJECT_STATUS.md) for a current breakdown of what's done, underway, and still ahead. Nothing in this repo claims to be finished unless the status tracker says so. If you're picking this project up from someone else, treat `PROJECT_STATUS.md` -- *not this README* -- as the definitive word on where our tree inventory project actually stands. Once this pilot project is finished and the current project lead's service ends, this repo will serve as documentatiion for this project's continuation and as a reference for any community college that is interested in replicating this workflow.

## Goals

- Tree dataset is spatially accurate and defensible
- GPS workflow is tested and scalable
- Field operations are structured and repeatable
- Initial GIS model system is standardized and documented
- Web map is stable and stakeholder-ready

## Where to start (by what you're trying to do)

| If you're... | Start with |
|---|---|
| New to this project entirely | [`PROJECT_STATUS.md`](./PROJECT_STATUS.md), then [`docs/overview.md`](./docs/overview.md) |
| Checking or editing the data schema | [`docs/SCHEMA.md`](./docs/SCHEMA.md) is authoritative -- [`docs/data-dictionary.md`](./docs/data-dictionary.md) explains *why* it looks the way it does |
| Running the ArcGIS Pro workflow | [`gis/arcgis_pro_workflow.md`](./gis/arcgis_pro_workflow.md) |
| Understanding how raw data becomes GIS-ready | [`gis/database_development_workflow.md`](./gis/database_development_workflow.md) |
| Running or supervising a field collection day | [`protocols/field_data_collection_protocol.md`](./protocols/field_data_collection_protocol.md) + [`protocols/gps_best_practices_cheat_sheet.md`](./protocols/gps_best_practices_cheat_sheet.md) |
| Running the point validation script | [`scripts/point_validation_toolkit.py`](./scripts/point_validation_toolkit.py), guided by [`protocols/point_validation_SOP.md`](./protocols/point_validation_SOP.md) |
| Looking for the reasoning or prior art behind a decision | [`docs/REFERENCES.md`](./docs/REFERENCES.md) |
| Looking for the GIS project file or where the real spatial data lives | [`gis/README.md`](./gis/README.md) |
| Looking for exported data or test data | [`data/README.md`](./data/README.md) |
| Contributing a change | [`CONTRIBUTING.md`](./CONTRIBUTING.md) |

## Repository layout

```
├── PROJECT_STATUS.md      ← current, honest state of each objective — START HERE
├── CONTRIBUTING.md        ← rules for keeping docs in sync with reality
├── CHANGELOG.md           ← dated log of schema/methodology changes
├── CITATION.cff           ← how to cite this project
├── LICENSE                ← code license (MIT)
├── LICENSE-DATA.md        ← data licensing considerations (separate from code)
│
├── docs/
│   ├── overview.md            ← project background, stakeholders, objectives
│   ├── SCHEMA.md               ← THE authoritative field-by-field schema (v2)
│   ├── data-dictionary.md     ← reconciliation record — how schema conflicts were resolved, and why
│   ├── REFERENCES.md          ← external standards & comparable projects this work draws on
│   └── Archive/
│       └── Field_Guide_Reference.md   ← retired reference doc, kept only for history
│
├── protocols/
│   ├── point_validation_SOP.md              ← how desk-based QA classifies each point
│   ├── field_data_collection_protocol.md    ← in-field team roles & step-by-step workflow
│   └── gps_best_practices_cheat_sheet.md    ← GPS accuracy troubleshooting + Garmin GPSMAP 65s workflow
│
├── scripts/
│   └── point_validation_toolkit.py    ← ArcGIS Pro validation script
│
├── gis/
│   ├── project/        ← .aprx / .lyrx files (lightweight, versionable — not the real data)
│   └── README.md       ← where the actual GIS data (geodatabase, imagery) actually lives
│
└── data/
    ├── sample/         ← tiny test fixtures used to validate script logic (not real records)
    ├── exports/        ← validated, timestamped, public-tier data snapshots
    └── README.md       ← what belongs in each subfolder, and what doesn't
```

## License

Code in this repository is licensed under MIT (see `LICENSE`). Data licensing considerations are noted separately in `LICENSE-DATA.md`, since data and code often need different terms.

## Citation

See `CITATION.cff` if you're referencing this workflow or dataset elsewhere.