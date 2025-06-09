# backend/app/api/clone.py

import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.scraper import scrape_website
from app.services.llm import generate_clone
from app.utils.cleaner import clean_html_for_design_replication

router = APIRouter()
logger = logging.getLogger(__name__)

class CloneRequest(BaseModel):
    url: str

class CloneResponse(BaseModel):
    html: str

@router.post("/clone", response_model=CloneResponse)
async def clone_website(request: CloneRequest):
    """
    Accepts a website URL, scrapes it, and returns a cloned HTML.
    """
    logger.info(f"Received cloning request for URL: {request.url}")

    try:
        design_context = await scrape_website(request.url)
        logger.info("Website scraping completed.")
    except Exception as e:
        logger.error(f"Error scraping website: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error scraping website: {str(e)}")

    try:
        cloned_html = generate_clone(design_context)
        logger.info("LLM HTML generation completed.")
    except Exception as e:
        logger.error(f"Error generating clone HTML: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating clone HTML: {str(e)}")

    return CloneResponse(html=cloned_html)
