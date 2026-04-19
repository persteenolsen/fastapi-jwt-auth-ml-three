from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth, predict, history

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI ML v3")

app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(history.router)


@app.get("/")
def root():
    return {"message": "API running"}