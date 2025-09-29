from pydantic import BaseModel
from typing import List

class PredictRequest(BaseModel):
    symptoms: List[str]
    age: int | None = None
    sex: str | None = None

class PredictResponse(BaseModel):
    predictions: list[dict]  # [{condition, probability}]
    disclaimer: str

class NearbyRequest(BaseModel):
    lat: float
    lng: float
    query: str = "clinic"
