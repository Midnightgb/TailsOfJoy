from fastapi import FastAPI
from core.Logger import Logger
#from api.v1.routes import pets
from api.routes import health_checker
from api.routes import user_router

Logger.info("Starting API")

app = FastAPI()


@app.get("/")
def root():
    return {"status": "true", "message": "API is running"}


#app.include_router(pets.router)
app.include_router(health_checker.router)
app.include_router(user_router.router)