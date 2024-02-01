from fastapi import FastAPI
from starlette.requests import Request
import os
from dotenv import load_dotenv
from logger.Logger import Logger
from api.endpoints_v1 import adoption

load_dotenv()

Logger.info("Starting API")

app = FastAPI()

@app.get("/")
def root(request: Request):
    return {"message": "API IS RUNNING"}

app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])
