# Long-Term Memory: User & Projects

## User Overview
- Name: Timothy (Tim)
- Location: Sydney, Australia (Timezone: Australia/Sydney)
- Communication: Direct, concise, prefers quick action over explanations
- Critical requirements: Autonomous agent operation, daily backups, reliability

## GitHub Repository
- Repository URL: https://github.com/timba2000/Prince_Andrew.git
- Authentication: Existing SSH key configured for the workspace.
- Purpose: Daily backups and project synchronisation.

## Completed Project: ANZ Mortgage Refinancing Research
### Status
- Research to find the best Australian mortgage rates for refinancing initiated and completed.
- A 'steering view' summary of findings was presented to Tim on March 25th, 2026.

### Next Actions
- None. This project phase is complete.

## Active Project: Scuba Down Under - Dive Site Corroboration
### Status (as of latest update)
- All dive site data has been successfully migrated from `scubadownunder.csv` into a persistent SQLite database: `dive_sites.db`.
- This database now serves as the primary source of truth for all dive site information.
- The schema includes `validation_status` (for data integrity) and `article_status` (to track article completion).
- Initial validation was completed during the CSV parsing phase, flagging missing/suspicious values.
- Automation is designed for:
  - Google Maps cross-verification
  - Web directory searches to validate entries (name, region, coordinates, facilities, marine life, etc.)
  - Flagging probable errors/unverified entries
- The `dive_sites.db` has been exported to `sdu_export.csv` and committed to the GitHub repository.
- The final output for this phase will be a comprehensive CSV file containing the validated data for all dive sites, including validation information and sources.
- Article writing is now the priority, focusing on sites with no `article_status`.

### Next Actions
- Continue systematic cross-check for remaining sites by querying `dive_sites.db` for uncorroborated entries.
- Generate a comprehensive CSV output of all validated dive site data upon project completion.
- **Article Word Count:** Each `ScubaDownUnder` article should be between 750-1000 words.
- **Completed Articles:** Articles for American River Wharf, Ningaloo Reef, Exmouth Navy Jetty, Fish Rock Cave, and Montague Island have been drafted.


## Active Project: viz - Compass Bearing Corroboration
### Status
- Initiated task to accurately determine and update the `Compass_Bearing` for all dive sites in `dive_sites.db`.
- The `Compass_Bearing` is defined as the direction the dive site faces the open water.
- Current Completion Percentage: 86.83% (211 out of 243 sites).

### Next Actions
- Continue systematically determining and updating `Compass_Bearing` for remaining dive sites.
- Maintain a running tally of completion percentage.
- Once `Compass_Bearing` is complete for all sites, proceed with `Viz_Slug`, `Nearby_Runoff`, `Viz_Triggers`, and `Viz_Seasonal`.


## Completed Project: Whisper Skill Installation
### Status
- OpenAI Whisper skill identified, installed, and successfully used for audio transcription.
- Project is now complete.

## Preferences/Guidelines
- If restarted or reset, always reload project memory from this file and any memory logs
- If uncertain, ask Tim before taking public/external actions
- **Model Usage Policy:**
  - **OpenAI:** Exclusively for voice-related tasks (e.g., audio transcription).
  - **Gemini:** For all other tasks and general reasoning.

## Dive Site Review Guidelines
To make a dive site review on ScubaDownUnder truly valuable, you need to go beyond "the water was blue and I saw a turtle." A high-quality review helps a diver decide if the site fits their skill level, gear setup, and expectations. Here is a breakdown of what every comprehensive review should cover, based on the approved Muiron Island format:

### Standard SDU Dive Site Review Format:

**[Dive Site Name]: [Catchy Subtitle Describing Its Essence]**

[Introductory paragraph - sets the scene, highlights key aspects, defines target diver skill level, and location context. Approx 100-150 words]

**The Essentials: [Specific Focus e.g., A Glimpse Beneath the Waves / Navigating the Depths of History]**

For those planning an expedition to [Dive Site Name], here are the crucial details for a safe and exhilarating dive:

*   **Depth Range:** [Min-Max depth, notes on certification needed]
*   **Visibility:** [Typical range, influencing factors]
*   **Water Temperature:** [Typical range, wetsuit recommendations]
*   **Current/Conditions:** [Expected currents, surface conditions, specific hazards]
*   **Viz Implications:** [A comprehensive section covering what causes good visibility, factors leading to poor visibility, the site's facing direction, how swell direction and conditions impact visibility, and any other environmental elements (like rain, current, silt) that affect Viz.]

**Terrain & Navigation: [Specific Focus e.g., Exploring Unspoiled Coral Gardens / Exploring a Wreck Transformed]**

The underwater topography around [Dive Site Name] is characterised by [description of terrain: coral gardens, sandy channels, walls, wrecks, etc.]. Key navigational features and points of interest include:

*   [Specific feature 1: e.g., Pristine Reef Systems / Wreck Structure]
*   [Specific feature 2: e.g., Sandy Patches & Channels / Artificial Reef Formation]
*   [Specific feature 3: e.g., Drift Diving Opportunities / Sandy Surroundings]
*   [Specific feature 4: e.g., Boat Access Only / Entry/Exit points]

**Marine Life Highlights: [Specific Focus e.g., A Rich Tapestry of Biodiversity / A Thriving Ecosystem]**

[Dive Site Name] is a biodiversity hotspot, offering an extraordinary array of marine encounters, from the smallest reef inhabitants to some of the ocean's most magnificent creatures.

*   [Specific marine life 1: e.g., Manta Rays & Whale Sharks / Resident Fish]
*   [Specific marine life 2: e.g., Tropical Fish Extravaganza / Bottom Dwellers]
*   [Specific marine life 3: e.g., Reef Sharks / Pelagic Visitors]
*   [Specific marine life 4: e.g., Coral Trout & Groupers / Invertebrate Gardens]
*   [Specific marine life 5: e.g., Macro Wonders / Unique Sightings]

**Logistics & Facilities: Planning Your [Remote/Local] Adventure**

Diving [Dive Site Name] requires specific planning due to its [remote/local] nature:

*   **Accessibility:** [How to get there, boat/shore access, distances]
*   **Facilities:** [On-site facilities, dive operator services, gear rental]
*   **Best Time to Dive:** [Optimal seasons, tides, weather considerations]
*   **Conservation:** [Marine park status, rules, environmental considerations]

**Who Is It For?: An [Beginner/Intermediate/Advanced] Diver's Dream**

[Dive Site Name] is particularly suited for [skill level] divers. [Elaborate on required skills, experience, and what makes it ideal for this group. Approx 50-100 words]

**Pro-Tip: [Insightful closing remark/unique aspect]**

The "vibe" of [Dive Site Name] is one of [description of atmosphere, feeling, unique selling point]. [Elaborate further. Approx 50-100 words]

---

**75-word excerpt:** "[A concise summary of the dive site, highlighting key features, location, skill level, and main attractions. Must be exactly 75 words or very close.]"

---
This section will be updated as the project progresses. For more detail, consult project-specific memory logs if available.
