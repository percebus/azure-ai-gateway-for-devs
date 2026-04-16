# Module 3: Azure API Management (APIM)

## Summary

Put APIM in front of Foundry so all AI traffic flows through a managed gateway instead of hitting Foundry directly.

## Motivation

Exposing AI services through a gateway enables centralized authentication, policy enforcement, and observability. Managed identity eliminates the need to distribute Foundry API keys.

## Use cases

- Centralized API access for all AI consumers
- Managed identity authentication.
- Subscription-based access tracking per consumer
- Token consumption policies (`llm-token-limit`) at the API level

## Skills learned

- Creating an APIM instance (Basic v2 tier)
- Importing Foundry APIs using the APIM wizard
- Configuring System Managed Identity and RBAC ("Azure AI User")
- Understanding `set-backend-service` and `llm-token-limit` policies
- Testing APIs directly from the APIM portal
- Reading response headers (`x-powered-by`, rate limit headers)

## Chapters

1. [APIM](./apim/apim.md)
1. [Foundry via APIM](./apim/foundry.md)
1. [Python Smoke tester](./python.md)

## Goal

![Architecture](../../../assets/drawio/architecture-03.drawio.svg)

## Next

[Back to Modules](../README.md)
