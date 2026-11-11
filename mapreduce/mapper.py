#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("id"):
        continue
    parts = line.split(",")
    if len(parts) != 8:
        continue
    try:
        fecha_hora = parts[1]
        cat = parts[3]
        cant = float(parts[5])
        precio = float(parts[6])
        
        # Extraer hora (0-23) de 'YYYY-MM-DD HH:MM:SS'
        hora = fecha_hora.split(" ")[1].split(":")[0]
        ingreso = cant * precio
        
        print(f"{hora}\t{cat}\t{ingreso}")
    except (ValueError, IndexError):
        continue
