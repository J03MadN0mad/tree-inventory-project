# **Tree Inventory GIS Schema Reference**

### Campus Tree Inventory & Climate Action Mapping Project

---

## **Document Status**

* **Version:** 2 — Updated 2026-07-20
* This is the **single authoritative schema reference** for this project's mastersheet. `Field_Guide_Reference.md` has been formally retired as of this version — it remains in the repo only as a deprecated historical record and should not be treated as a live source. See that file's deprecation notice for the full list of what it got wrong.
* **Change from v1:** Added `Duplicate_Candidate` to the `Status` domain below — an automated-QA-only flag (never field-confirmed, never auto-deletes) that `point_validation_toolkit.py` was already setting in practice. This formalizes what was previously only a recommendation in `data-dictionary.md`.

---

## **Overview**

This document defines the authoritative schema for the campus tree inventory GIS database.
It is designed to support:

* Field data collection (Arboreal / mobile GIS)
* Spatial analysis (ArcGIS Pro / QGIS)
* Web mapping (ArcGIS Online)
* Long-term asset management and climate reporting

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
* **Format Examples:**

  * `000123`
  * `2022-045`
* **Purpose:** Primary key for GIS joins and long-term tracking

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
* **Description:** Average canopy width.

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

### **Status**

* **Type:** Text (Domain Controlled)
* **Required:** Yes
* **Description:** Workflow tracking field for validation.

#### **Allowed Values & Definitions**

* **Existing**

  * Verified in field, matches ID and tag

* **Needs_Verification**

  * Default for legacy data not yet field-checked

* **Missing_Tag**

  * Tree present, tag missing/damaged/illegible

* **New_2025**

  * Newly added tree (post-2022 dataset)

* **Uncertain_Location**

  * GPS error >3–5m or unclear placement

* **Duplicate_Candidate**

  * Automated QA flagged this record as sharing a near-identical location, and/or a duplicate `Tag_ID`, with another record.
  * Set only by desk-based validation (`point_validation_toolkit.py`) — never a field-confirmed state.
  * Requires human review before any deletion. Never auto-removed.

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
  * 3–5m → Conditional
  * > 5m → Needs correction

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
* **Working Projection:** UTM Zone 11N (WGS 84)
* **Rule:** All spatial data must align with project CRS before analysis

---

# **Data Governance Rules**

* Tree_ID is the **authoritative key**
* CSV files are **non-authoritative (read-only for GIS geometry)**
* Master dataset stored as:

  * File Geodatabase (ArcGIS)
  * GeoPackage (QGIS backup)
* Edits must occur in GIS environment, not raw CSV

---

# **Versioning & Updates**

* Each update cycle must:

  * Preserve previous records
  * Log changes to Status field
  * Record verification date (future field recommended)

---

# **Summary**

This schema ensures:

* Data consistency across platforms
* Defensible spatial accuracy
* Scalable field workflows
* Long-term usability for campus operations and climate analysis

---
