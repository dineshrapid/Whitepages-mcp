# whitepages_mcp.py
import asyncio
from playwright.async_api import async_playwright
from fastmcp import FastMCP, tool

app = FastMCP("whitepages-scraper")

@tool()
async def check_whitepages(person_name: str, location: str = "New York, NY"):
    """Search Whitepages for a person and return possible addresses."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled"
        ])
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.whitepages.com", wait_until="domcontentloaded", timeout=90000)
        await page.fill("#search-name", person_name)
        await page.fill("#search-location", location)
        await page.click("#wp-search")

        await page.wait_for_selector("ul.speedbump-list li", timeout=60000)

        people_info = []
        results = await page.query_selector_all("ul.speedbump-list li")

        for person in results:
            name_el = await person.query_selector("h2.name-wrap, div.name-wrap")
            name = await name_el.text_content() if name_el else None
            addresses = [
                (await addr.text_content()).strip()
                for addr in await person.query_selector_all("span[data-qa-selector^='current-and-historical-address']")
            ]
            if name:
                people_info.append({"name": name, "addresses": addresses})

        await browser.close()

        return {"query": person_name, "results": people_info or "not found"}

if __name__ == "__main__":
    app.run()
