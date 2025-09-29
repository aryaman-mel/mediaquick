from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictRequest, PredictResponse, NearbyRequest
from app.model import predict_conditions
from app.maps import search_nearby

app = FastAPI(title="MediQuick", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

DISCLAIMER = ("This is not a medical diagnosis. If symptoms persist, "
              "seek professional medical advice or emergency services.")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    preds = predict_conditions(req.symptoms)
    return {"predictions": preds, "disclaimer": DISCLAIMER}

@app.post("/nearby")
async def nearby(req: NearbyRequest):
    results = await search_nearby(req.lat, req.lng, req.query)
    return {"results": results}
