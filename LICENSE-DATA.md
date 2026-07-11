# Data Licensing Notes

Code in this repository is under MIT (see `LICENSE`). Tree inventory *data* is a separate question — worth deciding deliberately rather than defaulting.

**Considerations before publishing any actual tree location data publicly:**

- A common choice for open geospatial datasets is **CC-BY 4.0** (attribution required, otherwise unrestricted) or, for government/municipal data, whatever your organization's existing open-data policy specifies.
- Check whether your organization has privacy, security, or liability concerns about publishing exact tree coordinates (e.g., trees on private property, sensitive infrastructure proximity) before any real coordinate data goes into a public `data/` folder. If so, publish the schema and a sample/synthetic dataset instead, and keep production data private.
- This decision should be made explicitly, not left implicit — note it here once resolved.

**Current status:** no production tree location data is published in this repository. `docs/` and `protocols/` describe methodology only.
