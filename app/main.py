from fastapi import FastAPI
import os
from dotenv import load_dotenv
from logger.Logger import Logger
from api.v1.routes import adoption

load_dotenv()

Logger.info("Starting API")

app = FastAPI()


@app.get("/")
def root():
    return {"status": "true", "message": "API is running"}


app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])