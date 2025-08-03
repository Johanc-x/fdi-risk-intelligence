import pandas as pd
import matplotlib.pyplot as plt
import cx_Oracle
from scripts.fdi_analysis_preprocessing import (limpiar_datos_fdi, analizar_fdi, procesar_pais,
                       graficar_comparativo, generar_resumen,)
from empresas import generar_empresas_ficticias, insertar_simulaciones_empresas

"""
Script auxiliar para pruebas de desarrollo.
Se utilizó para ejecutar simulaciones, generar resúmenes y hacer inserciones 
en Oracle.

"""

#Cargar archivo
df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)

# Limpieza de datos.

df_limpio= limpiar_datos_fdi(df)
print(df_limpio)
# df individuales por país.



top5_mejoresFDI = {
    "Italia" : "Italy",
    "Irlanda" : "Ireland",
    "Bélgica" : "Belgium",
    "Portugal" : "Portugal",
    "Polonia" : "Poland"
}

# 5 peores FDI 

peores_5 = {
    "Grecia"  : "Greece",
    "Italia"  : "Italy",
    "Estados Unidos de América" : "United States",
    "Francia" : "France",
    "China"   : "China"
}

bloques_geopoliticos = {
    "Unión Europea": "European Union",
    "Estados Unidos": "United States",
    "China": "China"
}

# Resúmenes estadísticos por país
paises_data = {}
resumenes_data = {}

for nombre_visible, filtro in bloques_geopoliticos.items():
    df_pais, resumen = analizar_fdi(df_limpio, filtro, nombre_visible)
    paises_data[nombre_visible] = df_pais
    resumenes_data[nombre_visible] = resumen



# Gráfico comparativo
graficar_comparativo(paises_data, "img/fdi_comparativo_bloque3png")

# Crear resumen
generar_resumen(resumenes_data, ruta_archivo="docs/resumen_fdi_bloque3.txt")


# ==========================================
# Simulación Monte Carlo para China
# ==========================================

# df_china = procesar_pais(df_limpio, "China")
# media_china = df_china["FDI"].mean()
# std_china = df_china["FDI"].std()

# df_simulado = simular_fdi("CHN", media_china, std_china, años=8, iteraciones=500)
# print(df_simulado)
# # Conexión Oracle (aqui hay que insertar tu usuario y contraseña de tu BBDD)
# connection_string = "usuario/contraseña@host:puerto/SID"

# insertar_simulacion_oracle(df_simulado, connection_string)

"""Insertar simulaciones de todos los paises que se encuentran en la tabla
fdi_pais_objeto en Oracle"""

# paises_dict = {
#     "European Union": "EUU",
#     "United States": "USA",
#     "Germany": "DEU",
#     "France": "FRA",
#     "Spain": "ESP",
#     "Ireland": "IRL",
#     "Italy": "ITA",
#     "Poland": "POL",
#     "Netherlands": "NLD",
#     "Belgium": "BEL",
#     "Portugal": "PRT",
#     "Greece": "GRC"
# }


# Conexión Oracle (Inserta los datos reales de la BBDD que quieras conectar)
# connection_string = "usuario/contraseña@host:puerto/SID"

# for nombre, codigo in paises_dict.items():
#     df_pais = procesar_pais(df_limpio, "European Union")
#     media = df_pais["FDI"].mean()
#     std = df_pais["FDI"].std()

#     df_simulado = simular_fdi("EUU", media, std, años=8, iteraciones=1000)
    
#     insertar_simulacion_oracle(df_simulado, connection_string)

# print(df_limpio["Country Name"].unique())

# Conexión Oracle
# connection_string = "usuario/contraseña@host:puerto/SID"
# connection = cx_Oracle.connect(connection_string)
# cursor = connection.cursor()

# # Generar empresas
# empresas = generar_empresas_ficticias()

# for e in empresas:
#     print(e)

# # Insertar la lista generada en Oracle. 

# for emp in empresas:
#     cursor.execute("""
#         INSERT INTO empresas_ficticias (nombre, pais, sector, ingresos_base, sensibilidad_fdi)
#         VALUES (:1, :2, :3, :4, :5)
#     """, (emp.nombre, emp.pais, emp.sector, emp.ingresos_base, emp.sensibilidad_fdi))

# connection.commit()
# print(f"Se insertaron {len(empresas)} empresas ficticias en Oracle.")
# cursor.close()
# connection.close()

# # Insertar simulaciones
# connection_string = "usuario/contraseña@host:puerto/SID"
# insertar_simulaciones_empresas(connection_string, años=8, escenarios=1000)
