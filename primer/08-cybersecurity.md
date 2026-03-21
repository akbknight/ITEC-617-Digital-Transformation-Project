# Cybersecurity Governance

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/risk-security/cybersecurity/>

**Relevant Personas:** CISO, Legal, CIO

---

## Overview

Cybersecurity governance establishes the policies, frameworks, and organizational structures that protect enterprise information assets. It spans technical controls, regulatory compliance, risk management, and incident response, requiring coordination across the entire C-suite.

## Key Frameworks

### NIST Cybersecurity Framework (CSF) 2.0

The most widely adopted cybersecurity framework in the US, organized around **6 core functions:**

1. **Govern** -- Establish and monitor cybersecurity risk management strategy, expectations, and policy (new in CSF 2.0)
2. **Identify** -- Understand the organization's assets, risks, and vulnerabilities
3. **Protect** -- Implement safeguards to ensure delivery of critical services
4. **Detect** -- Develop capabilities to identify cybersecurity events in a timely manner
5. **Respond** -- Take action when a cybersecurity incident is detected
6. **Recover** -- Restore capabilities and services impaired by a cybersecurity incident

### ISO 27001

- International standard for information security management systems (ISMS)
- Requires systematic evaluation of information security risks
- Provides a certifiable framework that demonstrates security maturity to partners and regulators

### CIS Controls v8.1

- Prioritized set of defensive actions organized by implementation group
- Practical, prescriptive guidance that maps to other frameworks
- Particularly useful for organizations beginning their security maturity journey

## Regulatory Landscape

| Regulation | Scope | Key Requirements |
|-----------|-------|-----------------|
| **SOX (Sarbanes-Oxley)** | Public companies (US) | IT controls for financial reporting integrity |
| **HIPAA** | Healthcare (US) | Protected health information safeguards |
| **GDPR** | EU data subjects | **72-hour breach notification** requirement, privacy by design |
| **PCI-DSS** | Payment card data | Technical and operational controls for cardholder data |

## Threat Landscape

The cybersecurity threat environment is continuously evolving, with attackers leveraging:

- Ransomware and extortion campaigns
- Supply chain attacks targeting trusted vendors and software
- Social engineering and phishing at scale
- Nation-state sponsored intrusions
- AI-enabled attack techniques

## Risk Treatment Strategies

Organizations have four options for addressing identified cybersecurity risks:

- **Mitigate** -- Implement controls to reduce risk to acceptable levels
- **Transfer** -- Shift risk to a third party (e.g., cyber insurance)
- **Accept** -- Acknowledge the risk and choose not to act (with documented rationale)
- **Avoid** -- Eliminate the activity that creates the risk

## Architectural Concepts

### Defense in Depth

- Multiple layers of security controls so that failure of one layer does not compromise the whole system
- Combines physical, technical, and administrative controls

### Zero Trust

- "Never trust, always verify" -- no implicit trust based on network location
- Requires continuous authentication and authorization for every access request
- Increasingly adopted as perimeter-based security proves insufficient

### SIEM (Security Information and Event Management)

- Centralized platform for collecting, correlating, and analyzing security events
- Enables real-time threat detection and forensic investigation
- Foundation for a security operations center (SOC)

## SEC Disclosure Rules

- Publicly traded companies must disclose **material cybersecurity incidents within 4 business days**
- Boards must describe their cybersecurity risk oversight
- Annual reporting on cybersecurity risk management processes and strategy
- Elevates cybersecurity from a technical issue to a board-level governance concern

## Case Studies

### SolarWinds Supply Chain Attack

- Attackers compromised the SolarWinds Orion software build process
- Malicious updates distributed to approximately 18,000 organizations including US government agencies
- Demonstrated the devastating potential of supply chain attacks
- Highlighted the need for software supply chain security and vendor risk management

### Colonial Pipeline Ransomware Attack

- Ransomware attack forced shutdown of the largest fuel pipeline in the United States
- Resulted in fuel shortages across the southeastern US
- Company paid approximately $4.4 million in ransom
- Exposed the vulnerability of critical infrastructure to cyber attacks
- Led to increased federal focus on critical infrastructure cybersecurity
