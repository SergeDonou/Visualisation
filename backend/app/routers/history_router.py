from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/sensors", tags=["Sensors"])

@router.get("/history")
def get_history(
    page: int = 1,
    limit: int = 20,
    sensor: Optional[str] = None,
    sort_by: Optional[str] = "timestamp"
):
    # Données mock
    data = [
        {"sensor": "temp", "value": 22.1, "timestamp": "2026-04-02T13:00:00"},
        {"sensor": "temp", "value": 22.3, "timestamp": "2026-04-02T13:30:00"},
        {"sensor": "temp", "value": 22.5, "timestamp": "2026-04-02T14:00:00"},
    ]

    # Filtre capteur
    if sensor:
        data = [d for d in data if d["sensor"] == sensor]

    # Tri
    data = sorted(data, key=lambda x: x[sort_by])

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(data),
        "items": data[start:end]
    }
