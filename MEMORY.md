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

## High-Priority Project: ANZ Mortgage Refinancing Research
### Status
- Initiated research to find the best Australian mortgage rates for refinancing.
- Aim: Identify competitive interest rates and refinancing offers to renegotiate with ANZ.
- Mortgage Details (from images):
  - Fixed Rate Loan:
    - Current Balance: ~$657,164.03
    - Fixed Term Ends: 21st April 2026
    - Current Repayment: ~$3,101.44/month (fixed)
    - Expected New Repayment (without refinancing): ~$4,400/month (variable)
  - Variable Rate Loan:
    - Current Balance: ~$600,520.02
    - Current Interest Rate: 5.54% (variable)
    - Current Repayment: ~$2,015.00/month (variable)
- Focus: Exhaustive search, avoiding hidden fees, providing options for negotiation with ANZ.
  - Fixed Rate Loan will revert to the variable rate of 5.54% p.a. from the April 30th payment.

### Next Actions
- Conduct comprehensive web searches for current Australian mortgage rates and refinancing options.
- Analyse offers for competitive interest rates, fees, and favourable terms.
- Summarise findings to present to Tim.

## Active Project: Scuba Down Under - Dive Site Corroboration
### Status (as of latest update)
- All dive site data has been successfully migrated from `scubadownunder.csv` into a persistent SQLite database: `dive_sites.db`.
- This database now serves as the primary source of truth for all dive site information, including names, coordinates, descriptions, and corroboration status.
- Initial validation was completed during the CSV parsing phase, flagging missing/suspicious values.
- Automation is designed for:
  - Google Maps cross-verification
  - Web directory searches to validate entries (name, region, coordinates, facilities, marine life, etc.)
  - Flagging probable errors/unverified entries
- Corroboration progress will now be tracked directly within the `dive_sites.db` database.
- **Current Batch (in progress since March 6th, 2026):** SS Yongala Wreck, Muiron Island, Hat Head Bommie, Black Rock – Forster, HMAS Brisbane, Arno Bay Jetty, Aldinga Drop-off, American River Wharf, Ningaloo Reef, Exmouth Navy Jetty, Green Island – South West Rocks (AI corroborated), Latitude Rock (AI corroborated), Bluefish Point (AI corroborated), Mullaway Reef (AI corroborated), Woody Head Reef (AI corroborated), Wedding Cake Island (AI corroborated), Manta Bommie (AI corroborated), Bushrangers Bay (AI corroborated), Cod Hole (AI corroborated), Fish Rock Cave (AI corroborated), Magic Point (AI corroborated), The Gutter (restored from CSV).
- This activity has been ongoing for several days.
- The final output will be a comprehensive CSV file containing the corroborated data for all dive sites, including validation information and sources.

### Next Actions
- Continue systematic cross-check for remaining sites by querying `dive_sites.db` for uncorroborated entries.
- Generate a comprehensive CSV output of all corroborated dive site data upon project completion.
- **Article Word Count:** Each `ScubaDownUnder` article should be between 750-1000 words.


## Completed Project: viz - Compass Bearing Corroboration
### Status
- Successfully completed the task to accurately determine and update the `Compass_Bearing` for all 243 dive sites in `dive_sites.db`.
- The project is 100% complete.

### Next Actions
- Proceed with `Viz_Slug`, `Nearby_Runoff`, `Viz_Triggers`, and `Viz_Seasonal` for all dive sites.


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
