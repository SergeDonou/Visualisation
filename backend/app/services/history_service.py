import random
from datetime import datetime, timedelta

def generate_mock_history():
    sensors = ["temp", "humidity", "light"]
    history = []
    now = datetime.now()

    for day_offset in range(5):
        day = now - timedelta(days=day_offset)

        for hour in range(0, 24, 3):
            timestamp = day.replace(hour=hour, minute=0, second=0, microsecond=0)

            entry = {
                "timestamp": timestamp.isoformat(),
                "sensor": random.choice(sensors),
                "value": round(random.uniform(10, 35), 2)
            }

            history.append(entry)

    history = sorted(history, key=lambda x: x["timestamp"])
    return history


def get_history_mock(page, limit, sensor, sort_by):
    data = generate_mock_history()

    if sensor:
        data = [d for d in data if d["sensor"] == sensor]

    data = sorted(data, key=lambda x: x[sort_by])

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(data),
        "items": data[start:end]
    }
