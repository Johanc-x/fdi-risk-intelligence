import random
import cx_Oracle
import numpy as np
from datetime import datetime

"""Este script realiza la creación de empresas ficticias, 
simula como el FDI impactaria en los ingresos futuros bajo un análisis
 de sensibilidad. Realiza la inserción tanto de las empresas como de
 los ingresos simulados a la BBDD de Oracle."""

class Empresa:
    def __init__(self, nombre, pais, sector, ingresos_base, sensibilidad_fdi):
        self.nombre = nombre
        self.pais = pais  # Código tipo "ESP", "USA", etc.
        self.sector = sector
        self.ingresos_base = ingresos_base  # Valor en millones
        self.sensibilidad_fdi = sensibilidad_fdi  # Coef. entre 0 y 1

    def __repr__(self):
        return f"{self.nombre} ({self.pais}) - {self.sector} - Sensibilidad: {self.sensibilidad_fdi}"


def generar_empresas_ficticias():
    nombres = ["TechNova", "GreenCore", "InverPlus", "DataMotion", "FinSphere",
               "Oceanix", "Solaria", "QuantumEdge", "BluePulse", "TerraSmart"]
    paises = ["ESP", "USA", "DEU", "CHN", "IRL"]
    sectores = ["Tecnología", "Energía", "Finanzas", "Construcción", "Logística"]

    empresas = []

    for nombre in nombres:
        pais = random.choice(paises)
        sector = random.choice(sectores)
        ingresos = round(random.uniform(10, 500), 2) * 1_000_000  # entre 10M y 500M
        sensibilidad = round(random.uniform(0.2, 1.0), 2)

        empresa = Empresa(nombre, pais, sector, ingresos, sensibilidad)
        empresas.append(empresa)

    return empresas

# Insertar simulaciones

def simular_ingresos_empresa(base, sensibilidad, años, escenarios):
    # Simula ingresos año a año en función del FDI y sensibilidad.
    
    simulaciones = []
    for esc in range(1, escenarios + 1):
        for j in range(años):
            año = 2023 + j
            factor = np.random.normal(loc=1.0, scale=sensibilidad)
            ingreso = round(base * factor, 2)
            simulaciones.append((año, esc, ingreso))
    return simulaciones

def insertar_simulaciones_empresas(connection_string, años=8, escenarios=1000):
    conn = cx_Oracle.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT id_empresa, nombre, pais, ingresos_base, sensibilidad_fdi FROM empresas_ficticias")
    empresas = cursor.fetchall()

    insert_sql = """
        INSERT INTO simulaciones_empresas (id_empresa, pais, año, escenario_id, ingreso_simulado)
        VALUES (:1, :2, :3, :4, :5)
    """

    for emp in empresas:
        id_emp, _, pais, base, sensibilidad = emp
        datos = simular_ingresos_empresa(base, sensibilidad, años, escenarios)
        registros = [(id_emp, pais, año, esc, ingreso) for (año, esc, ingreso) in datos]
        cursor.executemany(insert_sql, registros)

    conn.commit()
    print(f"✅ Se insertaron simulaciones para {len(empresas)} empresas.")
    cursor.close()
    conn.close()