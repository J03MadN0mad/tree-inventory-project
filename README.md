# Tree Inventory GIS Modernization

A from-scratch effort to bring a municipal/organizational (community college campus in the case of this specific prokect) tree inventory to a spatially accurate, standardized, and stakeholder-ready state GPS workflow, field protocol, GIS system, and web map, documented as it's built rather than after the fact, to ensure transparancy, repeatability, and defensability. 

🚧 **This project is in progress.** See [`PROJECT_STATUS.md`](./PROJECT_STATUS.md) for an honest, current breakdown of what's done, what's underway, and what's still ahead. Nothing in this repo claims to be finished unless the status tracker says so. Please ensure you, as the project lead/team implementing your own project, or new fellow project lead/team take the PROJECT_STATUS.md as a form to commnicate difinitive project status. 

## Goals

- Tree dataset is spatially accurate and defensible
- GPS workflow is tested and scalable
- Field operations are structured and repeatable
- GIS system is standardized and documented
- Web map is stable and stakeholder-ready

## Repository layout

```
├── PROJECT_STATUS.md      ← current, honest state of each objective (start here)
├── docs/
│   └── overview.md        ← project background and objective breakdown
├── protocols/
│   └── point_validation_SOP.md   ← GPS testing & point validation methodology
├── scripts/
│   └── point_validation_toolkit.py   ← ArcGIS Pro validation tool
├── LICENSE                ← code license (MIT)
└── LICENSE-DATA.md        ← data licensing notes
```

## Where to start

`PROJECT_STATUS.md` to be treated as the single source of truth for what's actually complete versus planned. It shows what has been been and what needs to be done by the project team. 

## License

Code in this repository is licensed under MIT (see `LICENSE`). Data licensing considerations are noted separately in `LICENSE-DATA.md`, since data and code often need different terms.

## Citation

See `CITATION.cff` if you're referencing this workflow or dataset elsewhere.
