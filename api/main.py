from fastapi import FastAPI
from api.alerts import router as alerts_router  # Importamos el router

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente."}

app.include_router(alerts_router)  # Activamos la ruta /alertas-quiebra

