# Module 7: Content-Safety

## Goal

![Architecture](../../../assets/drawio/architecture-final.drawio.svg)

## Summary

Decouple content-safety enforcement from LLM model deployments and move it into APIM policies. Create distinct safety profiles (relaxed vs strict) as Products, so multiple teams can share the same model deployments with different content moderation rules.

## Use cases

Imagine the customer coming with the following requirements:

- We need a `gpt-4.1-mini-global-standard-stable` that has minimal blocking, for a dev team for a healthcare solution that uses terms like "Suicidal, blood, bodily fluids, etc".
- We need another `gpt-4.1-mini-global-standard-stable` that has very strict blocking, because they plan to expose that to their customers
- We need another one that has Hate:1, Sexual:5, Self-hate:2, Violence:3
- etc.

Unfortunately, GPT HardWare is finite. Every time we create a deployment model, we're chipping away from the allocated TPM quota for that family in that region.

Furthermore, in high availability scenarios, managing multiple LLM deployments with different content-safety settings can become complex and resource-intensive (even w/ IaC, i.e. `terraform`)

## Objective

To move content-safety checks from LLM deployments directly into APIM

## Introduction

Remember when we added MS Foundry using the APIM wizard and it did everything for us?

Well, this time, we'll take it up a notch and manually add configuration.

## Skills learned

- Assigning "Cognitive Services User" RBAC roles via `az` CLI
- Creating Foundry Guardrail policies and custom Blocklists (exact match + regex)
- Locating Cognitive Services endpoints in the Foundry portal
- Creating APIM backends for Cognitive Services with Managed Identity
- Configuring `llm-content-safety` policy with `EightSeverityLevels` thresholds
- Building content-safety Policy Fragments (relaxed vs strict profiles)
- Attaching content-safety fragments to Products for per-subscription enforcement
- Testing blocklists: positive tests, negative input tests, and output-tricking tests

## Chapters

1. [APIM to Foundry RBAC permissions](./rbac.md)
1. Foundry
   1. [Foundry Guardrails & Blocklists](./foundry/guardrails.md)
   1. [Cognitive Services @ Foundry](./foundry/cognitiveservices.md)
1. APIM
   1. [CognitiveServices Load Balancer](./apim/load_balance.md)
   1. [Test blocklist in API](./apim/blocklists.md)
   1. [Products w/ different Content-Safety profiles](./apim/products.md)
1. [Test with python](./python.md)

## Next

[Back to Modules](../README.md)
