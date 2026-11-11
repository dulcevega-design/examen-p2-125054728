# Examen Parcial 2 - Pipeline Big Data (125054728)

Pipeline end-to-end con Hadoop MapReduce, PostgreSQL y FastAPI en Docker.

## Arquitectura
1. Generacion de datos en Python.
2. MapReduce procesa 5M+ de registros en 240 agregados.
3. PostgreSQL almacena los resultados.
4. FastAPI expone /resultados/.

## Ejecucion
```bash
docker-compose up -d --build
python3 scripts/cargar_resultados.py
```
