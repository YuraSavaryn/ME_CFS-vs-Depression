import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from .database import Base, engine


class CleanData(Base):
    __tablename__ = "clean_data"

    data_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    sleep_quality_index = Column(Float)
    brain_fog_level = Column(Float)
    physical_pain_score = Column(Float)
    stress_level = Column(Float)
    fatigue_severity_scale_score = Column(Float)
    pem_duration_hours = Column(Float)
    hours_of_sleep_per_night = Column(Float)

    # --- One-Hot Encoded колонки (Boolean) ---
    # Якщо назва колонки в SQL містить великі літери або пробіли,
    # її ОБОВ'ЯЗКОВО треба взяти в лапки як перший аргумент Column.

    gender_Male = Column("gender_Male", Boolean)
    work_status_Partially_working = Column("work_status_Partially working", Boolean)
    work_status_Working = Column("work_status_Working", Boolean)
    social_activity_level_Low = Column("social_activity_level_Low", Boolean)
    social_activity_level_Medium = Column("social_activity_level_Medium", Boolean)
    social_activity_level_Very_high = Column("social_activity_level_Very high", Boolean)
    social_activity_level_Very_low = Column("social_activity_level_Very low", Boolean)
    exercise_frequency_Never = Column("exercise_frequency_Never", Boolean)
    exercise_frequency_Often = Column("exercise_frequency_Often", Boolean)
    exercise_frequency_Rarely = Column("exercise_frequency_Rarely", Boolean)
    exercise_frequency_Sometimes = Column("exercise_frequency_Sometimes", Boolean)
    meditation_or_mindfulness_Yes = Column("meditation_or_mindfulness_Yes", Boolean)

    diagnosis = Column(Integer)

    timestamp = Column('timestamp', DateTime(timezone=False))


class Data(Base):
    __tablename__ = "data"

    data_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String)
    sleep_quality_index = Column(Float)
    brain_fog_level = Column(Float)
    physical_pain_score = Column(Float)
    stress_level = Column(Float)
    depression_phq9_score = Column(Float)
    fatigue_severity_scale_score = Column(Float)
    pem_duration_hours = Column(Float)
    hours_of_sleep_per_night = Column(Float)
    pem_present = Column(Integer)
    work_status = Column(String)
    social_activity_level = Column(String)
    exercise_frequency = Column(String)
    meditation_or_mindfulness = Column(String)
    diagnosis = Column(String)
    timestamp = Column(DateTime)


class Predictions(Base):
    __tablename__ = "predictions"

    prediction_id = Column(Integer, primary_key=True, autoincrement=True)
    prediction = Column(Integer)
    actual = Column(Integer)
    source = Column(String)
    log_timestamp = Column(DateTime, default=datetime.datetime.now())


class InferenceInputs(Base):
    __tablename__ = 'inference_inputs'

    inference_input_id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    gender = Column(String)
    sleep_quality_index = Column(Float)
    brain_fog_level = Column(Float)
    physical_pain_score = Column(Float)
    stress_level = Column(Float)
    fatigue_severity_scale_score = Column(Float)
    pem_duration_hours = Column(Float)
    hours_of_sleep_per_night = Column(Float)
    work_status = Column(String)
    social_activity_level = Column(String)
    exercise_frequency = Column(String)
    meditation_or_mindfulness = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.now())
