# Open Source Software

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/technology/open-source-software/>

**Relevant Personas:** CTO, CIO, Legal

---

## Overview

Open source software has become foundational to enterprise IT. Understanding the licensing models, business strategies, and governance considerations is essential for any organization that consumes, contributes to, or builds upon open source technology.

## License Families

### Copyleft Licenses

- Require that derivative works be distributed under the same license terms
- **GPL (GNU General Public License)** is the most prominent example
- Creates obligations that can affect how organizations distribute their own software
- Requires careful compliance management, especially for embedded or distributed software

### Permissive Licenses

- Allow broad freedom to use, modify, and redistribute with minimal restrictions
- Examples: **MIT, Apache 2.0, BSD**
- Generally preferred by enterprises for their flexibility and reduced compliance burden
- Allow proprietary use of the licensed code

## 5 Open Source Business Models

| Model | Description | Example |
|-------|-------------|---------|
| **Support and Services** | Free software; revenue from enterprise support, training, consulting | Red Hat |
| **Open Core** | Core product is open source; proprietary premium features | GitLab |
| **Managed Cloud** | Operate the open source software as a hosted service | Various cloud providers |
| **Dual Licensing** | Offer both open source and commercial licenses | MySQL (Oracle) |
| **Foundation-backed** | Community-governed with corporate sponsors funding development | Linux Foundation, Apache Foundation |

## Enterprise Open Source Landscape

- **Linux** powers **90%+ of public cloud workloads**, making it the de facto server operating system
- **Kubernetes** has become the standard for container orchestration
- **Python** dominates the AI/ML ecosystem, with most major frameworks being open source
- Open source databases (PostgreSQL, MySQL), web servers (Nginx, Apache), and developer tools are ubiquitous

## Decision Framework Dimensions

When evaluating open source adoption, consider:

- **Community health** -- Activity level, contributor diversity, governance structure
- **License compatibility** -- Implications for your own software distribution
- **Support availability** -- Commercial support options and community responsiveness
- **Security posture** -- Vulnerability disclosure process, patch cadence
- **Long-term viability** -- Funding model, corporate backing, bus factor

## Notable Developments

### Red Hat / IBM Acquisition

- IBM acquired Red Hat for **$34 billion**, the largest open source acquisition in history
- Validated the enterprise value of open source business models
- Demonstrated that open source companies can build substantial, sustainable revenue

### Cloud Provider Controversy

- Major cloud providers offer managed versions of open source projects as services
- Original maintainers often see limited benefit from this commercial use
- Led to the creation of restrictive licenses (SSPL, BSL) designed to prevent cloud providers from offering competing services
- Sparked ongoing debate about the sustainability of open source business models in the cloud era

## Critical Risks

- **GPL compliance** -- Organizations must track open source components through a **Software Bill of Materials (SBOM)** to ensure license obligations are met
- **Community health** -- Projects with declining contributor engagement may become security risks or development dead ends
- **"Free" does not equal zero cost** -- Enterprise deployment requires investment in integration, support, security patching, training, and internal expertise
