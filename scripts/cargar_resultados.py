import os, psycopg2

def cargar():
    db_host = os.getenv("POSTGRES_HOST", "db")
    db_user = os.getenv("POSTGRES_USER", "datamart_user")
    db_pass = os.getenv("POSTGRES_PASSWORD", "datamart_pass")
    db_name = os.getenv("POSTGRES_DB", "datamart_db")

    conn = psycopg2.connect(host=db_host, user=db_user, password=db_pass, dbname=db_name)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id SERIAL PRIMARY KEY,
            clave VARCHAR(100),
            subclave VARCHAR(100),
            valor NUMERIC
        );
    """)

    path_resultado = "/app/mapreduce/output/part-00000"
    if os.path.exists(path_resultado):
        with open(path_resultado, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cur.execute("INSERT INTO resultados (clave, subclave, valor) VALUES (%s, %s, %s)",
                                (parts[0], parts[1], float(parts[2])))
        conn.commit()
        print("Resultados cargados exitosamente en la base de datos.")
    else:
        print(f"Archivo {path_resultado} no encontrado.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    cargar()
