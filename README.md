# Event Attendance Predictor (ML Project)

## Detailed Description

This project presents a Machine Learning solution to predict event attendance based on social media activity. Traditional prediction methods rely only on historical data, but this system enhances prediction accuracy by incorporating simulated real-time social media signals such as post sentiment, likes, comments, and shares.

Due to restrictions in accessing Facebook Graph API data, a realistic synthetic dataset was generated to simulate social media engagement. The system uses Natural Language Processing (NLP) to extract sentiment and combines it with engagement metrics and event features to train a predictive model.

The trained model is deployed using Gradio, allowing users to input new event posts and receive predicted attendance in real time.

---

## Features

- Synthetic dataset generation (500–1500 samples)
- Sentiment analysis using TextBlob
- Feature engineering (engagement, time, event type)
- Machine Learning model (Gradient Boosting Regressor)
- Model evaluation using MAE and R² Score
- Interactive UI using Gradio for live predictions

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- TextBlob (NLP)
- Gradio (UI)
- JSON (data format)

---

## Project Structure

```
Event Attendance Predictor/
│
├── data/
│   └── fb_simulated_posts.json
│
├── src/
│   ├── simulate_data.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── app.py
│
├── model/
│   └── gb_model.pkl
│
└── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```
git clone <https://github.com/MuhammadAsad29/Event-Attendance-Predictor>
cd Event-Attendance-Predictor
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## How to Run the Project

### Step 1: Generate Dataset

```
python src/simulate_data.py
```

### Step 2: Train Model

```
python src/train.py
```

### Step 3: Evaluate Model

```
python src/evaluate.py
```

### Step 4: Run Gradio App

```
python src/app.py
```

---

## Model Performance

- MAE: ~140
- R² Score: ~0.90

---

## Example Input (Gradio)

- Event Post: AI Conference 2026 is coming!
- Likes: 600
- Comments: 200
- Shares: 150
- Mode: Offline
- Days Until Event: 5
- Country: Pakistan

---

## Limitations

- Facebook Graph API restricts access to public event data without app review.
- Real-time data was simulated to demonstrate the system pipeline.

---

## Future Improvements

- Integration with real social media APIs
- Use of larger real-world datasets
- Dashboard visualization
- Advanced NLP techniques

---

## Author

Muhammad Asad

---

## License

This project is for academic purposes.
