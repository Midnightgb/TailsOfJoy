from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configurar archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rutas
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

# Importar las rutas de la API
from app.api.endpoints import adoption

app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])
