import json
import pandas as pd
from textblob import TextBlob
from sklearn.preprocessing import LabelEncoder

with open("data/fb_simulated_posts.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

df["sentiment"] = df["message"].apply(
    lambda x: TextBlob(x).sentiment.polarity
)

df["engagement"] = df["likes"] + df["comments"] + df["shares"]

encoder = LabelEncoder()
df["online"] = encoder.fit_transform(df["online"])
df["country"] = encoder.fit_transform(df["country"])

X = df[["sentiment", "engagement", "online", "event_time", "country"]]
y = df["attendance"]

print("Preprocessing completed.")
