import sys, csv, time

def procesar_secuencial(filepath):
    inicio = time.time()
    totales = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Ignorar encabezado
        for row in reader:
            if len(row) == 8:
                try:
                    fecha_hora = row[1]
                    cat = row[3]
                    cant = float(row[5])
                    precio = float(row[6])
                    hora = int(fecha_hora.split(" ")[1].split(":")[0])
                    clave = (hora, cat)
                    totales[clave] = totales.get(clave, 0.0) + (cant * precio)
                except (ValueError, IndexError):
                    continue
    fin = time.time()
    print(f"Tiempo de ejecución secuencial: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        procesar_secuencial(sys.argv[1])
