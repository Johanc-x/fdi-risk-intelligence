import cx_Oracle

""" Funciones de interacción directa con la base de datos Oracle."""

# ===========================
# Generador de INSERT SQL
# ===========================

def generar_insert_oracle(nombre_pais, codigo_pais, df_pais):
    """
    Genera una sentencia SQL INSERT para Oracle con tipos anidados.

    Args:
        nombre_pais (str): Nombre del país (ej. "España").
        codigo_pais (str): Código del país (ej. "ESP").
        df_pais (pd.DataFrame): DataFrame con columnas 'Año' y 'FDI'.

    Returns:
        str: Sentencia SQL INSERT lista para pegar en Oracle SQL Developer.
    """
    valores = []
    for _, fila in df_pais.iterrows():
        valores.append(f"fdi_anual_tipo({fila['Año']}, {round(fila['FDI'], 2)})")

    valores_str = ",\n        ".join(valores)
    
    insert = f"""
    INSERT INTO fdi_pais_objeto VALUES (
        '{nombre_pais}',
        '{codigo_pais}',
        fdi_lista_tipo(
            {valores_str}
        )
    );
    """
    return insert

# ===========================
# Función que realiza una consulta SQL a la BBDD. 
# ===========================

def consultar_fdi_por_pais(conexion, nombre_pais):
    cursor = conexion.cursor()
    """
     Función que ejecuta una consulta SQL en Oracle para obtener los datos 
     de FDI de un país específico.
    """
    query = """
        SELECT p.nombre_pais, f.anio, f.fdi_porcentaje
        FROM fdi_pais_objeto p,
             TABLE(p.fdi_anual) f
        WHERE p.nombre_pais = :nombre_pais
        ORDER BY f.anio
    """

    cursor.execute(query, {"nombre_pais": nombre_pais})
    resultados = cursor.fetchall()

    print(f"\n📊 Datos FDI de {nombre_pais}:")
    for fila in resultados:
        print(f"Año: {fila[1]}, FDI: {fila[2]}%")

    cursor.close()



if __name__ == "__main__":
    from scripts.fdi_analysis_preprocessing import procesar_pais, limpiar_datos_fdi
    from conexion_Oracle import conectar_oracle
    import pandas as pd

    # ========================
    # 1. Diccionarios de mapeo
    # ========================

    nombre_paises = {
        "Germany": "Alemania",
        "France": "Francia",
        "Italy": "Italia",
        "Poland": "Polonia",
        "Netherlands": "Países Bajos",
        "Belgium": "Bélgica",
        "Portugal": "Portugal",
        "Greece": "Grecia"
    }

    codigos_pais = {
        "Germany": "DEU",
        "France": "FRA",
        "Italy": "ITA",
        "Poland": "POL",
        "Netherlands": "NLD",
        "Belgium": "BEL",
        "Portugal": "PRT",
        "Greece": "GRC"
    }

    # ========================
    # 2. Limpieza y procesamiento
    # ========================

    df = pd.read_csv("data/fdi_inflows.csv", skiprows=4)
    df_limpio = limpiar_datos_fdi(df)

    # ========================
    # 3. Generador SQL para INSERT en Oracle
    # ========================

    for nombre_csv in nombre_paises.keys():
        df_pais = procesar_pais(df_limpio, nombre_csv)
        nombre_es = nombre_paises[nombre_csv]
        codigo = codigos_pais[nombre_csv]
        
        sql_insert = generar_insert_oracle(nombre_es, codigo, df_pais)
        print(f"===== INSERT PARA {nombre_es} =====")
        print(sql_insert)

    # ========================
    # 4. Ejecutar la consulta a la BBDD de Oracle. 
    # ========================

    conexion = conectar_oracle("usuario", "contraseña")
    if conexion:
        consultar_fdi_por_pais(conexion, "España")
        conexion.close()
