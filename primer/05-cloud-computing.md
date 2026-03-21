# Cloud Computing

**Source:** <https://leifulstrup.github.io/enterprise-it-primer/technology/cloud-computing/>

**Relevant Personas:** CTO, CIO, CISO, CFO

---

## Overview

Cloud computing has fundamentally reshaped how organizations provision, consume, and pay for technology resources. Understanding the service models, deployment options, migration strategies, and economic implications is essential for any technology investment decision.

## Service Models

| Model | What You Manage | What the Provider Manages |
|-------|----------------|--------------------------|
| **IaaS (Infrastructure as a Service)** | OS, middleware, applications, data | Servers, storage, networking, virtualization |
| **PaaS (Platform as a Service)** | Applications and data | Everything below the application layer |
| **SaaS (Software as a Service)** | Configuration and data | The entire stack including the application |

## Deployment Models

- **Public Cloud** -- Shared infrastructure operated by a cloud provider; highest scalability, lowest upfront cost
- **Private Cloud** -- Dedicated infrastructure for a single organization; greater control and security, higher cost
- **Hybrid Cloud** -- Combination of public and private; allows workload placement based on requirements
- **Multi-Cloud** -- Using multiple public cloud providers; reduces vendor lock-in but increases operational complexity

## 6 Rs Migration Framework

A structured approach to deciding what to do with each application during cloud migration:

1. **Rehost** ("Lift and Shift") -- Move as-is to cloud infrastructure
2. **Replatform** ("Lift and Reshape") -- Make minor optimizations for cloud without changing core architecture
3. **Repurchase** -- Replace with a SaaS equivalent
4. **Refactor** -- Re-architect the application to be cloud-native
5. **Retire** -- Decommission applications no longer needed
6. **Retain** -- Keep on-premises (not everything should move to the cloud)

## Shared Responsibility Model

- The cloud provider and the customer share security and operational responsibilities
- The division varies by service model: IaaS customers manage more; SaaS customers manage less
- A frequent source of security incidents is the assumption that the provider handles responsibilities that actually belong to the customer

## Cloud Economics

- **CapEx to OpEx shift** -- Cloud replaces large upfront hardware purchases with pay-as-you-go operating expenses
- **Pay-as-you-go pricing** -- Costs scale with consumption, enabling elasticity but requiring active cost management
- **FinOps** -- The emerging discipline of cloud financial management; brings financial accountability to cloud spending through cross-functional collaboration between finance, technology, and business teams

## Major Cloud Providers: Market Share

| Provider | Approximate Market Share |
|----------|------------------------|
| **AWS (Amazon Web Services)** | ~31% |
| **Microsoft Azure** | ~25% |
| **Google Cloud Platform (GCP)** | ~11% |

## Common Pitfalls

- **Cost overruns** -- Without active management, cloud costs can exceed on-premises equivalents; unused resources, oversized instances, and lack of reserved capacity planning are common culprits
- **Vendor lock-in** -- Deep adoption of proprietary services makes migration between providers expensive and complex
- **Lift-and-shift without optimization** -- Moving applications to the cloud without redesigning them misses the benefits of cloud-native architecture
- **Assuming the provider handles all security** -- Misunderstanding the shared responsibility model leads to security gaps, especially around identity management, data encryption, and network configuration
