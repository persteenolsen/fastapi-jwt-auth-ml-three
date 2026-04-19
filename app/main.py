from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth, predict, history

Base.metadata.create_all(bind=engine)

# app = FastAPI(title="FastAPI ML v3")

# -----------------------------
# INIT APP
# -----------------------------
app = FastAPI(
    title="FastAPI + JWT + ML (v3)",
    description="19-04-2026 - House Price Prediction API with ML pipeline + JWT auth + PostgreSQL",
    version="3.0.0",
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(history.router)


@app.get("/")
def root():
    return {"message": "FastAPI + JWT + ML v3 is running"}