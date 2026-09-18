# Project Overview

## Background

This project expands a 2022 campus tree inventory into a full GIS-based system for mapping and managing campus trees. It integrates existing Arboreal app collection data (tagged trees, GPS points, attributes) with ongoing in-field verification to fill gaps in the original dataset. The end goal is a centralized, interactive geospatial database usable both operationally (Facilities maintenance and planning) and educationally (faculty, students, and public access).

## Why this matters

Campus trees carry ecological, educational, and aesthetic value. Reliable, accessible tree data supports maintenance planning, research, and climate resilience reporting, and advances institutional environmental stewardship goals.

## Stakeholders

| Group | Role |
|---|---|
| Fellow & Project Team | Project coordination and GIS development |
| Facilities Department | Tree care, maintenance, and qualitative data updates |
| Sustainability | Landscape design, carbon monitoring, sustainability reporting |
| Faculty & Students | Research and education (read/extraction access) |
| General Public | Community education via public-facing map (read-only) |

## Objectives

See [`PROJECT_STATUS.md`](../PROJECT_STATUS.md) for current status of each. The eight objectives for Summer 2026:

1. GPS Accuracy Testing & Integration
2. Spatial Accuracy Finalization
3. Field Data Collection Optimization (Fall Readiness)
4. GIS Protocol Standardization
5. Web Map & Visualization Stability
6. Multi-Stakeholder Integration
7. Mentorship & Shadowing Program (Fall Launch)
8. Documentation & Knowledge Repository (this repository)

    *Note: NDVI (vegetation index) analysis, part of the ArcGIS Pro     
    workflow (see `gis/arcgis_pro_workflow.md`), is a supplementary
    technique for visualizing tree canopy -- not tied to a specific
    objective above, and not a required deliverable of any one of them.*

*Note: NDVI (vegetation index) analysis, part of the ArcGIS Pro workflow (see
`gis/arcgis_pro_workflow.md`), is a supplementary technique for visualizing tree canopy -- not tied to a specific objective above, and not a required deliverable of any one of them.Each project is free to incorporate this workflow as pleased.*

## Measurable outcomes (from the project proposal)

| Outcome | Target |
|---|---|
| Tree data coverage | 100% of existing + newly identified trees verified and mapped; GPS accuracy ±2 m |
| Data integration & quality | All Arboreal, GPS, and field data integrated into one standardized GIS dataset after QA/QC |
| GIS system established | Authoritative ArcGIS Pro feature class created, projected, and validated (see `gis/arcgis_pro_workflow.md`) |  
| Mapping deliverables | Interactive + static web map (QGIS- or ESRI-based) |
42  | Operational use | Facilities/Sustainability staff trained and using GIS tools |
| Educational impact | Used in ≥2 courses/research projects; public map online |
| Sustainability impact | Tree data linked to carbon/green-asset tracking and reporting |

## Data sources

- **Arboreal software exports** — species, DBH, height, condition
- **Physical tree tags** — metal tags linking field observations to digital records
- **Imagery layers & basemaps** — aerial imagery, building footprints, land use
- **GPS coordinates** — from the 2022 inventory, pending QA/QC before GIS integration (this is what `protocols/point_validation_SOP.md` addresses)

## Platform direction

The project is evaluating both an open-source path (QGIS + qgis2web, hosted on institutional servers or GitHub Pages) and an ESRI path (ArcGIS Pro → ArcGIS Online → Field Maps), and will settle on one based on scalability and long-term maintainability once both have been tested.

## Documentation approach

Working notes, daily logs, and in-progress drafts are kept in a private Obsidian vault. A protocol or piece of documentation moves into this public repository only once it's stable enough that someone else could follow it without the author in the room — this repo is the polished record, not the scratch pad.
