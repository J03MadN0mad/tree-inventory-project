# **Tree Inventory GIS Schema Reference**

### Campus Tree Inventory & Climate Action Mapping Project

---

## **Document Status**

* **Version:** 2 — Updated 2026-07-20
* This is the **single authoritative schema reference** for this project's master datasheet. Basically, the attribute data per each tree that we are interested in collecting. It also servers as a reference to the master data sheet. 
`Field_Guide_Reference.md` has been formally retired as of this version and it remains in the repo only as a deprecated historical record and should not be treated as a live source. See that file's deprecation notice the reasonaing.
* **Change from v1:** Added `Duplicate_Candidate` to the `Status` domain below -- an automated-QA-only flag (never field-confirmed, never auto-deletes) that `point_validation_toolkit.py` was already setting in practice. This formalizes what was previously only a recommendation in `data-dictionary.md`.

---

## **Overview**

This document defines the authoritative schema for this project's campus tree inventory GIS database.
It is designed to support:

* Field data collection (Arboreal / mobile GIS)
* Data management (excel master data sheet for all recorded trees)
* Spatial analysis (ArcGIS Pro) *## Removed QGIS as that objected will not to fulfilled this cohort.*
* Web mapping (ArcGIS Online) *## Maybe if time allows Novemeber*
* Long-term tree asset management and climate reporting 

The schema follows best practices from:

* Urban forestry GIS standards
* ESRI data models
* Campus-scale inventory systems (e.g., i-Tree, OpenTreeMap-inspired workflows)

---

# **Field Definitions**

## **Identification Fields**

### **Tree_ID**

* **Type:** Text (String)
* **Required:** Yes
* **Description:** Permanent unique identifier for each tree record.
* **Rules:**

  * Must be unique
  * Never reassigned or reused
  * Must be stored/imported as *Text*, never Number -- both formats below use
    leading zeros that a numeric type will silently strip; this may affect how the GIS reads and displays this.
* **Format Examples:**
  * `0001` -- tagged tree: 4-digit, zero-padded, sequential *## Double check this via the master sheet 
  * `UT-001` -- untagged tree ("UT" = Untagged): `UT-` prefix + 3-digit,
    zero-padded, sequential
* **Purpose:** Primary key for GIS joins and long-term tracking 
*See `arcgis_pro_workflow.md` for explanation and practice of GIS join* *## Validate this later*

---

### **Tag_ID**

* **Type:** Text (String)
* **Required:** No
* **Description:** Physical tag attached to tree.
* **Rules:**

  * May match Tree_ID
  * Use `"None"` if missing
* **Purpose:** Field identification reference

---

## **Species Information**

### **Species**

* **Type:** Text (String)
* **Required:** Yes (if known)
* **Description:** Scientific (binomial) species name.
* **Example:** *Acer saccharum*
* **Purpose:** Standardized ecological classification

---

### **Common_Name**

* **Type:** Text (String)
* **Required:** No
* **Description:** Public-friendly tree name.
* **Example:** Sugar Maple
* **Purpose:** Web map usability

---

## **Tree Measurements**

### **DBH_in**

* **Type:** Float (Double)
* **Required:** No
* **Units:** Inches
* **Description:** Diameter at Breast Height (1.37m / 4.5 ft).
* **Rules:**

  * Numeric only
  * No units stored in field
* **Purpose:** Biomass and carbon estimation

---

### **Perpendicular_Height_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Vertical tree height measurement.

---

### **Inclination_deg**

* **Type:** Float
* **Units:** Degrees
* **Description:** Lean angle of tree from vertical.

---

### **Inclined_Height_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Height adjusted for lean.

---

### **Crown_Width_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Average canopy width. *## Confirm if truely average or just 1 measurement of one tree*

---

### **Crown_Base_Height_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Height from ground to lowest live branch.

---

## **Condition & Status**

### **Condition**

* **Type:** Text (Domain Controlled)
* **Required:** Yes
* **Allowed Values:**

  * Good
  * Fair
  * Poor
  * Dead
  * Remove
