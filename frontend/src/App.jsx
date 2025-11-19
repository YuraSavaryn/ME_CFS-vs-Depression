import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [formData, setFormData] = useState({
    age: 0,
    gender: 'Male',
    sleep_quality_index: 0.0,
    brain_fog_level: 0.0,
    physical_pain_score: 0.0,
    stress_level: 0.0,
    fatigue_severity_scale_score: 0.0,
    pem_duration_hours: 0.0,
    hours_of_sleep_per_night: 0.0,
    work_status: 'Working',
    social_activity_level: 'Low',
    exercise_frequency: 'Rarely',
    meditation_or_mindfulness: 'No'
  });

  // 2. Стан для результату (діагнозу) та помилок
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // 3. Обробник для оновлення полів вводу
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // 4. Обробник для відправки форми
  const handleSubmit = async (e) => {
    e.preventDefault(); // Запобігаємо перезавантаженню сторінки
    
    setLoading(true);
    setResult(null);
    setError(null);

    const dataToSend = {
      ...formData, // Копіюємо рядкові значення (gender, work_status тощо)
      // Перезаписуємо числові поля, конвертуючи їх
      age: parseInt(formData.age, 10),
      sleep_quality_index: parseFloat(formData.sleep_quality_index),
      brain_fog_level: parseFloat(formData.brain_fog_level),
      physical_pain_score: parseFloat(formData.physical_pain_score),
      stress_level: parseFloat(formData.stress_level),
      fatigue_severity_scale_score: parseFloat(formData.fatigue_severity_scale_score),
      pem_duration_hours: parseFloat(formData.pem_duration_hours),
      hours_of_sleep_per_night: parseFloat(formData.hours_of_sleep_per_night),
    };

    // URL FastAPI ендпоїнту
    const API_URL = 'http://127.0.0.1:8000/inference/predict'; 

    try {
      // 5. Відправляємо POST-запит з даними з нашого стану
      const response = await axios.post(API_URL, dataToSend);
      
      // Отримуємо відповідь і зберігаємо її у стан
      setResult(response.data); // Припускаємо, що FastAPI повертає JSON

    } catch (err) {
      if (err.response && err.response.status === 422) {
         setError('Помилка валідації. Перевірте, чи всі поля заповнені коректно.');
      } else {
         setError('Сталася помилка. Перевірте консоль або URL ендпоїнту.');
      }
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="App">
      <header className="App-header">
        <h1>ME/CFS vs Depression Classificator</h1>
        <h2>Діагностика пацієнта</h2>
        
        
        <form onSubmit={handleSubmit} className="patient-form">
          <div className="form-group">
            <label htmlFor="age">Вік:</label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="gender">Стать:</label>
            <select id="gender" name="gender" value={formData.gender} onChange={handleChange}>
              <option value="Male">Чоловік</option>
              <option value="Female">Жінка</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="sleep_quality_index">Якість сну:</label>
            <input
              type="number"
              id="sleep_quality_index"
              name="sleep_quality_index"
              value={formData.sleep_quality_index}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="brain_fog_level">Рівень когнітивної затуманеності:</label>
            <input
              type="number"
              id="brain_fog_level"
              name="brain_fog_level"
              value={formData.brain_fog_level}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="physical_pain_score">Рівень фізичного болю:</label>
            <input
              type="number"
              id="physical_pain_score"
              name="physical_pain_score"
              value={formData.physical_pain_score}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="stress_level">Рівень стресу:</label>
            <input
              type="number"
              id="stress_level"
              name="stress_level"
              value={formData.stress_level}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="fatigue_severity_scale_score">Оцінка за шкалою вираженості втоми:</label>
            <input
              type="number"
              id="fatigue_severity_scale_score"
              name="fatigue_severity_scale_score"
              value={formData.fatigue_severity_scale_score}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="pem_duration_hours">Тривалість pem в годинах:</label>
            <input
              type="number"
              id="pem_duration_hours"
              name="pem_duration_hours"
              value={formData.pem_duration_hours}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="hours_of_sleep_per_night">Середня кількість годин сну:</label>
            <input
              type="number"
              id="hours_of_sleep_per_night"
              name="hours_of_sleep_per_night"
              value={formData.hours_of_sleep_per_night}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="work_status">Робоча зайнятість:</label>
            <select id="work_status" name="work_status" value={formData.work_status} onChange={handleChange}>
              <option value="Not working">Ледарюю</option>
              <option value="Partially working">Працюю на пів ставки</option>
              <option value="Working">Працюю</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="social_activity_level">Рівень соціальної активності:</label>
            <select id="social_activity_level" name="social_activity_level" value={formData.social_activity_level} onChange={handleChange}>
              <option value="Very low">Я інтроверт</option>
              <option value="Low">Низький</option>
              <option value="Medium">Достатній</option>
              <option value="High">Високий</option>
              <option value="Very high">Я екстраверт</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="exercise_frequency">Фізична активність:</label>
            <select id="exercise_frequency" name="exercise_frequency" value={formData.exercise_frequency} onChange={handleChange}>
              <option value="Never">Ніколи</option>
              <option value="Rarely">Рідко</option>
              <option value="Sometimes">Інколи</option>
              <option value="Often">Часто</option>
              <option value="Daily">Щоденно</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="meditation_or_mindfulness">Практика медитації:</label>
            <select id="meditation_or_mindfulness" name="meditation_or_mindfulness" value={formData.meditation_or_mindfulness} onChange={handleChange}>
              <option value="Yes">Так</option>
              <option value="No">Ні</option>
            </select>
          </div>
          
          <button type="submit" disabled={loading}>
            {loading ? 'Аналізуємо...' : 'Визначити діагноз'}
          </button>
        </form>

        
        {/* 7. ВІДОБРАЖЕННЯ РЕЗУЛЬТАТУ (ОНОВЛЕНО) */}
        
        {error && <div className="error-message">{error}</div>}

        {result && (
          <div className="result-container">
            <h3>Результат діагностики:</h3>
            
            <p className="diagnosis-prediction">
              {result.prediction}
            </p>
            
            <p className="diagnosis-confidence">
              Впевненість: {Math.round(result.prediction_confidence * 100)}%
            </p>

            {/* За бажанням, можна вивести всі ймовірності */}
            {/* <details>
              <summary>Показати всі ймовірності</summary>
              <pre>{JSON.stringify(result.probabilities, null, 2)}</pre>
            </details> */}
          </div>
        )}

      </header>
    </div>
    </>
  )
}

export default App
