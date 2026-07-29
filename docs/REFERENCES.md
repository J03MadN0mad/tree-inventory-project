# References & Prior Art

**Purpose:** This document records the external standards, tools, and comparable projects
that informed decisions made elsewhere in this repo (through the project) so those decisions are grounded in
outside precedent, and so a future readers can see *why* decisions were made regarding establish/tested project protocols and workflows. 

**How to use this file:** Each entry states what it is, links to it, and names which
decision(s) in this repo it actually informed. When a new source gets referenced in
conversation or in a doc, add it here rather than re-describing it inline elsewhere -- link
back to this file instead. 

---

## Metadata & accuracy standards

### ISO 19115 (Geographic Information Metadata)
International standard for describing geospatial dataset metadata. Notably includes a
formal "Lineage" element for documenting a dataset's sources and processing history -- this
file is, in effect, a manual version of that same concept applied to the whole project.
<https://mappingsystemsauthority.com/geospatial-data-standards/> (overview of how ISO 19115,
FGDC CSDGM, and NSSDA relate to each other)
**Informed:** the general documentation structure of this repo; referenced in
`point_validation_SOP.md` §8.

### FGDC CSDGM (Content Standard for Digital Geospatial Metadata, 1994)
The U.S. federal geospatial metadata standard that predates ISO 19115 and remains active for
legacy federal datasets.
<https://mappingsystemsauthority.com/geospatial-data-standards/>
**Informed:** same as above -- `point_validation_SOP.md` §8.

### NSSDA (National Standard for Spatial Data Accuracy, FGDC-STD-007.3-1998)
Federal methodology for reporting positional accuracy as RMSE at a 95% confidence level,
rather than a single bare accuracy number.
<https://www.fgdc.gov/standards/projects/accuracy/part3/index_html>
**Informed:** `data-dictionary.md`'s "Resolved conflict #2" -- separating the collection-time
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

### Esri ArcGIS Solutions -- Tree Management
Esri's packaged solution for municipal tree inventories: field data collection, inspection
workflows, condition tracking, and public-facing apps.
<https://doc.arcgis.com/en/arcgis-solutions/11.3/reference/use-tree-management.htm>
**Informed:** the overall shape of the `Status` field workflow (inventory → inspection →
condition → public map); the ESRI-path evaluation mentioned in `overview.md`.

### Davey Resource Group -- TreeKeeper / QA-QC tree inventory practice
Professional urban forestry inventory provider (i-Tree team member) that runs field-collected
GIS data through a formal QA/QC pass before treating it as authoritative.
<https://www.davey.com/environmental-consulting-services/urban-community-forestry/tree-inventory-management/>
**Informed:** the general shape of `point_validation_SOP.md` and
`point_validation_toolkit.py` - a defined QA/QC pass between raw field collection and an
authoritative dataset, the same pattern DRG uses professionally.

---

## Comparable institutional/campus tree inventories

### Iowa State University Campus Tree Inventory
A public, interactive GIS tree map maintained by Facilities Planning & Management, replacing
an older Excel + AutoCAD workflow.
<https://www.fpm.iastate.edu/planning_services/tree_inventory/>
**Informed:** this project's public web map + Facilities-operational access tier split
(`PROJECT_STATUS.md`, "Access tiers" section) -- ISU runs a near-identical structure at a
comparable institutional scale.

### University of Iowa -- ICIGO student GIS program
A student organization within UI's School of Earth, Environment & Sustainability that
conducts on-site tree studies and builds GIS-based digital tree inventory tools for partner
municipalities.
<https://iisc.uiowa.edu/colleges-and-departments/earth-environment-sustainability>
**Informed:** the volunteer/student-crew field collection model used in
`field_data_collection_protocol.md` - a comparable student-driven data collection structure.

---

## Comparable municipal case studies

### Washington, DC -- Urban Forestry Administration (DDOT)
Moved from PDA-based manual field collection (error-prone, manually merged back at the
office) to real-time, mobile ArcGIS-based field collection.
<https://www.esri.com/about/newsroom/arcwatch/protecting-urban-forests-the-modern-way>
**Informed:** the rationale in `gps_best_practices_cheat_sheet.md` for routing some points to
the Garmin GPSMAP 65s workflow rather than relying on smartphone GNSS alone
### City of Austin — GIS Tree Inventory (via Halff Associates)
A schema-driven ArcGIS Enterprise tree inventory (~22,300 trees) requiring a minimum of one
leaf/bark photo and one tree-form photo per record, tracked via ArcGIS Field Maps and
Dashboards.
<https://www.esri.com/about/newsroom/arcwatch/counting-trees>
**Informed:** the `Photo` field requirement and general schema shape in `SCHEMA.md`; a
directly comparable scale and structure to this project's own inventory.

---

## Correction log

*(Kept deliberately, in the same spirit as this repo's transperancy-first approach)*

- **2026-07-20:** An earlier informal mention of a "UIC" (University of Illinois Chicago)
  campus tree-map project could not be verified on follow-up research and has been dropped from consideration.
  Resolution: Replaced with the verified Iowa State and University of Iowa entries above.