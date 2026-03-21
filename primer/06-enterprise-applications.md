# Enterprise Applications (ERP, CRM, SCM)

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/technology/enterprise-applications/>

**Relevant Personas:** CIO, COO, CTO

---

## Overview

Enterprise applications form the operational backbone of modern organizations. These large-scale systems manage core business processes and represent some of the most significant and consequential IT investments an organization will make.

## Core Enterprise Systems

### ERP (Enterprise Resource Planning)

- Integrates core business processes: finance, HR, procurement, manufacturing, supply chain
- Provides a single source of truth across the organization
- Implementations are complex, expensive, and high-risk

### CRM (Customer Relationship Management)

- Manages customer interactions, sales pipelines, and service operations
- **Salesforce holds approximately 23% market share**, making it the dominant platform
- Increasingly incorporates AI-driven insights and automation

### SCM (Supply Chain Management)

- Coordinates planning, sourcing, manufacturing, and logistics
- Critical for visibility across multi-tier supply chains
- Gained renewed attention after global supply chain disruptions

## Architecture Strategies

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| **Best-of-breed** | Select the top product for each functional area | Best functionality but complex integration |
| **Suite** | Single vendor provides all modules | Simpler integration but potential compromises in specific areas |
| **Hybrid** | Mix of suite for core functions, best-of-breed for differentiating areas | Balanced approach but requires careful governance |

## Integration Challenges

Enterprise applications rarely exist in isolation. Integration approaches include:

- **Point-to-point** -- Direct connections between systems; simple for a few integrations but creates unmanageable complexity at scale
- **APIs (Application Programming Interfaces)** -- Standardized interfaces for system communication; the modern standard
- **Middleware / ESB (Enterprise Service Bus)** -- Centralized integration layer that mediates between systems
- **iPaaS (Integration Platform as a Service)** -- Cloud-based integration platforms; gaining adoption for hybrid and multi-cloud environments

## Implementation Failure Drivers

Enterprise application implementations have notoriously high failure rates. Common drivers include:

- Underestimating organizational change management requirements
- Excessive customization that undermines the value of standard processes
- Poor data migration planning and execution
- Inadequate executive sponsorship and governance
- Unrealistic timelines and budgets

## Case Studies

### Hershey's ERP Failure (1999)

- Attempted simultaneous implementation of SAP ERP, CRM, and supply chain systems
- Compressed timeline to meet a holiday season deadline
- Result: inability to process $100M+ in orders during peak season

### Lidl SAP Implementation

- Invested approximately **500 million EUR** in a SAP implementation
- Ultimately abandoned the project after years of effort
- Highlighted the risks of forcing standard ERP processes onto a highly customized business model

## Modern Trends

- **Cloud ERP** -- Major vendors are pushing customers to cloud-hosted versions; SAP has announced a **2027 deadline** for customers to migrate from on-premises to cloud
- **Composable ERP** -- Modular approach where organizations assemble ERP capabilities from multiple cloud services rather than deploying a monolithic suite
- **Implementation services cost 3-7x the license fees** -- The software cost is often the smallest part of the total investment; consulting, customization, data migration, training, and change management dominate the budget
