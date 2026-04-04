# SDU_skill.md - Scuba Down Under Article Writing Skill

This skill provides guidelines for consistently writing articles for Scuba Down Under dive sites and general scuba diving topics.

## Article Guidelines

**1. ScubaDownUnder Dive Site Reviews:**
   - **Identify Next Site:** Query the `dive_sites.db` to identify the next dive site that does not have an article (`article_status IS NULL OR article_status != 'completed'`).
   - **Word Count:** 750-1000 words.
   - **Format:** All completed Scuba Down Under dive site articles must be appended collectively into the `SDU_dive_sites.md` file. Individual `.md` files for completed dive site reviews will no longer be maintained.
     - Each article within `SDU_dive_sites.md` will follow this structure:
       - `# [Dive Site Name]: [Catchy Subtitle Describing Its Essence]`
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
- All completed dive site review content will be combined into `SDU_dive_sites.md` in the `dive_site_articles/` directory and committed to the GitHub repository.
- The `dive_sites.db` will continue to store the `article_full_text` for consistency, but the primary long-term article storage will be the `SDU_dive_sites.md` file.
- I will ensure all existing individual article Markdown files (currently in `sdu_articles/`) are combined into `SDU_dive_sites.md` and then deleted.
- When reporting on article completion, I will include the percentage of sites that now have dive site articles.
