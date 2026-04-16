# python AI smoke tester

The app is a simple "what tools do you have?" tester for the AI agent.

Is pre-configured w/ mslearn docs. But it should work w/ any MCP either directly or via APIM

## Pre-requisites

1. [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
1. Azure account
   1. Foundry
      1. Access to said foundry
      1. At least 1 LLM deployment model

## Setup

1. `$> uv venv`
1. Activate `.venv`
1. `$> uv sync --locked --all-extras`

### .env

1. Copy+paste `.env.example` to `.env`
1. Fill in the required environment variables.

### login to Azure

1. `$> az login`
1. Choose the appropiate subscription

## Run

`$> python src/my_agent`

Returns something like.-

![Screenshot](assets/img/console.png)

```
User: What tools are available to you?
Agent: I have access to a set of tools focused on Microsoft and Azure technologies documentation and coding examples:

1. microsoft_docs_search: Search official Microsoft/Azure documentation to find relevant content for a user's query.
2. microsoft_code_sample_search: Search for code snippets and examples in official Microsoft Learn documentation.
3. microsoft_docs_fetch: Fetch and convert a Microsoft Learn documentation webpage to markdown format for complete step-by-step procedures or tutorials.

These tools help me provide accurate, detailed, and up-to-date information and code examples related to Microsoft and Azure technologies.
```
