# ArcGIS Pro Mapping &amp; Analysis Workflow

**Campus Tree Inventory Project**

## Overview

This document covers the hands-on ArcGIS Pro procedure for turning validated tabular data into the project's actual spatial deliverables: the point feature class, NDVI vegetation analysis, and (later) the published web map. Where `gis/database_development_workflow.md` covers *getting data ready* for the GIS, this document picks up from there, *inside* ArcGIS Pro itself.

This is also the one document in this repo most likely to keep growing in your own hands rather than the current project's: it's written to be extended with your specific ArcGIS Pro setup, tool parameters, and any project-specific quirks, so a future fellow or project lead can repeat exactly what you did rather than reconstruct it from a generic ArcGIS tutorial.

---

<details>
<summary><strong>1. Data Import (CSV → GIS)</strong></summary>

**Step 1 -- Load CSV**

Add the cleaned, Master-tier CSV (see `gis/database_development_workflow.md` Section 2) to the ArcGIS Pro project. At this stage it's still just a table -- no geometry yet.

**Step 2 — Create XY points**

- **Tool:** `XY Table To Point`
- **Inputs:** X = `Longitude`, Y = `Latitude`
- **Coordinate system:** WGS 84 (EPSG:4326) -- this must match the Coordinate Refence System (CRS) the coordinates were actually captured in (see `SCHEMA.md`'s Coordinate System Standard); setting the wrong input CRS here doesn't throw an error, it just silently places every point in the wrong location.

**Important rule:** CSV layers are read-only for spatial editing. Once points exist as a CSV-backed layer, don't edit their geometry directly in that layer, that's what Section 2 (below) exists to fix.

</details>

<details>
<summary><strong>2. Create Authoritative Feature Class</strong></summary>

A CSV-backed XY layer isn't a real feature class — it's a live read of a text file, which is fragile (move the CSV, break the layer) and, per Section 1's rule, not something you can edit directly. To fix both problems in one step:

1. Export the XY points layer to a proper **Feature Class** inside a File Geodatabase
2. From this point forward, *that* feature class -- not the original CSV -- is the editable, authoritative dataset described in `gis/database_development_workflow.md`'s Core Principle

*This is the exact moment data stops being "staging" and becomes "the GIS."*

</details>

<details>
<summary><strong>3. Projection Management</strong></summary>

The storage and working projections are defined, authoritatively, in `SCHEMA.md`'s Coordinate System Standard (Primary storage: WGS 84 · Working projection: UTM Zone 11N) and explained in more depth in `data-dictionary.md`'s coordinate system note, including *why* it matters: `point_validation_toolkit.py`'s distance-based checks (duplicate detection, boundary checks) assume projected meters and will silently misbehave if run against unprojected lat/long. This document doesn't restate those values; here's the actual tool step, which is specific to this document:

- **Tool:** `Project` (Data Management Tool)
- Run this to produce the UTM Zone 11N working copy that the validation script actually gets pointed at. The WGS 84 version stays the permanent storage format; the UTM 11N version is generated from it, not maintained as a separate parallel dataset.

</details>

<details>
<summary><strong>4. Feature Editing</strong></summary>

Once points exist as a proper feature class, both geometry and attributes get corrected here -- this is the "editing happens in the GIS environment" half of `SCHEMA.md`'s Data Governance Rules actually being carried out.

**Adjusting point locations**, based on:
- Field verification (the field crew physically re-checked a point)
- High-resolution imagery, but only under the conditions `point_validation_SOP.md` Section 5 lays out for remote verification -- imagery-based correction isn't a substitute for field verification whenever there's genuine ambiguity about which tree a point refers to

**Updating attributes** -- at minimum:
- `Status`
- `Species`
- `DBH_in`
- `Collection_Method`

</details>

<details>
<summary><strong>5. Basemap &amp; Imagery Integration</strong></summary>

- **ESRI World Imagery** as the default basemap
- **Local aerial imagery**, where available, as a higher-resolution alternative
- Confirm alignment with the project's working projection (Section 3) before treating either as a reliable reference for placing or verifying points -- a basemap in the wrong projection will look plausible while being systematically offset; don't make your maps distracting whenever possible. 

</details>

<details>
<summary><strong>6. NDVI Analysis Workflow</strong></summary>

**Step 1 — Acquire imagery**

Multispectral or already-processed raster imagery covering the campus extent.

**Recommended source:** NAIP (National Agriculture Imagery Program) -- free, public domain, currently flown at roughly 0.6m resolution nationwide, currently used by this project. Available through USGS's The National Map (nationalmap.gov) or USDA's Geospatial Data Gateway (datagateway.nrcs.usda.gov). Worth knowing specifically for this step: NAIP ships as 4-band imagery -- Red, Green, Blue, and Near-Infrared -- required for NDVI analysis, if you choose to use that index. A standard RGB-only basemap like ESRI World Imagery doesn't carry a NIR band, so for NDVI specifically, NAIP is close to the only workable free option. If the campus's state or county GIS portal publishes its own orthoimagery, it's worth checking too -- some go sub-1ft, sharper than NAIP -- though they typically won't include the NIR band NAIP does.

**Step 2 — Calculate NDVI**
Formula: `NDVI = (NIR − Red) / (NIR + Red)`

This produces a per-pixel value from −1 to 1, where higher values indicate denser, healthier vegetation -- the basis for the color ramp in Step 3.

**Step 3 — Raster processing**

- Clip the raster to the campus boundary (working from a smaller extent avoids processing imagery for areas the project has no use for)
    *If a boundary polygon doesn't already exist, digitize it once in ArcGIS Pro by tracing the campus perimeter over aerial imagery, save it as its own feature class, and reuse it for every future clip -- this is a one-time setup, not a per-analysis step. If the campus's county assessor or planning department already publishes parcel boundaries, importing and dissolving the relevant parcels is usually faster and more accurate than hand-tracing* (ADD TO THIS ONCE I RUN THE PROCESS)

-Reclassify values if a simplified category scheme (e.g., low/medium/high vegetation) is more useful than a continuous gradient for a given map
- Apply a color ramp: red → low vegetation, green → high vegetation

</details>

<details>
<summary><strong>7. NDVI Troubleshooting</strong></summary>

**Raster not displaying correctly**
- *Cause:* Incorrect pixel type.
- *Solution:* Convert to 8-bit unsigned or float raster.

**Not visible in web map**
- *Cause:* Unsupported raster format for web publishing.
- *Solution:* Publish as a Tile Layer rather than a standard raster layer.

**Error 24078 (Unsupported data source)**
- *Cause:* Raster isn't in a format ArcGIS Online/Portal supports for publishing.
- *Solution:* Convert to TIFF (or another supported raster format) and re-export before publishing.

</details>

<details>
<summary><strong>8. Web Map Publishing</strong></summary>

**Holding this section for now.** This work aligns with Objective 5 (Web Map & Visualization Stability), which `PROJECT_STATUS.md` currently lists as ⚪ Not started -- work is planned to begin **October 2026**. Rather than fill this section in ahead of that work actually happening, this section will be written up once that objective is underway, matching the project's own rule of not documenting work as done, or as a fixed procedure, before it's real.

</details>

<details>
<summary><strong>9. Layer Organization Best Practice</strong></summary>

Default layer order, top to bottom:

1. Tree Inventory
2. NDVI
3. Aerial Imagery (bottom)

This keeps the point layer -- the thing most map interactions are actually about -- visually on top, with contextual layers underneath rather than obscuring it. *Less distractions = a good map*

</details>

<details>
<summary><strong>10. Known Issues &amp; Resolutions</strong></summary>

| Issue | Fix |
|---|---|
| NDVI appears monochrome | Adjust the symbology renderer |
| NDVI not showing in web map | Publish as a Tile Layer |
| Layer projection mismatch | Reproject using the `Project` tool (Section 3) |
| Unique ID Error (00374) | Enable "Allow assignment of unique numeric IDs" |

</details>

<details>
<summary><strong>11. Quality Control</strong></summary>

- Visually inspect all points against the basemap/imagery
- Symbolize by `Status` -- this makes QA issues visible at a glance rather than requiring a manual query, since every flagged record (`Uncertain_Location`, `Duplicate_Candidate`, `Needs_Verification`) is already carrying the information needed to color it distinctly
- Identify clusters, outliers, and missing areas -- clusters often indicate the duplicate-detection scenario in `gis/database_development_workflow.md` Section 3; outliers and gaps often indicate a `Status` this dataset hasn't caught yet

</details>

<details>
<summary><strong>12. References &amp; Best Practices</strong></summary>

Same recommendation as the sibling database development workflow document: fold these into `docs/REFERENCES.md` rather than maintaining a second, disconnected list --

- ESRI Raster Analysis Documentation
- USGS NDVI Guidelines
- GIS Urban Forestry Workflows
- Remote Sensing Fundamentals

I can draft these as proper `REFERENCES.md` entries (with the "what it informed" line the file's format requires) once the NDVI scope question above is settled — it'll be easier to say what each reference actually informed once NDVI's place in the objectives is explicit.

</details>

---

## Summary

This workflow gets validated tabular data from a CSV into a real, editable feature class, keeps that feature class correctly projected and up to date, layers in vegetation analysis on top of it, and -- starting this October -- will extend into a published web map. Everything here assumes the schema, accuracy tiers, and governance rules already defined in `docs/SCHEMA.md`; this document is where those rules get executed inside ArcGIS Pro, not where they get redefined.