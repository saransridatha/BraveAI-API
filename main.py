import os
import logging
import asyncio
from fastapi import FastAPI
from playwright.async_api import async_playwright
from app import BraveSearcher

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Use a dictionary to store the browser instance, to be managed by startup/shutdown events.
browser_context = {}

@app.on_event("startup")
async def startup_event():
    """
    On startup, launch the browser and store it in the app state.
    """
    logger.info("Starting up and launching browser...")
    headless_mode = os.environ.get("HEADLESS_MODE", "true").lower() == "true"
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless_mode)
    browser_context["playwright"] = playwright
    browser_context["browser"] = browser
    logger.info("Browser launched successfully.")

@app.on_event("shutdown")
async def shutdown_event():
    """
    On shutdown, close the browser.
    """
    logger.info("Shutting down and closing browser...")
    if "browser" in browser_context:
        await browser_context["browser"].close()
    if "playwright" in browser_context:
        await browser_context["playwright"].stop()
    logger.info("Browser closed successfully.")

@app.get("/search")
async def search(q: str):
    """
    Search endpoint that uses the shared browser instance.
    """
    if "browser" not in browser_context:
        logger.error("Browser not available.")
        return {"error": "Browser is not initialized."}

    page = None
    try:
        # Create a new page for each request for isolation.
        page = await browser_context["browser"].new_page(
            bypass_csp=True,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        )
        searcher = BraveSearcher(page)
        result = await searcher.search(q)
        return {"query": q, "result": result}
    except Exception as e:
        logger.error(f"An error occurred during search: {e}")
        return {"error": "An internal error occurred."}
    finally:
        if page:
            await page.close()
