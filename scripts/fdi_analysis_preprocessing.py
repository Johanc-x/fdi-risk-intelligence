import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

"""
En este script se realizarán las siguientes acciones:
    - Limpieza del DataFrame FDI
    - Conversión y filtrado de años válidos
    - Estadísticas descriptivas por país
    - Generación de gráficos exploratorios
"""

"""funciones para limpieza, procesamiento y cálculo estadístico. """

# =====================================
# Funciones de limpieza de datos
# =====================================

def limpiar_datos_fdi(df):
    """
    Limpia el DataFrame original del CSV:
    - Elimina columnas completamente vacías.
    - Convierte los valores FDI a float.
    - Elimina filas con todos los valores FDI nulos.
    - Mantiene solo los años entre 2000 y 2022 (si están presentes).
    """

    print(f"Shape original: {df.shape}")

    # 1. Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # 2. Verifica qué columnas de año realmente están presentes
    columnas_esperadas = [str(año) for año in range(2000, 2023)]
    columnas_presentes = [col for col in columnas_esperadas if col in df.columns]

    # 3. Selecciona solo columnas válidas
    columnas_validas = ["Country Name", "Country Code"] + columnas_presentes
    df = df[columnas_validas]

    # 4. Convertir columnas de año a float
    for col in columnas_presentes:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 5. Eliminar filas que tengan todos los FDI como NaN
    df = df.dropna(subset=columnas_presentes, how='all')

    print(f"Shape después de limpieza: {df.shape}")
    print(f"¿Hay nulos? {df.isnull().values.any()}")

    return df


# =====================================
# Funcion para la creacion de df por país.
# =====================================

def procesar_pais(df, nombre_pais):
    """
    Filtra el DataFrame por país y transforma los datos para análisis.

    Args:
        df (pd.DataFrame): DataFrame original cargado desde el CSV.
        nombre_pais (str): Nombre del país a procesar.

    Returns:
        pd.DataFrame: DataFrame con columnas 'Año' y 'FDI'.
    """

    cols = ["Country Name", "Country Code"] + [str(a) for a in range(2000, 2023)]
    df_filtrado = df[cols]
    pais = df_filtrado[df_filtrado["Country Name"] == nombre_pais]
    pais = pais.drop(columns=["Country Name", "Country Code"])
    pais = pais.T
    pais = pais.reset_index()
    pais.columns = ['Año','FDI']
    pais["Año"] = pais["Año"].astype(int)
    pais = pais[pais["FDI"].notnull()]

    return pais

# =====================================
# Funciones para el cálculo estadístico por país.
# =====================================

def resumen_estadistico_fdi(df_pais, nombre_pais):
    """
    Calcula y devuelve estadísticas completas del FDI de un país.
    También imprime los resultados ordenadamente.

    Args:
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.
        nombre_pais (str): Nombre del país.

    Returns:
        dict: Diccionario con todas las métricas estadísticas calculadas.
    """
    print(f"\nAnálisis estadístico completo de {nombre_pais}")

    serie = df_pais['FDI'].dropna()

    promedio = serie.mean()
    mediana = serie.median()
    rango = serie.max() - serie.min()
    desviacion = serie.std()
    var_5 = np.percentile(serie, 5)
    best_95 = np.percentile(serie, 95)
    diff_yoy = serie.diff().fillna(0)
    promedio_yoy = diff_yoy.mean()

    print(f"Promedio: {promedio:.2f}% del PIB")
    print(f"Mediana: {mediana:.2f}% del PIB")
    print(f"Rango: {rango:.2f}%")
    print(f"Desviación estándar: {desviacion:.2f}%")
    print(f"Value at Risk (5%): {var_5:.2f}% del PIB")
    print(f"Best Case (95%): {best_95:.2f}% del PIB")
    print(f"Promedio de variación interanual: {promedio_yoy:.2f}%")

    return {
        "promedio": promedio,
        "mediana": mediana,
        "rango": rango,
        "desviacion_estandar": desviacion,
        "VaR_5": var_5,
        "BestCase_95": best_95,
        "variacion_yoy_promedio": promedio_yoy
    }


# =====================================
# Funcion que agrupa las 3 funciones anteriores en una sola.
# para automatizar el proceso de limpieza y cálculo estadístico.
# =====================================

def analizar_fdi(df, nombre_filtro, nombre_visible):
    df_pais = procesar_pais(df, nombre_filtro)
    resumen = resumen_estadistico_fdi(df_pais, nombre_visible)
    return df_pais, resumen  

"""Funciones para la creación de gráficos"""

# =====================================
# Funcion para la creación de gráfica por país.
# =====================================


def graficar_fdi(df_pais, nombre_pais, ruta_salida):
    """
    Genera un gráfico de líneas con la evolución del FDI.

    Args:
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.
        nombre_pais (str): Nombre del país.
        ruta_salida (str): Ruta donde guardar la imagen .png.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df_pais["Año"], df_pais["FDI"], marker='o', label=nombre_pais)
    plt.axhline(df_pais["FDI"].mean(), color='red', linestyle='--', label='Promedio')
    plt.title(f"Flujo de Inversión Extranjera Directa (% PIB) - {nombre_pais}")
    plt.xlabel("Año")
    plt.ylabel("FDI (% PIB)")
    plt.legend()
    plt.grid(True)
    print(f"📁 Guardando gráfica en: {ruta_salida}")
    plt.savefig(ruta_salida)
    plt.close()



# =====================================
# Funcion para generar un gráfico comparativo entre países.
# =====================================


def graficar_comparativo(paises_data, ruta_salida):
    """
    Genera un gráfico comparativo de FDI para múltiples países.

    Args:
        paises_data (dict): Diccionario con clave el nombre visible del país y valor su DataFrame.
        ruta_salida (str): Ruta para guardar la imagen comparativa.
    """
    plt.figure(figsize=(12, 6))
    
    for nombre_pais, df in paises_data.items():
        plt.plot(df["Año"], df["FDI"], marker='o', label=nombre_pais)

    plt.title("Comparación FDI (% del PIB) - 2000 a 2022")
    plt.xlabel("Año")
    plt.ylabel("FDI (% PIB)")
    plt.legend()
    plt.grid(True)
    print(f"📊 Guardando gráfico comparativo en: {ruta_salida}")
    plt.savefig(ruta_salida)
    plt.close()

"""Función para almacenar el resumen estadístico"""

# =====================================
# Función que genera un archivo nuevo con el resumen estadístico por país.
# =====================================

def generar_resumen(resumenes_data, ruta_archivo="docs/resumen_fdi.txt"):
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write("RESUMEN ESTADÍSTICO FDI (% del PIB)\n")
        f.write("=" * 50 + "\n\n")

        for nombre_pais, resumen in resumenes_data.items():
            f.write(f"{nombre_pais}\n")
            f.write(f"Promedio: {resumen['promedio']:.2f}%\n")
            f.write(f"Mediana: {resumen['mediana']:.2f}%\n")
            f.write(f"Rango: {resumen['rango']:.2f}%\n")
            f.write(f"Desviación estándar: {resumen['desviacion_estandar']:.2f}%\n")
            f.write(f"Value at Risk (5%): {resumen['VaR_5']:.2f}%\n")
            f.write(f"Best Case (95%): {resumen['BestCase_95']:.2f}%\n")
            f.write(f"Variación interanual promedio: {resumen['variacion_yoy_promedio']:.2f}%\n")
            f.write("-" * 50 + "\n\n")

