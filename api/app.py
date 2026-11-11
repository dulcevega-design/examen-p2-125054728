from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os, psycopg2

app = FastAPI()

def get_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        user=os.getenv("POSTGRES_USER", "datamart_user"),
        password=os.getenv("POSTGRES_PASSWORD", "datamart_pass"),
        dbname=os.getenv("POSTGRES_DB", "datamart_db")
    )

class Registro(BaseModel):
    clave: str
    subclave: str = None
    valor: float

@app.get("/resultados")
def get_resultados():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, clave, subclave, valor FROM resultados;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "hora": r[1], "categoria": r[2], "ingreso": float(r[3])} for r in rows]

@app.get("/resultados/{clave}")
def get_resultado_by_clave(clave: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, clave, subclave, valor FROM resultados WHERE clave = %s;", (clave,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="Hora no encontrada")
    return [{"id": r[0], "hora": r[1], "categoria": r[2], "ingreso": float(r[3])} for r in rows]

@app.post("/resultados")
def create_registro(reg: Registro):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO resultados (clave, subclave, valor) VALUES (%s, %s, %s) RETURNING id;",
                (reg.clave, reg.subclave, reg.valor))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": new_id, "status": "creado"}
