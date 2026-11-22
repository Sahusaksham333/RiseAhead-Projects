"""FastAPI Weather Forecast Microservice (Open-Meteo Zero-Key API)"""
from fastapi import FastAPI
import urllib.request, json

app = FastAPI(title="Weather Forecast API")

@app.get("/weather")
def get_weather(lat: float = 22.7196, lon: float = 75.8577):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    with urllib.request.urlopen(url, timeout=5) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return {"latitude": lat, "longitude": lon, "current_weather": data.get("current_weather", {})}
