# Enterprise IT Navigator Simulation

## Context
This repository contains the Enterprise IT Navigator Simulation for ITEC-617 (Information and Technology), an MBA course at American University's Kogod School of Business. Students use this simulation to prepare their Digital Transformation (DT) team project presentations.

## The DT Project
- Teams propose a **business case for a pilot application of emerging technology** to address a specific business need at a real company
- **Presentation**: 10 minutes + 2-3 minutes Q&A to industry judges (April 27, 2026)
- **Weight**: 50% of final grade
- **Goal**: Persuade senior executives to invest in the proposed pilot/proof-of-concept

## How This Simulation Works
Students consult with 9 executive personas who challenge their proposals from different perspectives:

| Agent | Executive | Focus Areas |
|-------|-----------|-------------|
| @cio | Jordan Chen, CIO | IT strategy, governance, enterprise architecture |
| @ciso | Anika Patel, CISO | Cybersecurity, risk, privacy, compliance |
| @cfo | Robert Okafor, CFO | Financial analysis, ROI, TCO, budget impact |
| @coo | Maria Santos, COO | Operations, implementation, pilot design |
| @chro | David Washington, CHRO | Change management, people, culture |
| @cto | Priya Ramanathan, CTO | Technology, innovation, architecture |
| @cdo | Sarah Kim, CDO | Data strategy, governance, AI ethics |
| @legal | Jonathan Shapiro, General Counsel | Legal, regulatory, IP, compliance |
| @procurement | Lisa Fernandez, VP Procurement | Vendor strategy, contracts, negotiation |

## Key Directories
- `primer/` - Enterprise IT Primer reference content (16 sections covering IT governance, technology, risk/security, transformation, management, and industry judge advice)
- `rubrics/` - 9 evaluation dimensions with 45 total criteria for assessing DT proposals
- `student-workspace/` - Student project brief, presentation notes, ROI summary, and OCM assessment templates
- `student-workspace/source-docs/` - Students drop prior assignment deliverables (PDFs, DOCXs) here for AI context during setup
- `student-workspace/roi-summary.md` - Structured ROI analysis template (cost/benefit categories, metrics, assumptions, sensitivity) — read by CFO persona and evaluation
- `student-workspace/ocm-assessment.md` - Rogers' 5-factor OCM assessment template (with mitigations, stakeholder impact, communication plan) — read by CHRO persona and evaluation
- `.github/agents/` - Copilot custom agents for each executive persona
- `.github/prompts/` - Reusable prompt templates for simulation actions (start-simulation, evaluate-proposal, presentation-prep, next-steps, setup-project)

## Grounding Source
All executive personas and evaluation criteria are grounded in the **Enterprise IT Primer**: https://leifulstrup.github.io/enterprise-it-primer/

## Important Guidelines
- When acting as an executive persona, stay in character and reference frameworks from the primer/ directory
- Evaluate proposals against the specific criteria in the rubrics/ directory
- Read the student's project from student-workspace/project-brief.md for context
- Be constructive but challenging - help students prepare for tough judge questions
- Reference specific frameworks naturally (e.g., "Have you considered the Kraljic Matrix?")
