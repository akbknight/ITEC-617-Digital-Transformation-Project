# Data Governance

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/risk-security/data-governance/>

**Relevant Personas:** CDO, CISO, CIO

---

## Overview

Data governance defines the policies, roles, and processes that ensure data is managed as a strategic enterprise asset. It encompasses data quality, master data management, business intelligence, ethics, and regulatory compliance.

## Key Roles

| Role | Responsibility |
|------|---------------|
| **Data Owner** | Business executive accountable for a data domain; makes policy decisions about access and use |
| **Data Steward** | Day-to-day responsibility for data quality and standards within a domain |
| **Data Custodian** | Technical responsibility for data storage, security, and infrastructure |
| **Data Consumer** | Business users who access and use data for decision-making |
| **CDO (Chief Data Officer)** | Executive accountable for the overall data governance program and strategy |

## 6 Data Quality Dimensions

Effective data governance requires measuring and managing quality across six dimensions:

1. **Accuracy** -- Data correctly represents the real-world entities or events it describes
2. **Completeness** -- All required data elements are present and populated
3. **Timeliness** -- Data is available when needed and reflects the current state
4. **Consistency** -- Data values are uniform across systems and do not contradict each other
5. **Validity** -- Data conforms to defined formats, ranges, and business rules
6. **Uniqueness** -- Each real-world entity is represented only once (no unwanted duplicates)

## Master Data Management (MDM)

### 4 MDM Implementation Styles

1. **Registry** -- Each system maintains its own data; MDM provides a cross-reference index
2. **Consolidation** -- Data is copied from source systems into a central hub for reporting
3. **Coexistence** -- MDM hub and source systems synchronize data bidirectionally
4. **Transaction (Centralized)** -- MDM hub is the single authoritative source; all systems read from it

### Golden Records

- The single, authoritative version of a master data entity (customer, product, vendor)
- Created by matching, merging, and surviving the best data from multiple sources
- Essential for accurate analytics, reporting, and customer experience

## Business Intelligence Architecture

BI systems are typically organized in layers:

- **Data Sources** -- Operational systems, external feeds, files
- **Data Integration** -- ETL/ELT processes that extract, transform, and load data
- **Data Storage** -- Data warehouses, data lakes, lakehouses
- **Analytics and Reporting** -- Dashboards, ad-hoc queries, advanced analytics
- **Consumption** -- Self-service BI, embedded analytics, data products

### Leading BI Platforms

- Microsoft Power BI, Tableau, Qlik, Looker (Google), and others
- Market is consolidating around platforms that combine visualization, governance, and AI/ML capabilities

## Data-Driven Culture

Building a data-driven organization requires more than tools and technology:

- **Executive sponsorship** for data initiatives
- **Data literacy** programs across the organization
- **Self-service capabilities** that empower business users
- **Metrics and KPIs** tied to business outcomes, not just data quality scores
- **Incentive alignment** so that teams are rewarded for data-informed decision-making

## Data Ethics

Responsible data use requires attention to:

- **Consent** -- Ensuring individuals understand and agree to how their data is used
- **Purpose limitation** -- Using data only for the purposes for which it was collected
- **Data minimization** -- Collecting only the data that is necessary
- **Bias auditing** -- Regularly evaluating datasets and algorithms for unfair bias, especially in AI/ML applications

## Regulatory Landscape

| Regulation | Key Data Governance Requirements |
|-----------|--------------------------------|
| **GDPR** | Data protection by design, right to erasure, consent management, data protection officer |
| **CCPA / CPRA** | Consumer data rights, opt-out of data sale, privacy impact assessments |
| **HIPAA** | Protected health information controls, access audit trails |
| **SOX** | Data integrity controls for financial reporting, audit requirements |

## Data Lifecycle

Data governance must address the full lifecycle:

1. **Creation / Collection** -- Standards for how data enters the organization
2. **Storage** -- Policies for where and how data is stored securely
3. **Usage** -- Access controls, acceptable use policies
4. **Sharing** -- Rules for internal and external data sharing
5. **Archival** -- Retention policies aligned with regulatory and business requirements
6. **Destruction** -- Secure disposal when data is no longer needed or required
