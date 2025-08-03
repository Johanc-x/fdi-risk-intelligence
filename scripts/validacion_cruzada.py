from scripts.fdi_analysis_preprocessing import limpiar_datos_fdi, procesar_pais
from conexion_Oracle import conectar_oracle
import pandas as pd

# ==============================================
# Script de validación cruzada Python vs Oracle
# ==============================================


# 1. Leer y limpiar CSV

df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)
df_limpio = limpiar_datos_fdi(df)

# 2. Lista de países a validar (Python usa nombres en inglés, Oracle en español)
paises = [
    {"python": "Spain", "oracle": "España"},
    {"python": "Italy", "oracle": "Italia"},
    {"python": "France", "oracle": "Francia"},
    {"python": "Germany", "oracle": "Alemania"},
    {"python": "Netherlands", "oracle": "Países Bajos"},
    {"python": "Greece", "oracle": "Grecia"},
    {"python":"Poland", "oracle": "Polonia"},
    {"python": "Belgium", "oracle": "Bélgica"},
    {"python": "Portugal", "oracle": "Portugal"},
    {"python": "China", "oracle": "China"},
]

# 3. Función para obtener datos desde Oracle
def obtener_datos_oracle(conexion, nombre_pais):
    cursor = conexion.cursor()
    query = """
        SELECT f.anio, f.fdi_porcentaje
        FROM fdi_pais_objeto p,
             TABLE(p.fdi_anual) f
        WHERE p.nombre_pais = :nombre_pais
        ORDER BY f.anio
    """
    cursor.execute(query, {"nombre_pais": nombre_pais})
    resultados = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(resultados, columns=["Año", "FDI_Oracle"])

""""""

# ========================================================
# Validación cruzada con Oracle utilizando try/except/finally
# --------------------------------------------------------
# Este bloque establece la conexión con Oracle y compara
# los datos FDI país por país entre el CSV y la BBDD.
# Se implementa un bloque try/except/finally para:
#   - Capturar errores durante la conexión o consulta.
#   - Evitar la interrupción del script ante fallos.
#   - Asegurar el cierre correcto de la conexión.
# ========================================================

try:
    # 4. Conectar a Oracle
    conexion = conectar_oracle("usuario", "contrasena")
    if not conexion:
        raise Exception("Conexión fallida.")

    # 5. Recorrer países y comparar
    for pais in paises:
        print(f"\nComparando FDI para {pais['python']} / {pais['oracle']}")

        # Procesar desde CSV
        df_python = procesar_pais(df_limpio, pais["python"])
        df_python = df_python.rename(columns={"FDI": "FDI_Python"})

        # Obtener desde Oracle
        df_oracle = obtener_datos_oracle(conexion, pais["oracle"])

        # Comparar por año
        comparacion = df_python.merge(df_oracle, on="Año", how="inner")
        comparacion["Diferencia"] = abs(comparacion["FDI_Python"] - comparacion["FDI_Oracle"])

        # Mostrar resultado
        print(comparacion)

except Exception as error:
    print(f"\nError durante la validación cruzada: {error}")

finally:
    if 'conexion' in locals() and conexion:
        conexion.close()
       
