from fastapi import APIRouter
from app.services.sensors_service import get_latest_mock, get_sensor_by_id_mock

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.get("/latest")
def latest():
    return get_latest_mock()

@router.get("/by-id/{id}")
def by_id(id: int):
    return get_sensor_by_id_mock(id)
