import random

def get_alerts_mock():
    alerts = [
        {"type": "temp", "message": "Température élevée", "value": 32},
        {"type": "humidity", "message": "Humidité basse", "value": 25},
        {"type": "light", "message": "Luminosité anormale", "value": 900},
    ]

    if random.random() < 0.5:
        return []

    return random.sample(alerts, random.randint(1, 3))
