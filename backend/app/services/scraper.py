# backend/app/services/scraper.py

import logging
import requests
import time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

async def scrape_website(url: str, use_browser: bool = False) -> dict:
    """
    Scrapes the given URL and returns design context, using HTTP or headless browser.
    """
    if use_browser:
        try:
            logger.info(f"Using browser-based scraping for URL: {url}")
            return await scrape_with_playwright(url)
        except Exception as e:
            logger.warning(f"Browser scraping failed: {e}, falling back to HTTP scraping.")
    return scrape_with_http(url)

def scrape_with_http(url: str) -> dict:
    """
    HTTP scraping using requests + BeautifulSoup.
    Includes retries and exponential backoff.
    """
    logger.info(f"Starting HTTP scraping for URL: {url}")

    for attempt in range(3):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            raw_html = soup.prettify()
            logger.info("HTTP scraping completed successfully.")
            return {"html": raw_html}
        except RequestException as e:
            logger.warning(f"HTTP scraping attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)

    raise Exception(f"HTTP scraping failed after 3 attempts for URL: {url}")

async def scrape_with_playwright(url: str) -> dict:
    """
    Browser-based scraping using Playwright.
    """
    logger.info(f"Starting Playwright scraping for URL: {url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle", timeout=15000)
            raw_html = await page.content()
            logger.info("Playwright scraping completed successfully.")
            return {"html": raw_html}
        except PlaywrightTimeoutError as e:
            logger.error(f"Playwright timeout: {e}")
            raise Exception(f"Playwright scraping timed out for URL: {url}")
        finally:
            await browser.close()
