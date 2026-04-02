from fastapi import APIRouter

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.get("/latest")
def get_latest_sensor():
    return {
        "sensor": "temperature",
        "value": 22.5,
        "timestamp": "2026-04-02T14:00:00"
    }

@router.get("/history")
def get_sensor_history():
    return [
        {"value": 22.1, "timestamp": "2026-04-02T13:00:00"},
        {"value": 22.3, "timestamp": "2026-04-02T13:30:00"},
        {"value": 22.5, "timestamp": "2026-04-02T14:00:00"},
    ]

@router.get("/by-id/{id}")
def get_sensor_by_id(id: int):
    return {"id": id, "sensor": "humidity", "value": 45}
