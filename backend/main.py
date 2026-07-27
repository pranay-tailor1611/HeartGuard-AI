from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import logging

from routes import router
from predict import predictor
from config import APP_TITLE, APP_VERSION

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description="Enterprise Healthcare SaaS API for Cardiac Risk Prediction"
)

# Enable CORS for cross-origin frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup Event: Load ML assets once
@app.on_event("startup")
def startup_event():
    logger.info("Initializing FastAPI Backend Services...")
    predictor.load_assets()

# Include API Router
app.include_router(router)

# Mount Frontend Static Files at Root
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
    logger.info(f"Frontend static files mounted from {frontend_path}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
