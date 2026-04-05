import json
import random

events = [
    "AI Conference", "Tech Meetup", "Music Festival",
    "Startup Pitch", "Webinar on ML", "Coding Bootcamp"
]

countries = ["Pakistan", "USA", "UK", "India"]
online_modes = ["Online", "Offline"]

data = []

for _ in range(5000):   # increase data size
    likes = random.randint(20, 800)
    comments = random.randint(5, 300)
    shares = random.randint(2, 200)

    sentiment = random.uniform(-0.3, 0.8)
    online = random.choice(online_modes)
    event_time = random.randint(1, 30)

    engagement = likes + comments + shares

    # LOGICAL attendance formula (THIS IS THE KEY)
    attendance = (
        engagement * 2
        + (sentiment * 500)
        + (300 if online == "Offline" else 150)
        + max(0, (30 - event_time)) * 20
        + random.randint(-100, 100)
    )

    attendance = max(50, int(attendance))

    data.append({
        "message": f"{random.choice(events)} happening soon!",
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "online": online,
        "country": random.choice(countries),
        "event_time": event_time,
        "attendance": attendance
    })

with open("data/fb_simulated_posts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Meaningful simulated data generated.")
