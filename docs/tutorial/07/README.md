# Module 7: Content-Safety

## Use cases

Imagine the customer coming with the following requirements:

- We need a `gpt-4.1-mini-global-standard-stable` that has minimal blocking, for a dev team for a healthcare solution that uses terms like "Suicidal, blood, bodily fluids, etc".
- We need another `gpt-4.1-mini-global-standard-stable` that has very strict blocking, because they plan to expose that to their customers
- We need another one that has Hate:1, Sexual:5, Self-hate:2, Violence:3
- etc.

Unfortunately, GTP HardWare is finite. Every time we create a deployment model, we're chipping away from the allocated TPM quota for that family in that region.

Furthermore, in high availability scenarios, managing multiple LLM deployments with different content-safety settings can become complex and resource-intensive (even w/ IaC, i.e. `terraform`)

## Objective

To move content-safety checks from LLM deployments directly into to APIM

## Introduction

Remember when we added MS Foundry using the APIM wizard and it did everything for us?

Well, this time, we'll take it up a notch and manually add configuration.

## Chapters

1. [APIM to Foundryb RBAC permissions](./rbac.md)
1. [Foundry Guardrails & Blocklists](./foundry/guardrails.md)
1. [Cognitive Services @ Foundry](./foundry/cognitiveservices.md)
1. [Content-Safety @ APIM](./apim/content-safety.md)
1. [Test with python](./python.md)

## Next

[Back to Modules](../README.md)
