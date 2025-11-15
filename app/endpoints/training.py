from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import crud, database
from app.services.pipeline import inference_pipeline

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score

from datetime import datetime
import pandas as pd
import joblib

router_training = APIRouter(prefix="/train", tags=["train ml model"])


@router_training.post('/model')
def train_model(db: Session = Depends(database.get_db)):
    #import data
    dataset = crud.get_clean_data(db)

    dataset.columns = [str(col) for col in dataset.columns]

    y = dataset['diagnosis']
    X = dataset.drop(columns=['diagnosis', 'data_id', 'timestamp'])

    #split data to train and input parts
    X_train, X_input, y_train, y_input = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)

    #train model
    model = RandomForestClassifier(max_depth=90, min_samples_leaf=5, min_samples_split=4, n_estimators=311,
                                   max_features=None, random_state=42)
    model.fit(X_train, y_train)

    pred = model.predict(X_input)
    score_rfc = f1_score(y_input, pred, average='weighted')

    print(f"Score RFC: {score_rfc}")

    #save model to folder
    joblib.dump(model, 'models/train_model.pkl')

    #add predictions to train data in table predictions
    prediction_data = pd.DataFrame({
        'prediction': pred,
        'actual': y_input
    })
    prediction_data['source'] = 'train'
    prediction_data['log_timestamp'] = datetime.now()

    crud.save_predictions(db, prediction_data)

    return {"score": score_rfc}


@router_training.post('/pipeline_model')
def train_model(db: Session = Depends(database.get_db)):
    #import data
    dataset = crud.get_data(db)
    y = dataset['diagnosis']
    X = dataset.drop(columns=['diagnosis', 'depression_phq9_score', 'pem_present', 'timestamp'])

    y = LabelEncoder().fit_transform(y)

    #split data to train and input parts
    X_train, X_input, y_train, y_input = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)

    #train model
    inference_pipeline.fit(X_train, y_train)

    pred = inference_pipeline.predict(X_input)
    score_rfc = f1_score(y_input, pred, average='weighted')

    print(f"Score RFC: {score_rfc}")

    #save model to folder
    joblib.dump(inference_pipeline, 'models/pipeline_model.pkl')

    #add predictions to train data in table predictions

    return {"score": score_rfc}