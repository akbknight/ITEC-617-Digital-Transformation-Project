# Technology Validation Command

## Activation
When the user invokes /tech-validate, run a structured technology validation assessment for the emerging technology proposed in the DT project.

## Context to Read
Before responding, read:
1. `student-workspace/project-brief.md` — extract the proposed technology and target company
2. `research/active-research.md` — for current Gartner/TRL research already completed
3. `primer/11-emerging-technology.md` — for technology evaluation frameworks
4. `rubrics/05-technology-fit.md` — for the rubric criteria judges will use

## Instructions

### Step 1 — Identify the Technology Under Validation
Read the project brief. If no technology is specified, ask the student: "What emerging technology would you like me to validate?"

### Step 2 — Run the Four-Part Validation Framework

#### Part 1: Technology Maturity Validation
- **Gartner Hype Cycle**: Current stage and time-to-mainstream estimate
- **NASA TRL**: Rating (1–9) with justification and pilot-readiness verdict
- **Vendor Landscape**: How many credible enterprise vendors offer this? Name 3–5.
- **Reference Customers**: Are there publicly known enterprise deployments (ideally in hospitality)?
- **Maturity Verdict**: Ready for enterprise pilot / Emerging but viable / Too early / Hype risk

#### Part 2: Business Fit Validation
- Does the technology directly address the stated business problem in the project brief?
- Is the ROI case credible given the technology's current capabilities?
- Are the claimed benefits (cost reduction, revenue uplift, efficiency gains) achievable at TRL [X]?
- What is the gap between vendor marketing claims and independently verified outcomes?
- **Business Fit Verdict**: Strong fit / Partial fit / Weak fit — with explanation

#### Part 3: Organizational Readiness Validation
- Does the target company have the data infrastructure to support this technology?
- What is the estimated implementation complexity (Low / Medium / High)?
- What organizational capabilities must exist or be developed?
- Are there known integration challenges with typical hospitality technology stacks (PMS, CRS, RMS)?
- **Readiness Verdict**: Ready / Needs preparation / Significant gaps

#### Part 4: Risk Profile Validation
- **Technology Risk**: What are the top 3 failure modes for this technology in production?
- **Vendor Risk**: What happens if the lead vendor fails or is acquired?
- **Data Risk**: What data dependencies could derail the pilot?
- **Competitive Risk**: Could FAAAM players undercut this capability before the pilot ends?
- **Risk Verdict**: Low / Medium / High — with most critical risk identified

### Step 3 — Score the Technology
Produce a validation scorecard:

| Dimension | Score (1–5) | Key Finding |
|-----------|------------|------------|
| Technology Maturity | [1–5] | [One sentence] |
| Business Fit | [1–5] | [One sentence] |
| Organizational Readiness | [1–5] | [One sentence] |
| Risk Profile | [1–5] | [One sentence] |
| **Overall Validation Score** | **[avg]** | **[Proceed / Proceed with caution / Reconsider]** |

### Step 4 — Provide Decision Recommendation
Based on the scorecard, recommend one of:
- ✅ **Proceed**: Technology is mature, fits the business problem, and risk is manageable
- ⚠️ **Proceed with Caution**: Strong fit but address [specific concern] before committing
- 🔄 **Consider Alternative**: This technology has significant gaps — consider [alternative technology] instead
- ❌ **Reconsider**: Technology is too immature or risky for a corporate pilot proposal

### Step 5 — Identify Judge Challenges
Based on the validation findings, predict the 3 most likely judge challenges:
1. [Challenge 1 — e.g., "Your TRL 4 rating means this is still experimental — why pilot now?"]
2. [Challenge 2 — e.g., "The top 3 vendors are all startups — what's your contingency if one fails?"]
3. [Challenge 3 — e.g., "Competitor X already deployed this — how are you differentiated?"]

For each challenge, suggest a strong response the team can prepare.

### Step 6 — Suggest Business Value Summary
After completing the validation, prompt the student: "Would you like me to run `/business-summary` to create a plain-English version of this validation for your non-technical teammates?" Do not generate the summary automatically — let the student decide.

## Output Format
Structure your response as:
1. **Technology Under Validation** — confirm what you're assessing
2. **Part 1: Maturity** — Gartner stage, TRL, vendor landscape, maturity verdict
3. **Part 2: Business Fit** — direct tie to business problem, ROI credibility, fit verdict
4. **Part 3: Organizational Readiness** — data needs, complexity, readiness verdict
5. **Part 4: Risk Profile** — top risks, risk verdict
6. **Validation Scorecard** — table with scores and overall recommendation
7. **Anticipated Judge Challenges** — 3 challenges + suggested responses

## Connection to Rubric
This validation directly maps to:
- `rubrics/05-technology-fit.md` — Technology Solution Assessment
- `rubrics/02-innovation-readiness.md` — Innovation Readiness Assessment
- `rubrics/01-business-case.md` — Business Case Strength (feasibility dimension)

After validation, recommend the student run `/evaluate` to see the impact on their overall rubric scores.

## Behavioral Guidelines
- Be honest about technology limitations — judges will probe weaknesses, and a team that acknowledges them proactively looks more credible than one that oversells
- Distinguish clearly between "the technology works in a lab" and "the technology works at enterprise scale in a hospitality context"
- If the technology is strong, say so clearly — students sometimes undersell good choices
- Reference primer/11-emerging-technology.md frameworks naturally
- Keep the response structured and scannable — this is a decision-support tool
