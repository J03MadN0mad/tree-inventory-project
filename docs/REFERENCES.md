# References & Prior Art

**Purpose:** This document records the external standards, tools, and comparable projects that informed decisions made elsewhere in this repo -- so those decisions are grounded in outside precedent rather than invented from scratch, for the purpose of future reference and to communicate *why* a choice was made, not just what it was.

**How to use this file:** each entry states what it is, links to it, and names which
decision(s) in this repo it actually informed. Except for *## General Relevant Data/Reference Sources* which is use for inspirational or informative references for the project.
 When a new source gets referenced in conversation or in a doc, add it here rather than re-describing it inline elsewhere -- link
back to this file instead. Same consolidation logic used for `SCHEMA.md` /
`data-dictionary.md`: one authoritative place, everything else points to it.

---

## Metadata & accuracy standards

### ISO 19115 (Geographic Information — Metadata)
International standard for describing geospatial dataset metadata. Notably includes a
formal "Lineage" element for documenting a dataset's sources and processing history — this
file is, in effect, a manual version of that same concept applied to the whole project.
<https://mappingsystemsauthority.com/geospatial-data-standards/> (overview of how ISO 19115,
FGDC CSDGM, and NSSDA relate to each other)
**Informed:** the general documentation structure of this repo; referenced in
`point_validation_SOP.md` §8.

### FGDC CSDGM (Content Standard for Digital Geospatial Metadata, 1994)
The U.S. federal geospatial metadata standard that predates ISO 19115 and remains active for
legacy federal datasets.
<https://mappingsystemsauthority.com/geospatial-data-standards/>
**Informed:** same as above — `point_validation_SOP.md` §8.

### NSSDA (National Standard for Spatial Data Accuracy, FGDC-STD-007.3-1998)
Federal methodology for reporting positional accuracy as RMSE at a 95% confidence level,
rather than a single bare accuracy number.
<https://www.fgdc.gov/standards/projects/accuracy/part3/index_html>
**Informed:** `data-dictionary.md`'s "Resolved conflict #2" — separating the collection-time
floor, dataset classification tiers, and project-level accuracy goal instead of treating
them as one contradictory number; directly referenced in `point_validation_SOP.md` §8.

---

## Comparable tools & schema models

### USDA Forest Service i-Tree suite
Peer-reviewed software suite (Eco, Streets, Canopy, and others) used by municipalities,
universities, and volunteers nationwide for tree inventory and ecosystem-benefit analysis.
<https://www.itreetools.org> · <https://research.fs.usda.gov/products/dataandtools/i-tree>
**Informed:** `SCHEMA.md`'s Overview section (cites i-Tree-inspired workflows); general
influence on which attributes this project tracks (species, DBH, condition, canopy).

OpenTreeMap (Azavea)

Open-source software for collaborative, geography-enabled urban tree inventory, used by municipal and community tree-map projects (PhillyTreeMap, UrbanForestMap, TreeMapLA, and others) to let a mix of professionals and public volunteers contribute to the same inventory. https://github.com/OpenTreeMap/otm-core Informed: the general feasibility of a mixed professional/volunteer contribution model for this project's own dataset -- a comparable open-source precedent for combining crowd-sourced and professionally-verified tree records, distinct from Esri's managed solution below.

### Esri ArcGIS Solutions — Tree Management
Esri's packaged solution for municipal tree inventories: field data collection, inspection
workflows, condition tracking, and public-facing apps.
<https://doc.arcgis.com/en/arcgis-solutions/11.3/reference/use-tree-management.htm>
**Informed:** the overall shape of the `Status` field workflow (inventory → inspection →
condition → public map); the ESRI-path evaluation mentioned in `overview.md`.

### Davey Resource Group — TreeKeeper / QA-QC tree inventory practice
Professional urban forestry inventory provider (i-Tree team member) that runs field-collected
GIS data through a formal QA/QC pass before treating it as authoritative.
<https://www.davey.com/environmental-consulting-services/urban-community-forestry/tree-inventory-management/>
**Informed:** the general shape of `point_validation_SOP.md` and
`point_validation_toolkit.py` — a defined QA/QC pass between raw field collection and an
authoritative dataset, the same pattern DRG uses professionally.

---

## Comparable institutional/campus tree inventories

### Iowa State University Campus Tree Inventory
A public, interactive GIS tree map maintained by Facilities Planning & Management, replacing
an older Excel + AutoCAD workflow.
<https://www.fpm.iastate.edu/planning_services/tree_inventory/>
**Informed:** this project's public web map + Facilities-operational access tier split
(`PROJECT_STATUS.md`, "Access tiers" section) — ISU runs a near-identical structure at a
comparable institutional scale.

### University of Iowa — ICIGO student GIS program
A student organization within UI's School of Earth, Environment & Sustainability that
conducts on-site tree studies and builds GIS-based digital tree inventory tools for partner
municipalities.
<https://iisc.uiowa.edu/colleges-and-departments/earth-environment-sustainability>
**Informed:** the volunteer/student-crew field collection model used in
`field_data_collection_protocol.md` — a comparable student-driven data collection structure
at another Iowa institution.

---

## Comparable municipal case studies

### Washington, DC — Urban Forestry Administration (DDOT)
Moved from PDA-based manual field collection (error-prone, manually merged back at the
office) to real-time, mobile ArcGIS-based field collection.
<https://www.esri.com/about/newsroom/arcwatch/protecting-urban-forests-the-modern-way>
**Informed:** the rationale in `gps_best_practices_cheat_sheet.md` for routing some points to
the Garmin GPSMAP 65s workflow rather than relying on smartphone GNSS alone — the same
"upgrade field hardware specifically where accuracy actually breaks down" logic.

### City of Austin — GIS Tree Inventory (via Halff Associates)
A schema-driven ArcGIS Enterprise tree inventory (~22,300 trees) requiring a minimum of one
leaf/bark photo and one tree-form photo per record, tracked via ArcGIS Field Maps and
Dashboards.
<https://www.esri.com/about/newsroom/arcwatch/counting-trees>
**Informed:** the `Photo` field requirement and general schema shape in `SCHEMA.md`; a
directly comparable scale and structure to this project's own inventory.

---

## Correction log

- **2026-07-20:** An earlier informal mention of a "UIC" (University of Illinois Chicago) campus tree-map project could not be verified on follow-up research and has been dropped. Replaced with the verified Iowa State and University of Iowa entries above.

## General Relevant Data/Reference Sources

### PBS Terra - EXTREME  HEAT Is Getting Worse, and It Will Reshape Earth FOREVER 
***"Extreme heat is the deadliest kind of weather on Earth. Even as deaths from most weather decline, heat-related mortality is on the rise. Part of the reason? The very nature of extreme heat is changing. Climate change has unleashed a dramatic increase in dangerous “wet-bulb” events, when heat and humidity combine to overwhelm the human body’s ability to cool itself. In these episodes, we explore how extreme heat has begun redrawing the map of where humans can safely live, and the dangers and adaptations facing us in this new world."***
PBS video on our current understanding of Urban Heat Islands in the US, their enviornmental & socio-economic causes, study, and potention resolutions.
<https://www.youtube.com/watch?v=GL3YUDYWcTI>
