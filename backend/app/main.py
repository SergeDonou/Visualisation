# ------------------------------------------------------------
# Imports principaux FastAPI
# ------------------------------------------------------------
from fastapi import FastAPI
from fastapi import Request

# ------------------------------------------------------------
# Import de l'initialisation de la base de données
# (appelée automatiquement au démarrage)
# ------------------------------------------------------------
from .database import init_db

# ------------------------------------------------------------
# Middleware CORS pour autoriser le frontend à appeler l'API
# ------------------------------------------------------------
from fastapi.middleware.cors import CORSMiddleware

# ------------------------------------------------------------
# Gestion des réponses JSON personnalisées
# ------------------------------------------------------------
from fastapi.responses import JSONResponse

# ------------------------------------------------------------
# Gestion des erreurs et affichage des traces
# ------------------------------------------------------------
import traceback
from fastapi.exceptions import RequestValidationError

# ------------------------------------------------------------
# Import des routers (endpoints)
# ------------------------------------------------------------
from app.routers.sensors_router import router as sensors_router
from app.routers.history_router import router as history_router
from app.routers.alerts_router import router as alerts_router


# ------------------------------------------------------------
# Création de l'application FastAPI
# ------------------------------------------------------------
app = FastAPI()


# ------------------------------------------------------------
# Événement exécuté automatiquement au démarrage de l'API
# Ici, on initialise la connexion à la base (si disponible)
# ------------------------------------------------------------
@app.on_event("startup")
def startup_event():
    init_db()


# ------------------------------------------------------------
# Endpoint simple pour vérifier que l'API fonctionne
# Utile pour les tests rapides ou les outils de monitoring
# ------------------------------------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ------------------------------------------------------------
# Middleware CORS
# Permet au frontend (HTML/JS) d'appeler l'API FastAPI
# Ici, on autorise tout ("*") pour simplifier le développement
# ------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre plus tard en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------------------
# Gestion globale des erreurs (Exception)
# Si une erreur non gérée survient, on renvoie une réponse 500
# et on affiche la trace dans la console pour le debug
# ------------------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("Erreur serveur :", traceback.format_exc())
    return JSONResponse(
        status_code=500,
        content={"detail": "Erreur interne du serveur"}
    )


# ------------------------------------------------------------
# Gestion des erreurs de validation (422)
# Exemple : paramètres manquants, mauvais types, etc.
# ------------------------------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )


# ------------------------------------------------------------
# Inclusion des routers (endpoints)
# Chaque router gère une partie de l'API
# ------------------------------------------------------------
app.include_router(sensors_router)
app.include_router(history_router)
app.include_router(alerts_router)
