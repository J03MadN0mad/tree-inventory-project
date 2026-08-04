# GPS Best Practices Cheat Sheet
**Audience:** citizen-scientist volunteers using the Arboreal app on a smartphone during community tree measurement days. One-page quick reference -- pin this or print it for field days.

## 1. Before taking a point

- Turn on Airplane Mode, then re-enable GPS (forces a fast location lock)
- Ensure Wi-Fi is ON (helps Android/iOS assisted GPS)
- Wait 10–15 seconds after opening Arboreal for satellites to stabilize
- Check the accuracy reading -- must be ≤5 m (ideal)
- If accuracy is >10 m, wait, or step into clearer sky

## 2. While logging

- Hold the phone away from your body
- Keep the device vertical (the GNSS antenna is usually at the top)
- Stay still for 5 seconds before tapping "Save"
- Avoid logging near tall buildings, dense canopy, vehicles/metal objects, or hillsides facing away from sky visibility; this is where utilizing Garmin GNSS unit may prove most adventageous. 

## 3. Environmental adjustments

- Move into a canopy gap if possible
- Step 2–3 meters into better signal
- Place the phone on a non-metal surface for 10–15 seconds if accuracy fluctuates

## 4. After taking a point

- Verify the point position visually on the map
- If off by more than 3–5 meters, retake
- Document anything unusual (poor signal, canopy, obstructions) in the comment section

## 5. End of day

- Sync app data
- Confirm coordinates exist, photos attach correctly, and DBH, Species, Tag_ID, and Condition entries are complete and consistent

**Comment format example:**
Tag ID: 112. Surveyor: Joe. Species: Sequoia sempervirens. DBH: 34.5 in. Condition: Poor. Notes: Tree appears declining; very poor GPS signal.

**Consistency across teams is the most important factor.**

---

## 6. Using the Garmin GPSMAP 65s (dedicated GPS hardware track)

*Smartphone GNSS hasn't consistently met the project's accuracy target*, so a dedicated handheld unit -- a Garmin GPSMAP 65s -- is now part of the toolkit for points where smartphone accuracy isn't cutting it (dense canopy, narrow campus corridors between buildings, or any point a volunteer has had to retake more than once).

**What's different about it:** the 65s uses multi-band GNSS, pulling from multiple satellite systems (GPS, GLONASS, Galileo, QZSS, and others) across multiple frequency bands per system, rather than the single-band reception a phone uses. In practical terms this means faster lock-on and meaningfully better accuracy in exactly the conditions that give smartphones trouble -- dense tree cover and areas with buildings on multiple sides. Reviewers consistently report real-world accuracy in the range of a couple of meters under those tough conditions, better than typical smartphone GNSS performance in the same spots. It's worth noting Garmin itself is explicit that *these are recreational-grade devices, not survey-grade instruments* -- so treat it as a meaningful accuracy upgrade, not a guarantee of centimeter-level precision.

**Workflow additions when using the Garmin unit:**

- Record which device captured each point (see `Collection_Method` field in the data dictionary) -- this is what lets the GPS Accuracy Testing objective actually compare device performance later, rather than guessing
- Let the unit acquire a stable multi-band lock before marking a point (same principle as the smartphone wait time, just usually faster)
- Use it as the fallback device specifically for points a team has already had to retake once on a phone -- no need to default to it everywhere, since that defeats the point of testing where it actually adds value versus where the phone was already fine
- Log the Garmin's on-device accuracy reading into `GPS_Accuracy_m` the same way as the phone reading, so both device types feed the same downstream QA logic
