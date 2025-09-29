import httpx

async def search_nearby(lat: float, lng: float, query: str = "clinic"):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": f"{query}", "format": "json", "limit": 10}
    async with httpx.AsyncClient(headers={"User-Agent": "MediQuick/1.0"}) as client:
        r = await client.get(url, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        # Nominatim is global search; you can filter by distance client-side if needed
        return [
            {"name": d.get("display_name"), "lat": float(d["lat"]), "lng": float(d["lon"])}
            for d in data
        ]
