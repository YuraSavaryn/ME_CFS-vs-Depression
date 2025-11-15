from datetime import datetime
import joblib
import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import Patient
from app.database import crud, database

router_inference = APIRouter(prefix="/inference", tags=["inference"])

model = joblib.load("models/pipeline_model.pkl")


@router_inference.post('/predict')
def predict(patient: Patient, db: Session = Depends(database.get_db)):
    patient_data = pd.DataFrame([patient.model_dump()])

    pred = model.predict(patient_data)

    probabilities = model.predict_proba(patient_data)
    probabilities = probabilities[0].tolist()
    confidence = max(probabilities)

    patient_data["timestamp"] = datetime.now()
    inference_prediction = pd.DataFrame({
        "prediction": pred,
        "actual": None,
        "source": "inference",
        "log_timestamp": datetime.now()
    })

    crud.save_inference_prediction(db, inference_prediction)
    crud.save_inference_data(db, patient_data)

    return {
        "prediction": int(pred[0]),
        "prediction_confidence": confidence,
        "probabilities": probabilities,
    }
