# python AI smoke tester

## Pre-requisites

1. `uv`

## Setup

1. `$> uv venv`
1. Activate `.venv`
1. `$> uv sync --locked --all-extras`

### .env

1. Copy+paste `.env.example` to `.env`
2. Fill in the required environment variables.

## Run

`$> python src/my_agent`

Returns something like.-

![Screenshot](assets/img/console.png)

```
User: What tools are available to you?
Agent: I have access to the following tools within the Microsoft functions namespace:

1. microsoft_docs_search: This tool allows me to search official Microsoft/Azure documentation to find relevant and trustworthy content for a user's query.

2. microsoft_code_sample_search: This tool helps me search for code snippets and examples in official Microsoft Learn documentation, which is useful for providing practical implementations and coding examples for Microsoft/Azure products and services.

3. microsoft_docs_fetch: This tool enables me to fetch and convert a complete Microsoft Learn documentation webpage to markdown format, providing detailed and full content from Microsoft documentation.
```
