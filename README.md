
# Whitepages MCP Server

Scrape Whitepages using Playwright, exposed as an MCP tool for workflow automation (via Smithery or n8n).

## Tools
- `check_whitepages(name: str, location: str = "New York, NY")`

## Usage
1. Deploy this repo to Smithery (`https://smithery.ai`).
2. Connect the MCP server in your workflow engine (n8n, LangChain, or custom).
3. Use the `check_whitepages` tool in your workflow.

## Local Run
```bash
pip install -r requirements.txt
playwright install chromium
python whitepages_mcp.py
