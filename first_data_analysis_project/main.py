from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd


app = FastAPI(
    title="Titanic Survival Prediction API",
    description="API for predicting survival on the Titanic Dataset",
    version="0.1.0",
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
model = joblib.load("ML_model/Logistic_regression.pkl")


class PassengerData(BaseModel):
    Pclass: int
    Sex_encoded: int
    Age: int
    Fare: float

    class Config:
        schema_extra = {
            "example": {"Pclass": 1, "Sex_encoded": 0, "Age": 25, "Fare": 50.0}
        }


class PredictionResponse(BaseModel):
    survival_pred: int
    survival_probability: float


@app.post("/predict", response_model=PredictionResponse)
async def predic_survival(passenger: PassengerData):
    try:
        df = pd.DataFrame([passenger.dict()])

        pred = model.predict(df)[0]
        proba = model.predict_proba(df)[0][1]

        return PredictionResponse(
            survival_pred=int(pred), survival_probability=float(proba)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    return {"message": "API is healthy"}
