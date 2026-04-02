from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import traceback

from app.routers.sensors_router import router as sensors_router
from app.routers.history_router import router as history_router
from app.routers.alerts_router import router as alerts_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("Erreur serveur :", traceback.format_exc())
    return JSONResponse(status_code=500, content={"detail": "Erreur interne du serveur"})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})

app.include_router(sensors_router)
app.include_router(history_router)
app.include_router(alerts_router)
