from pydantic import BaseModel, Field, ConfigDict

class Patient(BaseModel):
    age: int = Field(ge=0, le=110)
    gender: str
    sleep_quality_index: float
    brain_fog_level: float
    physical_pain_score: float
    stress_level: float
    fatigue_severity_scale_score: float
    pem_duration_hours: float
    hours_of_sleep_per_night: float
    work_status: str
    social_activity_level: str
    exercise_frequency: str
    meditation_or_mindfulness: str

    model_config = ConfigDict(extra="forbid")