# GIS Workstation — Folder Structure & Data Location

## What's actually in this `gis/` folder (and why)

This folder holds the **lightweight, versionable** parts of the ArcGIS Pro project --
things git can meaningfully track. It does **not** hold the actual vector or
raster data (feature classes, imagery, the working file geodatabase & shapefiles). That data is
binary, often large, and actively edited in ArcGIS Pro or within the GIS workspace -- a poor fit for git regardless of repo visibility. See `docs/SCHEMA.md`'s Data Governance Rules for the underlying
principle: edits happen in the GIS environment, not in git-tracked raw files.

```
gis/
  project/                          ← .aprx project file(s), .lyrx layer/style files
  database_development_workflow.md ← Excel-to-GIS staging, cleaning, reconciliation process
  arcgis_pro_workflow.md           ← ArcGIS Pro procedure: import, projection, NDVI, web map
  README.md                        ← this file
```

## Where the real data lives

*(PLACEHOLDER to be Filled in once finalized (Drive File) -- this is the one place a new team member/project lead should have to look.)*

- **Working File Geodatabase:** `[institutional server (Drive) path or ArcGIS Online/Portal item link TBD]`
- **Base imagery / raster layers:** `[server path (Drive) or ArcGIS Online item link TBD]`
- **Building footprints / boundary polygons:** `[server path (Drive) or item link TBD]`

## Reconnecting data sources on a new machine

When you open `project/*.aprx` on a different computer than the one it was authored on,
ArcGIS Pro may show broken data source links (a common issue when a project references
absolute paths). To fix:

1. In the Catalog pane, right-click the broken layer → **Repair** (single layer) or use
   **Map → Add Data → repair multiple** for several at once
2. Point it to the current location of the data listed above *(understand your established folder structure -- create a dedicated project folder within your host PC (i.e. Desktop or within your C: Drive))*
3. If this happens often across the team, consider switching the `.aprx` to reference
   data via a mapped network drive letter or UNC path that's consistent for everyone,
   or migrate fully to ArcGIS Online/Portal item references instead of local file paths

## Why the data isn't just committed to git anyway

GitHub hard-blocks individual files over 100MB and recommends repos stay under ~1GB
for performance -- file geodatabases and raster basemaps exceed past both routinely. Git
also can't meaningfully diff binary GIS formats, so version history on them wouldn't be
useful even if size weren't an issue. Git LFS exists for large files, but its free-tier
quota (about 1GB/month storage and bandwidth) is easily exhausted by GIS data at this
project's scale -- an institutional server or ArcGIS Online/Portal is the better home
either way.
