import pandas as pd
from sqlalchemy.orm import Session
from app.database.models import Data, CleanData, InferenceInputs


def get_data(db: Session):
    query = db.query(Data)

    return pd.read_sql(query.statement, db.bind)


def get_clean_data(db: Session):
    query = db.query(CleanData)

    return pd.read_sql(query.statement, db.bind)


def get_inference_data(db: Session):
    query = db.query(InferenceInputs)

    return pd.read_sql(query.statement, db.bind)


def save_predictions(db: Session, predictions):
    predictions.to_sql('predictions', db.bind, if_exists='append', index=False)


def save_inference_prediction(db: Session, prediction):
    prediction.to_sql('predictions', db.bind, if_exists='append', index=False)


def save_inference_data(db: Session, inference_data):
    inference_data.to_sql('inference_inputs', db.bind, if_exists='append', index=False)