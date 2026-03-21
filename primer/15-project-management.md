# Project Management

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/management/project-management/>

**Relevant Personas:** CIO, COO, CTO

---

## Overview

IT project management determines how technology initiatives are planned, executed, and delivered. Choosing the right methodology, governance structure, and delivery approach is critical because project failure remains one of the most persistent and costly problems in enterprise IT.

## Core Failure Drivers

IT projects continue to fail at high rates. The most common drivers include:

- **Unclear or shifting requirements** -- Scope that is poorly defined or changes without governance
- **Inadequate executive sponsorship** -- Leaders who approve but do not actively support
- **Poor estimation** -- Underestimating complexity, effort, and duration
- **Insufficient change management** -- Neglecting the human side of technology adoption
- **Technical debt and integration complexity** -- Underestimating the difficulty of working with existing systems
- **Talent and skill gaps** -- Teams lacking the expertise needed for the chosen approach

## Methodologies

### Waterfall

- **Sequential phase-gate** approach: Requirements --> Design --> Build --> Test --> Deploy
- Each phase must be completed and approved before the next begins
- **Best suited for:**
  - Stable, well-understood requirements
  - Regulatory environments requiring extensive documentation
  - Hardware-dependent projects with long lead times
- **Limitations:** Inflexible to change; problems discovered late are expensive to fix

### Agile

Core agile approaches:

#### Scrum

- Time-boxed iterations called **sprints** (typically 2 weeks)
- Defined roles: Product Owner, Scrum Master, Development Team
- Ceremonies: Sprint Planning, Daily Standup, Sprint Review, Retrospective
- Emphasis on delivering working software incrementally

#### Kanban

- Continuous flow model with **work-in-progress (WIP) limits**
- Visual board showing workflow stages
- Pull-based system: new work is pulled when capacity is available
- Well suited for operational and maintenance work

#### Scaled Agile Frameworks

- **SAFe (Scaled Agile Framework)** -- Most widely adopted framework for scaling agile across large organizations
- **LeSS (Large-Scale Scrum)** -- Extends Scrum principles to multiple teams with minimal additional structure
- **Spotify Model** -- Squad-based organizational model emphasizing autonomy and alignment

### Hybrid: Water-Scrum-Fall

- Combines elements of waterfall and agile
- Typically uses waterfall for planning and governance phases, agile for execution
- Common in organizations transitioning from waterfall or operating in regulated environments
- Pragmatic compromise when pure agile is not feasible

## PMO Types

Project Management Offices serve different functions depending on organizational maturity and needs:

| PMO Type | Role | Authority Level |
|----------|------|----------------|
| **Supportive** | Provides templates, tools, training, and best practices | Advisory; low control |
| **Controlling** | Requires conformance to frameworks, standards, and reporting | Moderate control |
| **Directive** | Directly manages projects and assigns project managers | High control |

## Portfolio Management

Managing the collection of projects and programs as a strategic portfolio:

- **Run / Grow / Transform** framework applied to project investment allocation
- Balances risk across the portfolio rather than evaluating projects in isolation
- Prioritization based on strategic alignment, resource constraints, and interdependencies
- Regular portfolio reviews to kill underperforming initiatives and reallocate resources

## DevOps and CI/CD

### DevOps

- Cultural and technical movement that unifies **software development (Dev) and IT operations (Ops)**
- Emphasizes automation, collaboration, continuous improvement, and shared responsibility
- Breaks down silos between teams that build software and teams that run it

### CI/CD (Continuous Integration / Continuous Delivery)

- **Continuous Integration** -- Developers frequently merge code changes into a shared repository; automated builds and tests run on every merge
- **Continuous Delivery** -- Code is always in a deployable state; releases can happen at any time with minimal manual intervention
- **Continuous Deployment** -- Every change that passes automated tests is automatically deployed to production
- Reduces risk by making changes smaller and more frequent rather than large and infrequent

## Case Studies

### Healthcare.gov Launch Failure

- The initial 2013 launch of the US federal health insurance marketplace was a high-profile failure
- Site crashed under load, enrollment was nearly impossible
- Root causes: inadequate testing, poor integration management, unrealistic timeline, fragmented vendor management
- Required emergency remediation effort to stabilize and restore public confidence
- Demonstrated the consequences of multiple project management failures compounding

### Spotify

- Pioneered the **Squad model**: autonomous, cross-functional teams aligned around features
- Squads grouped into **Tribes**; cross-cutting alignment through **Chapters** and **Guilds**
- Emphasized team autonomy with alignment through shared mission and principles
- Widely studied, though Spotify itself has noted the model continues to evolve

### ING Bank

- Adopted the Spotify model for its agile transformation
- Reorganized from traditional departments into squads and tribes
- Required significant cultural change alongside structural reorganization
- Demonstrated that agile principles can be applied in highly regulated financial services
