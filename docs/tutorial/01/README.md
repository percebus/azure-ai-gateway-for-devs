# Module 1: Foundry & logging infrastructure

## Goal

![Architecture](../../../assets/drawio/architecture-01.drawio.svg)

## Summary

Create the foundational Azure resources: a resource group, monitoring infrastructure, and AI Foundry instances across two regions.

## Motivation

Every Azure AI solution starts with a resource group, monitoring and the AI service itself. Setting these up correctly from the start ensures consistent naming, centralized logging, and multi-region readiness.

## Use cases

- Centralized logging per-region for AI deployments
- Standardized resource naming conventions for team collaboration
- Region-aware infrastructure for high availability

## Skills learned

- Creating and tagging Azure Resource Groups
- Deploying Log Analytics Workspace (LAW) and Application Insights (appi)
- Creating Azure AI Foundry instances across multiple regions
- Connecting Foundry to Application Insights for telemetry

## Chapters

1. [Resource group](./rg.md)
1. [Logging infrastructure](./logs.md)
1. [Foundry](./foundry.md)

## Next

[Back to Modules](../README.md)
