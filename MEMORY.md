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
- Save all article drafts to the GitHub repository at `https://github.com/timba2000/Prince_Andrew.git`.


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

## Article Guidelines

**1. ScubaDownUnder Dive Site Reviews:**
   - **Word Count:** 750-1000 words.
   - **Format:** All completed Scuba Down Under dive site articles will be saved as individual Markdown files in the `dive_site_articles/` directory within the repository. The filename will be `[site_name_slug].md` (e.g., `glenelg-dredge-wreck.md`).
     - **[Dive Site Name]: [Catchy Subtitle Describing Its Essence]** (This format will be used for the title within the Markdown file).
     - Introductory paragraph (approx 100-150 words)
     - **The Essentials:** Depth Range, Visibility (including best conditions such as wind/swell directions, seasonal variations, and other triggers derived from `Viz_Triggers` and `Viz_Seasonal` database columns), Water Temperature, Current/Conditions, Viz Implications.
     - **Terrain & Navigation:** Description of underwater topography and key features.
     - **Marine Life Highlights:** Array of marine encounters.
     - **Logistics & Facilities:** Accessibility, dive operator services, best time to dive, conservation.
     - **Who Is It For?:** Suitable skill level for divers.
     - **Pro-Tip:** Insightful closing remark.
     - **75-word excerpt:** Concise summary.

**2. General Scuba Diving Articles (e.g., Equipment Guides):**
   - **Word Count:** Flexible, as requested by user.
   - **Format:** Comprehensive, well-researched, including product reviews and comparisons where applicable. Structure will be determined by the topic but should include an introduction, detailed sections, and a conclusion.
   - **Content:** Information gathered from web searches, synthesized into a coherent guide.

**General Article Protocol:**
- All completed dive site review content will be saved as individual Markdown files in the `dive_site_articles/` directory and committed to the GitHub repository. The filename will be `[site_name_slug].md`.
- The `dive_sites.db` will continue to store the `article_full_text` for consistency, but the primary article storage will be the individual Markdown files.
- I will extract all existing articles from `dive_sites.db` and create individual markdown files for them in the `dive_site_articles/` directory.
- When reporting on article completion, I will include the percentage of sites that now have dive site articles.

---
This section will be updated as the project progresses. For more detail, consult project-specific memory logs if available.