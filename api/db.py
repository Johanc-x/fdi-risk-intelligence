# api/db.py
import cx_Oracle

def conectar_oracle():
    try:
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
        conn = cx_Oracle.connect("system", "Success_0425", dsn)
        return conn
    except cx_Oracle.Error as e:
        print("❌ Error al conectar con Oracle:", e)
        return None
