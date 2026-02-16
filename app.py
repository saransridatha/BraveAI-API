import time
import logging
from playwright.async_api import Page

logger = logging.getLogger(__name__)

class BraveSearcher:
    """
    A class to scrape Brave Search AI results using an existing Playwright page.
    """
    def __init__(self, page: Page):
        """
        Initializes the BraveSearcher with an existing Playwright page.
        """
        self.page = page

    async def search(self, query: str) -> str:
        base_url = "https://search.brave.com"
        search_url = f"{base_url}/search?q={query}&source=llmSuggest&summary=1"
        start_time = time.time()
        
        try:
            await self.page.goto(search_url, timeout=100000)
            # Wait for the AI summary to appear
            await self.page.wait_for_selector('//div[contains(@class, "llm-output")]', timeout=30000)
            page_content = await self.page.locator('//div[contains(@class, "llm-output")]').inner_text()
        except Exception as e:
            logger.error(f"An error occurred during search: {e}")
            # In a real-world scenario, you might want to handle different exceptions differently.
            # For now, we'll return an error message.
            await self.page.screenshot(path="error_screenshot.png")
            return "Could not retrieve the search summary. A CAPTCHA might be required."

        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Execution time for query '{query}': {execution_time:.2f} seconds")
        return page_content

