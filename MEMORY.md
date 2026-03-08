# Long-Term Memory: User & Projects

## User Overview
- Name: Timothy (Tim)
- Location: Sydney, Australia (Timezone: Australia/Sydney)
- Communication: Direct, concise, prefers quick action over explanations
- Critical requirements: Autonomous agent operation, daily backups, reliability

## Active Project: Scuba Down Under
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

---
This section will be updated as the project progresses. For more detail, consult project-specific memory logs if available.