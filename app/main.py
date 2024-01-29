from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os
from dotenv import load_dotenv

from api.endpoints_v1 import adoption  

load_dotenv()


app = FastAPI()

# Configurar archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])