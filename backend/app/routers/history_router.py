from fastapi import APIRouter
from typing import Optional
from app.services.history_service import get_history_mock

router = APIRouter(prefix="/sensors", tags=["History"])

@router.get("/history")
def history(
    page: int = 1,
    limit: int = 20,
    sensor: Optional[str] = None,
    sort_by: Optional[str] = "timestamp"
):
    return get_history_mock(page, limit, sensor, sort_by)
