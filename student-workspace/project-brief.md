# DT Project Brief (Judge-Ready Draft)

## Team Information
- **Team Name**: ITEC 617 DT Team (AT&T Upstream Advisory)
- **Team Members**: Yousef Auer, Robert Brown, Akshay Kumar, Mohammad Zalmai Siddiqi
- **Date**: March 26, 2026

## Target Company
- **Company Name**: AT&T Inc.
- **Industry**: Telecommunications
- **Business Unit/Division**: Enterprise and Government Solutions (pre-sales, solution engineering, and bid strategy)
- **Company Size**: Large enterprise telecom provider (Fortune-scale operations)

## Business Problem
AT&T currently competes in many deals after enterprise buyers have already defined RFP requirements. At that stage, vendors are often constrained by requirements that may be misaligned, incomplete, or biased toward legacy assumptions. This creates three issues: lower-quality pipeline, resource-heavy pursuit of low-fit opportunities, and weaker influence over technical decision framing.

The opportunity is to move upstream before formal procurement begins. If AT&T can help customers define problem statements, architecture options, and objective evaluation criteria earlier, it can improve solution fit, reduce avoidable bid effort, and increase probability of winning the right opportunities.

## Proposed Technology Solution
AT&T will pilot an **AI-Driven RFP Advisory and Pre-Procurement Optimization Platform** called **Shape Your Solution**.

The platform is a pre-procurement advisory layer that:
1. Ingests client environment data (network performance, architecture patterns, application usage, and location footprint) with explicit client permission.
2. Runs diagnostic analytics to identify likely root-cause constraints and inefficiency hotspots.
3. Simulates future-state scenarios (for example SD-WAN topology alternatives, edge placement, capacity reallocation).
4. Produces structured outputs that clients can use to draft higher-quality, outcome-based RFP requirements and scoring criteria.

This platform does not replace procurement tools. It improves the quality of inputs that enter procurement.

## Primary Benefit Type
- [ ] Cost Reduction
- [x] Revenue Growth
- [ ] Risk Mitigation
- [ ] Customer Experience
- [ ] Operational Efficiency
- [ ] Competitive Advantage

Secondary benefits: operational efficiency and competitive differentiation.

## Governance and Neutrality Model (Critical Design Feature)
To address legal and procurement concerns, the pilot will enforce a strict **Advisor-Bidder Separation Protocol**:
1. **Clean-team structure**: advisory team and bidding team are organizationally separated.
2. **Access separation**: role-based access controls prevent bid teams from viewing restricted advisory artifacts.
3. **Disclosure requirement**: clients receive written disclosure that AT&T may bid later.
4. **Neutrality standard**: recommendations must be outcome-based, not vendor-specific.
5. **Independent review gate**: legal/procurement sign-off required before outputs are used in formal sourcing.
6. **Audit trail**: immutable logs of data access, recommendation changes, and approval actions.

## Proposed Timeline
- **Pilot Duration**: 12 weeks (plus 4-week setup)
- **Pilot Scope**: One enterprise segment, 25-30 opportunities, matched control group using current process

### Key Milestones
1. **Weeks 1-4 (Setup)**: governance approval, data contracts, architecture baseline, and model validation on historical cases
2. **Weeks 5-8 (Live Pilot Phase 1)**: limited advisory use cases with mandatory human approval and quality scoring
3. **Week 9 (Midpoint Gate)**: stop/go review against KPI thresholds and risk controls
4. **Weeks 10-12 (Pilot Phase 2)**: expanded usage within same segment with continued control-group comparison
5. **Week 13 (Decision Gate)**: executive review for scale, redesign, or shutdown

## Pilot Success Metrics and Kill Criteria
### Primary KPIs
1. Opportunity qualification lift vs control group
2. Win-rate lift vs control group
3. Reduction in low-fit bid effort (hours per non-strategic opportunity)
4. Cycle-time improvement from discovery to bid/no-bid decision

### Guardrail KPIs
1. Neutrality compliance score (no vendor-specific requirement bias)
2. Legal/compliance exception rate
3. Recommendation rework rate after human review
4. Client trust score from advisory sessions

### Kill Criteria
Pilot pauses if any of the following occur for two consecutive reporting periods:
1. Compliance exceptions exceed threshold
2. Neutrality violations are confirmed
3. Recommendation quality falls below agreed acceptance threshold
4. No measurable improvement against control group by midpoint gate

## Initial Financial Estimate (Draft for CFO Review)
- **Estimated Pilot Cost**: $1.8M-$2.6M (build, integration, legal/compliance, enablement, and pilot operations)
- **Expected ROI (3-year range)**: 25%-55% (base case subject to finalized assumptions)
- **Expected Payback Range**: 18-30 months (base/downside range)
- **Funding Source**: Mostly OpEx in pilot year, with selective CapEx treatment for reusable internal assets

## Financial Assumptions to Validate Before Final Submission
1. Advisory-to-core attach rate assumptions by segment
2. Incremental win-rate improvement attributable to advisory motion
3. Cannibalization impact (if advisory drives lower-value solution designs)
4. Fully loaded talent and governance costs
5. Adoption rate and utilization assumptions for field teams

## Key Risks
1. **Conflict-of-interest risk**: perception that AT&T shapes RFPs to favor its own strengths
2. **Legal and procurement challenge risk**: buyer governance objections, bid protest exposure
3. **Data and privacy risk**: sensitive client environment data handling across jurisdictions
4. **Model credibility risk**: poor diagnostics or weak explainability reduces trust
5. **Operating model risk**: field teams fail to adopt consultative approach due to incentive misalignment
6. **Financial risk**: advisory revenue gains do not offset costs or cannibalization

## Risk Mitigation Plan (Executive Summary)
1. Advisor-bidder separation with independent compliance checks
2. Client disclosures, consent controls, and data minimization policy
3. Human-in-the-loop approval for all external recommendations
4. Stage-gated funding with midpoint stop/go decision
5. Comp and KPI alignment for consultative behavior in pilot segment

## Stakeholders
- **CIO / Enterprise Architecture**: architecture fit, integration burden, and governance discipline
- **CISO**: data classification, tenant isolation, model abuse controls, and incident readiness
- **CFO**: unit economics, TCO, cash flow timing, and downside sensitivity
- **COO / Sales Operations**: throughput, staffing, and process reliability
- **CHRO**: role redesign, capability uplift, and manager adoption behavior
- **Legal and Procurement**: neutrality, disclosure, conflict management, and contract safeguards
- **Enterprise Sales and Solution Engineering**: usability and impact on win strategy

## Additional Notes
### Why this can be strategic for AT&T
This proposal changes AT&T's position in the value chain from late-stage responder to early-stage decision partner. The value is not only faster response. The strategic value is shaping better-defined opportunities while maintaining procurement integrity.

### What must be true for scale approval
1. Pilot outperforms control group on qualified pipeline and win outcomes
2. Neutrality and compliance guardrails remain intact
3. Unit economics are positive under downside scenario
4. Sales and advisory teams demonstrate sustainable adoption
