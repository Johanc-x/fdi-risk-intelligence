import pandas as pd
import cx_Oracle


def obtener_simulaciones_empresas(connection_string):
    """
    Extrae los ingresos simulados de todas las empresas desde Oracle.

    Args:
        connection_string (str): usuario/contraseña@host:puerto/SID.

    Returns:
        pd.DataFrame: DataFrame con columnas [id_empresa, pais, año, escenario_id, ingreso_simulado]
    """
    conn = cx_Oracle.connect(connection_string)
    cursor = conn.cursor()

    query = """
        SELECT id_empresa, pais, año, escenario_id, ingreso_simulado
        FROM simulaciones_empresas
    """

    cursor.execute(query)
    columnas = [col[0].lower() for col in cursor.description]
    datos = cursor.fetchall()

    df = pd.DataFrame(datos, columns=columnas)

    cursor.close()
    conn.close()

    return df


def calcular_z_score(df_simulaciones, sensibilidad_dict):
    """
    Calcula el Z-Score de Altman adaptado para cada fila del DataFrame.

    Args:
        df_simulaciones (pd.DataFrame): Contiene columnas ['id_empresa', 'pais', 
        'año', 'escenario_id', 'ingreso_simulado']
        sensibilidad_dict (dict): Diccionario con sensibilidad 
        por empresa: {id_empresa: sensibilidad_fdi}

    Returns:
        pd.DataFrame: Mismo DataFrame original + columna 'z_score'
    """
    z_scores = []

    for _, row in df_simulaciones.iterrows():
        ingreso = row['ingreso_simulado']
        sensibilidad = sensibilidad_dict.get(row['id_empresa'], 0.5)  # Valor por defecto prudente

        # Fórmulas simuladas (ajustadas con lógica ficticia)
        activos_totales = ingreso
        activos_circulantes = ingreso * 0.4
        pasivos_circulantes = ingreso * (0.2 + (1 - sensibilidad) * 0.3)
        utilidad_retenida = ingreso * 0.1
        ebit = ingreso * (0.12 + sensibilidad * 0.08)
        patrimonio = ingreso * sensibilidad
        pasivo_total = ingreso - patrimonio

        # Fórmula Z-Score Altman adaptada
        z = (0.717 * (activos_circulantes - pasivos_circulantes) / activos_totales +
             0.847 * utilidad_retenida / activos_totales +
             3.107 * ebit / activos_totales +
             0.420 * patrimonio / pasivo_total)

        z_scores.append(round(z, 2))

    df_simulaciones['z_score'] = z_scores
    return df_simulaciones



def insertar_zscores_en_oracle(df, connection_string):
    """
    Inserta los Z-Scores calculados en la tabla 'zscore_empresas'.

    Args:
        df (pd.DataFrame): DataFrame con columnas [id_empresa, pais, año, 
        escenario_id, ingreso_simulado, z_score]
        connection_string (str): Cadena de conexión Oracle
    """
    conn = cx_Oracle.connect(connection_string)
    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO zscore_empresas (
            id_empresa, pais, año, escenario_id, ingreso_simulado, z_score
        ) VALUES (:1, :2, :3, :4, :5, :6)
    """

    datos = [
        (
            row["id_empresa"],
            row["pais"],
            row["año"],
            row["escenario_id"],
            row["ingreso_simulado"],
            row["z_score"]
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_sql, datos)
    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Z-Scores insertados correctamente: {len(datos)} registros.")


connection_string = "usuario/contraseña@host:puerto/SID"
# Suponiendo que ya cargaste tus simulaciones desde Oracle:
df = obtener_simulaciones_empresas(connection_string)

# Y ya tienes un diccionario con sensibilidad por empresa:
sensibilidad_dict = {
    1: 0.41, 2: 0.44, 3: 0.81, 4: 0.24, 5: 0.63,
    6: 0.24, 7: 0.99, 8: 0.26, 9: 0.64, 10: 0.45
}

# Calcular Z-Scores:
df_z = calcular_z_score(df, sensibilidad_dict)
print(df_z.head())

# Insertar Z-Cores en BBDD Oracle:

insertar_zscores_en_oracle(df_z, connection_string)
