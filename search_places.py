import requests
from typing import List

def search_places(city: str) -> str:
    """
    Search for points of interest in a given city using OpenStreetMap Nominatim API.
    Returns a formatted string summary of the top results.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "addressdetails": 1,
        "extratags": 1,
        "limit": 10
    }
    headers = {"User-Agent": "demo_app/1.0 (your_email@example.com)"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    if not data:
        return f"No places found for {city}."
    results = []
    for place in data:
        name = place.get("display_name", "Unknown")
        place_type = place.get("type", "Unknown")
        results.append(f"- {name} (type: {place_type})")
    return f"Points of interest in {city} (top {len(results)}):\n" + "\n".join(results) 