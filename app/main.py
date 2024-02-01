from fastapi import FastAPI
import os
from dotenv import load_dotenv
from logger.Logger import Logger
from api.v1.routes import adoption

load_dotenv()

Logger.info("Starting API")

app = FastAPI()

# Obtener el puerto de Heroku o usar el 8000 de forma predeterminada
port = int(os.environ.get("PORT", 8000))

@app.get("/")
def root():
    return {"status": "true", "message": "API is running"}

app.include_router(adoption.router, prefix="/adoption", tags=["adoption"])

if __name__ == "__main__":
    import uvicorn

    # Asegurar que la aplicación se ejecute en el puerto proporcionado por Heroku
    uvicorn.run(app, host="0.0.0.0", port=port)
