# backend/app/services/llm.py

import logging
import os
from dotenv import load_dotenv
import google.generativeai as genai

logger = logging.getLogger(__name__)
load_dotenv()

# Load Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise Exception("Gemini API key is not set. Please set GEMINI_API_KEY environment variable.")

# Initialize Gemini client
genai.configure(api_key=GEMINI_API_KEY)

def generate_clone(design_context: dict) -> str:
    """
    Uses Gemini 2.5 Pro to generate cloned HTML from design context.
    """
    try:
        logger.info("Starting Gemini HTML generation.")
        raw_html = design_context.get("html", "<html><body><h1>Clone failed</h1></body></html>")

        # Construct the prompt for Gemini
         
        prompt = (
            "You are a web developer assistant. "
            "Given the following HTML content from a real website, "
            "generate an HTML page that replicates its design as closely as possible. "
            "Preserve structure, layout, and styles as much as possible, but do not include any ads, "
            "analytics, or unnecessary scripts. Only output the raw HTML code without any explanations, disclaimers, or markdown code fences."
            f"HTML Content:\n\n{raw_html}"
        )



        # Call Gemini
        model = genai.GenerativeModel("gemini-2.5-pro-preview-06-05")
        response = model.generate_content(prompt)

        generated_html = response.text
        logger.info("Gemini HTML generation completed successfully.")
        return generated_html

    except Exception as e:
        logger.error(f"Gemini HTML generation failed: {e}")
        raise Exception(f"Failed to generate clone HTML: {e}")
