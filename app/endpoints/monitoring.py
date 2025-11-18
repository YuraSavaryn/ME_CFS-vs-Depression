from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import crud, database

from evidently.report import Report
from evidently.pipeline.column_mapping import ColumnMapping
from evidently.metric_preset import (
    DataDriftPreset,
    DataQualityPreset,
    TargetDriftPreset
)

numerical_features = [
    'age',
    'sleep_quality_index',
    'brain_fog_level',
    'physical_pain_score',
    'stress_level',
    'fatigue_severity_scale_score',
    'pem_duration_hours',
    'hours_of_sleep_per_night'
]

categorical_features = [
    'gender',
    'work_status',
    'social_activity_level',
    'exercise_frequency',
    'meditation_or_mindfulness'
]

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.get("", response_class=HTMLResponse)
def monitoring(db: Session = Depends(database.get_db)):
    data = crud.get_data(db)
    inference_data = crud.get_inference_data(db)

    data = data.drop(columns=["data_id", "depression_phq9_score",
                              "pem_present", "_sa_instance_state"], errors="ignore")
    inference_data = inference_data.drop(columns=["inference_input_id", "_sa_instance_state"], errors="ignore")

    column_mapping = ColumnMapping()
    column_mapping.target = 'diagnosis'
    column_mapping.numerical_features = numerical_features
    column_mapping.categorical_features = categorical_features

    dashboard = Report(metrics=[
        DataQualityPreset(),
        DataDriftPreset(),
        TargetDriftPreset(),
    ])

    dashboard.run(
        reference_data=data,
        current_data=inference_data,
        column_mapping=column_mapping
    )

    html_content = dashboard.get_html()

    return HTMLResponse(content=html_content, status_code=200)