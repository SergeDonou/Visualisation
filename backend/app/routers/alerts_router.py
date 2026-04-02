from fastapi import APIRouter
from app.services.alerts_service import get_alerts_mock

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/")
def alerts():
    return get_alerts_mock()
