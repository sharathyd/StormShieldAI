"""
Frontend configuration — API base URL and refresh settings.
"""
import os

import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

def get_config(key: str, default: str) -> str:
    """Fetch from os.getenv."""
    return os.getenv(key, default)

BACKEND_URL: str = get_config("BACKEND_URL", "http://localhost:8000")
DEFAULT_REFRESH_SECONDS: int = int(get_config("DEFAULT_REFRESH_SECONDS", "60"))

REFRESH_OPTIONS = {
    "30 seconds": 30,
    "60 seconds": 60,
    "5 minutes": 300,
}
