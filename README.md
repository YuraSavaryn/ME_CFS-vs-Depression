# ME/CFS vs Depression Classificator

Веб-додаток розроблений для встановлення діагнозу в пацієнта
на основі даних, чи у пацієнта депресія, чи синдром
хронічної втоми, чи обидва діагнози зразу.  

### Як підняти сервер FastAPI ?

1. Скопіюйте репозиторій собі на комп'ютер

2. Встановіть усі необхідні бібліотеки з файлу requirements.txt 
у своє віртуальне середовище venv

3. Підключіть PostgreSQL до проекту через файл .env

4. Запустіть main.py з папки app

5. Сервер запустить на http://127.0.0.1:8000

### Як викликати /train/model ?

Після запуску сервера перейдіть на http://127.0.0.1:8000/docs

Потрапивши на swagger документцію, у секції /train 
ви можете викликати /model

### Як викликати /inference/predict ?

Після запуску сервера перейдіть на http://127.0.0.1:8000/docs

Потрапивши на swagger документцію, у секції /inference
ви можете викликати /predict

### Опис структури БД:

У базі даних є 4 таблиці:

1. data

Зберігає необроблені дані датасету стану пацієнтів та їх
діагнозів

2. clean_data

Зберігає оброблені дані датасету стану пацієнтів та їх
діагнозів

3. predictions

Зберігає усі передбачення, які робить модель і під час 
тренування і під час 

4. inference_inputs

Зберігає нові дані, які поступають на /inference/predict від
пацієнтів

### Приклад збережених передбачень:

Приклад даних пацієнта у JSON форматі для передбачення:
```json
{
  "age": 32,
  "gender": "Male",
  "sleep_quality_index": 8,
  "brain_fog_level": 8,
  "physical_pain_score": 3,
  "stress_level": 9,
  "fatigue_severity_scale_score": 10,
  "pem_duration_hours": 7,
  "hours_of_sleep_per_night": 7,
  "work_status": "Working",
  "social_activity_level": "Low",
  "exercise_frequency": "Rarely",
  "meditation_or_mindfulness": "No"
}
```

Результат передбачення програми:
```json
{
  "prediction": 2,
  "prediction_confidence": 0.6796985242653864,
  "probabilities": [
    0.3203014757346136,
    0,
    0.6796985242653864
  ]
}
```