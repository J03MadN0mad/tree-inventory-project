# ⚠️ DEPRECATED — DO NOT USE FOR CURRENT FIELD NAMES, UNITS, OR STATUS VALUES

**Retired:** 2026-07-20
**Superseded by:** `SCHEMA.md` — the single authoritative schema reference for this project

This file is kept only as a historical record of the field reference used before schema
reconciliation. It is NOT current. Reconciliation against the live mastersheet and
`SCHEMA.md` (see `data-dictionary.md` for the full record) found:

- `DBH_in` was documented here as **centimeters** — contradicts the field's own name
  (`_in` = inches) and the field collection protocol, both of which use **inches**.
  `SCHEMA.md` was correct; the live mastersheet already used inches, so no data changed.
- This file's `Health` field is the same concept as `SCHEMA.md`'s `Condition` —
  a naming difference only, no data impact.
- This file's flat `Height_m` field was superseded by `SCHEMA.md`'s three-field
  lean-adjusted model (`Perpendicular_Height_m`, `Inclination_deg`, `Inclined_Height_m`),
  which is what's actually live.
- This file's `Photo_URL` naming was superseded by `SCHEMA.md`'s `Photo`, which is
  what's actually live. `Photo` remains the correct name.
- This file's `New_Tree2025` Status value was superseded by `SCHEMA.md`'s `New_2025`.
- `Genus`, `Condition_Notes`, `Xcoord`/`Ycoord`, and `Last_Verified`, defined only in
  this file, were never carried into the live schema and are not part of the current
  data model.

See `SCHEMA.md` for the current authoritative schema and `data-dictionary.md` for the
full reconciliation record.

---

*(Original content preserved below for reference only — do not treat as current.)*

---

Column-By-Column Field Guide (IMPORTANT for GIS)
Tree_ID:
Unique ID for each tree (critical for joining Arboreal + GPS)
Should never change
Format: 00123, 2022-045, etc.

Tag_ID:
Physical metal/plastic tag
If same as Tree ID → repeat
If missing → “None”

Species:
Scientific name (preferred for GIS)
e.g., Acer saccharum

Genus:
e.g., Acer, Quercus, Pinus

Common_Name:
Optional but useful for public-facing maps

DBH_in:
Diameter in centimeters
Must be numeric only
(no “cm” or “in”)

Height_m:
Height in meters (numeric)

Health:
Controlled list:
Good
Fair
Poor
Dead
Remove?

Condition_Notes:
Any specific notes from Arboreal or field crew.

Status:
Use for tracking verification (verifying the tree’s existence, identity, and tag in the field).
field verification states (Listed below)
Existing: (The tree is present, matches the ID, and has a valid tag.) → This is what you mark after field verification.
Needs_Verification: (The tree exists in the database but hasn’t been checked in the field yet.) → This is your default starting status for the 2022 data.
Missing_Tag: (The tree exists physically, but the tag is:Missing, Damaged, Illegible) → This tells you a re-tagging step is needed.
New_Tree2025: (New tree added since 2022)
Uncertain_Location: (Used for trees where the 2022 GPS point is:Off by >3–5 meters,Plotted in the wrong spot entirely,In an area with very dense canopy where exact location needs field validation) → This helps triage which trees need better GPS capture.
Removed: (Tree is no longer present; either removed or dead) 

Xcoord & Ycoord:
UTM Zone 11N (WGS 84) recommended
Numeric only
MUST match coordinate system used in GIS

Latitude & Longitude:
Decimal degrees (optional, but helpful for web maps)
If blank → GIS can calculate later

Photo_URL
URL or file path to image files
Skip if not applicable

Last_Verified:
Use format: YYYY-MM-DD
Helps track updates over time