from fastapi import FastAPI
from core.Logger import Logger
from api.v1.routes import adoption

Logger.info("Starting API")

app = FastAPI()


@app.get("/")
def root():
    return {"status": "true", "message": "API is running"}


app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])