import cx_Oracle

def conectar_oracle(usuario, contrasena, host="localhost", puerto=1521, sid="xe"):
    dsn = cx_Oracle.makedsn(host, puerto, sid=sid)
    try:
        conexion = cx_Oracle.connect(usuario, contrasena, dsn)
        print("✅ Conexión establecida con Oracle.")
        return conexion
    except cx_Oracle.Error as error:
        print(f"❌ Error al conectar con Oracle: {error}")
        return None


if __name__ == "__main__":
    conexion = conectar_oracle("Usuario", "Contraseña")
    if conexion:
        conexion.close()
