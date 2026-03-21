# Hospitality Research Command

## Activation
When the user invokes /hospitality-research, run a focused research session tailored to the Hospitality/Hotel Industry using the configuration set in `research/active-research.md`.

## Context to Read
Before responding, read:
1. `research/active-research.md` — extract `target_company` and `emerging_technology` from the Research Configuration block
2. `student-workspace/project-brief.md` — for overall proposal context
3. `primer/` directory as needed for relevant frameworks

## Instructions

### Step 1 — Parse Research Configuration
Read the `research/active-research.md` file and extract:
- `target_company` — the hotel company being analyzed
- `emerging_technology` — the technology being proposed

If either value is still a placeholder (`[TARGET COMPANY NAME]` or `[EMERGING TECHNOLOGY]`), stop and ask the student to fill in those fields first.

### Step 2 — Generate Tailored Research Output
With the configured company and technology, produce research across three mandatory lenses:

#### Lens 1: FAAAM Competitive Threat Analysis
- Identify which FAAAM players (Meta, Apple, Amazon, Alphabet/Google, Microsoft) most directly threaten the target company's value chain
- Explain how the proposed emerging technology is a strategic response to these threats (or creates new exposure)
- Reference hospitality-specific FAAAM incursions (e.g., Google Hotel Search, Amazon Alexa for Hospitality, Apple Wallet room keys)
- Rate each FAAAM player's threat level: 🔴 High / 🟡 Medium / 🟢 Low — with justification

#### Lens 2: Gartner Hype Cycle Positioning
- Place the emerging technology on the Gartner Hype Cycle (cite the most recent relevant report)
- Assess the hospitality-specific adoption curve — is the hotel industry ahead of, aligned with, or behind the general market?
- Identify early adopter hotel companies and their reported outcomes
- Recommend the optimal adoption window: early mover advantage vs. wait-for-maturity vs. fast follower
- Flag any "Peak of Inflated Expectations" hype risks that judges might challenge

#### Lens 3: NASA Technology Readiness Level (TRL)
- Assign a TRL (1–9) to the emerging technology in the hospitality context
- Justify the TRL with evidence: vendor case studies, peer-reviewed research, industry pilots
- Assess pilot readiness: TRL 6+ = pilot-ready; TRL 4–5 = exploratory; TRL 1–3 = research only
- Identify the key unknowns that must be resolved before enterprise deployment

### Step 3 — Populate research/active-research.md
After generating research, update the relevant sections of `research/active-research.md` with your findings. Fill in:
- Section 1 (Target Company Profile) with publicly available company data
- Section 2 (FAAAM Analysis) with tailored threat assessment
- Section 3 (Gartner Hype Cycle) with positioning and timing rationale
- Section 4 (TRL Assessment) with TRL rating and justification
- Section 7 Research Log with today's date and findings summary

### Step 4 — Suggest Business Value Summary
After completing the research, prompt the student: "Would you like me to run `/business-summary` to create a plain-English version of these research findings for your non-technical teammates?" Do not generate it automatically — let the student decide to avoid duplicate summaries if they plan to run `/business-summary` separately.

## Output Format
Structure your response as:
1. **Research Configuration Confirmed** — state the company and technology you're researching
2. **FAAAM Threat Analysis** — formatted table + narrative (use the table structure from active-research.md)
3. **Gartner Hype Cycle Positioning** — current stage, timing rationale, hospitality adoption context
4. **NASA TRL Assessment** — TRL rating, justification, pilot readiness verdict
5. **Key Insights for Your Proposal** — 3-5 bullet points connecting research to the DT proposal
6. **Recommended Follow-up** — which personas to consult and what to ask them

## Hospitality Industry Knowledge Base
Ground all responses in hospitality-specific context:
- **Key Industry Players**: Marriott International, Hilton Worldwide, IHG, Hyatt, Accor, Wyndham, Choice Hotels, Best Western
- **Key Metrics**: RevPAR (Revenue Per Available Room), ADR (Average Daily Rate), Occupancy Rate, GOP (Gross Operating Profit), TRevPAR
- **Key Technology Systems**: PMS (Property Management System), CRS (Central Reservation System), RMS (Revenue Management System), CRM, POS
- **Industry Bodies**: AHLA (American Hotel & Lodging Association), STR Global, HFTP, Hospitality Technology
- **OTA Threat**: Booking.com, Expedia, Airbnb — and hotel brand loyalty programs as counter-strategy
- **Current Trends**: Direct booking push, personalization at scale, contactless operations, sustainability/ESG, labor automation

## Behavioral Guidelines
- Always ground findings in publicly available data — do not fabricate statistics
- When citing Gartner, acknowledge if the specific report is not available and work from general knowledge of the technology category
- Be explicit about confidence levels: "Based on public reporting..." vs. "Gartner's 2024 Hype Cycle specifically states..."
- Push students to verify key claims before their presentation — judges will probe sources
- Connect all research back to the specific business problem in the project brief

## Important
This command is specifically designed for the Hospitality/Hotel Industry. If the target company is not in hospitality, note the mismatch and ask the student to confirm they want hospitality-focused research.
