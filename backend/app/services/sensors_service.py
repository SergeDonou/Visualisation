import random
from datetime import datetime

def get_latest_mock():
    return {
        "temperature": round(random.uniform(18, 30), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "light": random.randint(100, 800),
        "timestamp": datetime.now().isoformat()
    }

def get_sensor_by_id_mock(id: int):
    return {
        "id": id,
        "sensor": "temp",
        "value": round(random.uniform(18, 30), 2),
        "timestamp": datetime.now().isoformat()
    }
