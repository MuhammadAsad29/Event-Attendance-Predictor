import gradio as gr
import joblib
from textblob import TextBlob

model = joblib.load("model/rf_model.pkl")

def predict_attendance(message, likes, comments, shares, online, event_time, country):
    sentiment = TextBlob(message).sentiment.polarity
    engagement = likes + comments + shares

    online = 1 if online == "Online" else 0
    country = 0 if country == "Pakistan" else 1

    prediction = model.predict([[sentiment, engagement, online, event_time, country]])
    return int(prediction[0])

gr.Interface(
    fn=predict_attendance,
    inputs=[
        gr.Textbox(label="Event Post"),
        gr.Number(label="Likes"),
        gr.Number(label="Comments"),
        gr.Number(label="Shares"),
        gr.Radio(["Online", "Offline"], label="Mode"),
        gr.Number(label="Days Until Event"),
        gr.Radio(["Pakistan", "Other"], label="Country")
    ],
    outputs="number",
    title="Event Attendance Predictor"
).launch()
