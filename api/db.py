# api/db.py
import cx_Oracle
import os

def conectar_oracle():
    try:
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
        user = os.getenv("ORACLE_USER", "usuario_por_defecto")
        password = os.getenv("ORACLE_PASS", "contraseña_por_defecto")
        conn = cx_Oracle.connect(user, password, dsn)
        return conn
    except cx_Oracle.Error as e:
        print("❌ Error al conectar con Oracle:", e)
        return None