* **Purpose:** Tree health classification

---

### **Status**  *## Sweep Mastersheet for this*

* **Type:** Text (Domain Controlled)
* **Required:** Yes
* **Description:** Workflow tracking field for validation.

#### **Allowed Values & Definitions**

* **Existing**

  * Verified in field, matches ID and tag

* **Needs_Verification**

  * Default for legacy data not yet field-checked *## Run ALL pre-2025 for this this weekend?*

* **Missing_Tag**

  * Tree present, tag missing/damaged/illegible

* **New_2025**

  * Newly added tree (post-2022 dataset) *##confirm all these for 2025+ have this*

* **Uncertain_Location**

  * GPS error >3–5m or unclear placement *## mindful of this during sweep*

* **Duplicate_Candidate**

  * Automated QA flagged this record as sharing a near-identical location, and/or a duplicate `Tag_ID`, with another record.
  * Set only by desk-based validation (`point_validation_toolkit.py`) -- never a field-confirmed state.
  * *CRITICAL*: Requires human review before any deletion. Never auto-removed.
  * As a reminder: it is generally good practice to never delete data that is collected. Even when the data is 
  incorrected (storing bad data ≠ using bad data), it's best to keep it store somewhere within your private
  Drive or chose form of project data storage.

* **Removed**

  * Tree no longer present

---

## **Location Data**

### **Latitude**

* **Type:** Float (Double)
* **Units:** Decimal Degrees
* **Example:** 33.971611
* **Purpose:** Web mapping and GPS compatibility

---

### **Longitude**

* **Type:** Float (Double)
* **Units:** Decimal Degrees
* **Example:** -117.383740

---

### **Altitude_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Elevation above sea level

---

### **GPS_Accuracy_m**

* **Type:** Float
* **Units:** Meters
* **Description:** Estimated positional accuracy at time of capture
* **Use:**

  * ≤3m → Verified
  * 3–5m → Conditional  *## Needs verification via remote validation?*
  * > 5m → Needs correction

---

### **Collection_Method**

* **Type:** Text (Domain Controlled)
* **Allowed Values:** Smartphone_GNSS, Garmin_GPSMAP_65s
* **Required:** No
* **Description:** Device used to capture this point's coordinates.
* **Purpose:** Lets GPS Accuracy Testing (Objective 1) compare device performance.
---

## **Metadata Fields**

### **Date**

* **Type:** Date
* **Format:** YYYY-MM-DD
* **Description:** Date of observation

---

### **Time**

* **Type:** Text or Time
* **Format:** HH:MM (24-hour)
* **Description:** Time of observation

---

### **Surveyor_Name**

* **Type:** Text
* **Description:** Person or team collecting data

#### Due to privacy concerns, the decision to collect this data is purely at the descretion of the project team. 

---

## **Media & Notes**

### **Notes**

* **Type:** Text
* **Description:** Field notes, anomalies, or comments

---

### **Photo**

* **Type:** Text (URL or file path)
* **Description:** Link to tree image

---

# **Coordinate System Standard**

* **Primary Storage:** WGS 84 (EPSG:4326) 
This is genrally the default for collected data from Arboreal and GPS units. 
* **Working Projection:** UTM Zone 11N (WGS 84)
* **Rule:** All spatial data must align with project CRS before analysis *## Mention what CRS stands for* 

---

# **Data Governance Rules**

* Tree_ID is the **authoritative key**
* CSV files are **non-authoritative (read-only for GIS geometry)**
* Master dataset stored as:

  * File Geodatabase (ArcGIS)
  * GeoPackage (QGIS backup)
* Edits must occur in GIS environment, not raw CSV *## Get clarity on this*

---

# **Versioning & Updates**

* Each update cycle must:

  * Preserve previous records
  * Log changes to Status field
  * Record verification date (future field recommended) *## Incorporate this into official mastersheet*

---

# **Summary**

This schema ensures:

* Data consistency across platforms
* Defensible spatial accuracy
* Scalable field workflows
* Long-term usability for campus operations, climate action planning, and climate analysis

---
