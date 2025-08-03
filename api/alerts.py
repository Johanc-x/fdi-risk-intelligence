# api/alerts.py
from fastapi import APIRouter
from api.db import conectar_oracle
import pandas as pd

router = APIRouter()

@router.get("/alertas-quiebra")
def obtener_alertas(limit: int = 100):  # Valor por defecto: 100
    conn = conectar_oracle()
    
    if not conn:
        return {"error": "No se pudo conectar a la base de datos"}

    cursor = conn.cursor()
    
    query = f"""
        SELECT id_empresa, año, escenario_id, z_score, mensaje, fecha_alerta
        FROM alertas_empresas
        ORDER BY fecha_alerta DESC
        FETCH FIRST {limit} ROWS ONLY
    """
    
    cursor.execute(query)
    columnas = [col[0].lower() for col in cursor.description]
    resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    return resultados
