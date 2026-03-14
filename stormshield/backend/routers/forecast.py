"""
GET /api/forecast/current
"""
from __future__ import annotations

from fastapi import APIRouter
from backend.modules.prediction.model import PredictionResult
from backend.modules.cache import store as cache

router = APIRouter(prefix="/api/forecast", tags=["forecast"])


@router.get("/current", response_model=PredictionResult)
def get_current_forecast() -> PredictionResult:
    forecast: PredictionResult | None = cache.get("forecast")
    if forecast:
        return forecast
    # Fallback synthetic result
    from datetime import datetime, timezone, timedelta
    return PredictionResult(
        predicted_level_ft=3.85,
        estimated_crest_iso=datetime.now(timezone.utc) + timedelta(minutes=30),
        confidence_score=0.60,
        model_version="2.0-synthetic",
    )


@router.get("/weather")
def get_weather_proxy():
    """Proxy weather data through backend to avoid frontend 429 rate limits."""
    import httpx
    lat = 32.3668
    lon = -86.3000
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,weather_code&hourly=temperature_2m,precipitation_probability,precipitation&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America%2FChicago"
    
    try:
        resp = httpx.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
