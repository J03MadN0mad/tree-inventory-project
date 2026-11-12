# Project Overview

## Background

This project expands a 2022 campus tree inventory initiatie into a full GIS-based system for mapping and potentially managing campus trees. It integrates existing Arboreal tree app collection data (tagged trees, GPS points, attributes) with ongoing in-field verification to fill gaps in the original dataset. The end goal is a centralized, interactive geospatial database usable both operationally (Facilities maintenance and planning) and educationally (faculty, students, and public access).

## Why this matters

Campus trees carry ecological, educational, and aesthetic value. Reliable, accessible tree data supports maintenance planning, research, and climate resilience reporting, and advances institutional environmental stewardship goals.

## Stakeholders *## Revise last 2 points to ensure other campuses have extract access too*

| Group | Role |
|---|---|
| Fellow & Project Team | Project coordination and GIS development |
| Facilities Department | Tree care, maintenance, and qualitative data updates |
| Sustainability | Landscape design, carbon monitoring, sustainability reporting | *##Seek more info here*
| Faculty & Students | Research and education (read/extraction access) | 
| General Public | Community education via public-facing map (read-only) |

## Objectives

See [`PROJECT_STATUS.md`](../PROJECT_STATUS.md) for current status of each. The eight objectives for 2026:

1. GPS Accuracy Testing & Integration
2. Spatial Accuracy Finalization
3. Field Data Collection Optimization (Fall Readiness)
4. GIS Protocol Standardization
5. Web Map & Visualization Stability
6. Multi-Stakeholder Integration
7. Mentorship & Shadowing Program (Possible Fall Launch)
8. Documentation & Knowledge Repository (this repository)

## Measurable outcomes (from the project proposal) *## Revise his after master sweep and mapping redo*

| Outcome | Target |
|---|---|
| Tree data coverage | 100% of existing + newly identified trees verified and mapped; GPS accuracy ±2 m |
| Data integration & quality | All Arboreal, GPS, and field data integrated into one standardized GIS dataset after QA/QC |
| GIS system established | Authoritative ArcGIS Pro feature class created, projected, and validated (see `gis/arcgis_pro_workflow.md`) |  
| Mapping deliverables | Interactive + static web map (QGIS- or ESRI-based) |
| Operational use | Facilities/Sustainability staff trained and using GIS tools |
| Educational impact | Used in ≥2 courses/research projects; public map online |
| Sustainability impact | Tree data linked to carbon/green-asset tracking and reporting |

## Data sources

- **Arboreal software exports** — species, DBH, height, condition
- **Physical tree tags** — metal tags linking field observations to digital records
- **Imagery layers & basemaps** — aerial imagery, building footprints, land use
- **GPS coordinates** — from the 2022 inventory and forward, pending QA/QC before GIS integration (this is what `protocols/point_validation_SOP.md` addresses)

## Platform direction 

The project originally wanted to evaluate both an open-source path (QGIS + qgis2web, hosted on institutional servers or GitHub Pages) and an ESRI path (ArcGIS Pro → ArcGIS Online → Field Maps), to settle on one based on scalability and long-term maintainability once both have been tested. Althouhg, the latter option was chosen
for this pilot project to due time constraints and the ESRI licensing becoming available for the project. 

*(Note: Future team(s) of this project, or from outside campuses, will be free to implement an open-source path as they see fit), This is your project and can scale as you please based on your school, resources, and goals for your porject.*

## Documentation approach

Working notes, daily logs, and in-progress drafts are kept in private at the descretion of the project team. A protocol or piece of documentation moves into this public repository only once it's stable enough that someone else could follow it *"without the author in the room"* as a polished repeatable and userfriendly record for 
referece/inspiration. 
