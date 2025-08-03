# simulacion_montecarlo.py

import numpy as np
import pandas as pd
import cx_Oracle

def simular_fdi(pais, media, std, años=8, iteraciones=1000):
    """
    Principal función que realiza la simulación de Monte Carlo. 
    En base a un FDI anaul, imula FDI futuro para un país 
    mediante distribución normal.

    Args:
        pais (str): Nombre del país.
        media (float): Media histórica del FDI.
        std (float): Desviación estándar histórica del FDI.
        años (int): Años a proyectar hacia el futuro.
        iteraciones (int): Número de escenarios a simular.

    Returns:
        pd.DataFrame: Resultados con columnas [pais, año, valor_simulado, escenario_id].
    """
    resultados = []

    for i in range(iteraciones):
        for j in range(años):
            año = 2023 + j
            valor = np.random.normal(loc=media, scale=std)
            resultados.append({
                "pais": pais,
                "año": año,
                "valor_simulado": round(valor, 2),
                "escenario_id": i + 1
            })

    return pd.DataFrame(resultados)


"""Esta función fue reemplazada por la lógica directa implementada 
en exploracion_fdi.py, donde se ejecutan simulaciones y se insertan 
directamente en Oracle. Se conserva aquí por si se desea reutilizar como 
utilidad general en otros proyectos."""

def simular_montecarlo_fdi(df_fdi, num_simulaciones=1000, horizonte=5):
    """
    Ejecuta simulación de Monte Carlo para proyectar FDI futuros por país.

    Args:
        df_fdi (dict): Diccionario con DataFrames por país, columnas 'Año' y 'FDI'.
        num_simulaciones (int): Número de escenarios a simular.
        horizonte (int): Número de años hacia el futuro a simular.

    Returns:
        dict: Diccionario con simulaciones por país.
    """
    simulaciones = {}

    for pais, df in df_fdi.items():
        serie = df["FDI"].values

        # Cálculo de estadísticos
        media = np.mean(serie)
        desviacion = np.std(serie)

        # Simulación normal
        simulacion = np.random.normal(loc=media, scale=desviacion, size=(num_simulaciones, horizonte))

        simulaciones[pais] = simulacion

    return simulaciones


def insertar_simulacion_oracle(df_resultados, connection_string):
    """
    Inserta los resultados simulados en la tabla Oracle 'simulaciones_montecarlo'.

    Args:
        df_resultados (pd.DataFrame): DataFrame con columnas [pais, año, valor_simulado, escenario_id].
        connection_string (str): Cadena de conexión para Oracle (usuario/contraseña@host:puerto/servicio).
    """
    connection = cx_Oracle.connect(connection_string)
    cursor = connection.cursor()

    insert_sql = """
        INSERT INTO simulaciones_montecarlo 
        (pais, año, valor_simulado, escenario_id)
        VALUES (:1, :2, :3, :4)
    """

    for _, row in df_resultados.iterrows():
        cursor.execute(insert_sql, (
            row["pais"],
            row["año"],
            row["valor_simulado"],
            row["escenario_id"]
        ))

    connection.commit()
    cursor.close()
    connection.close()

