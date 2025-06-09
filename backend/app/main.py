# backend/app/main.py
from dotenv import load_dotenv
import os
load_dotenv()

import sys
import asyncio

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.clone import router as clone_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more verbose output
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Website Cloner API",
    description="API for cloning websites using LLMs",
    version="1.0.0"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(clone_router, prefix="/api")

@app.get("/")
async def root():
    logger.info("Root endpoint accessed.")
    return {"message": "Website Cloner Backend is running!"}
