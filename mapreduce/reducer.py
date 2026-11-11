#!/usr/bin/env python3
import sys

current_key = None
total_ingreso = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    parts = line.split('\t')
    if len(parts) != 2:
        continue
        
    key, valor_str = parts
    try:
        valor = float(valor_str)
    except ValueError:
        continue

    if current_key == key:
        total_ingreso += valor
        count += 1
    else:
        if current_key:
            promedio = total_ingreso / count
            print(f"{current_key}\t{promedio:.2f}")
        current_key = key
        total_ingreso = valor
        count = 1

if current_key and count > 0:
    promedio = total_ingreso / count
    print(f"{current_key}\t{promedio:.2f}")
