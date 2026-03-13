import csv
import json

totales = {}
conteo = {}


with open("vendedores.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        vendedor = fila["vendedor"]
        ventas = int(fila["ventas"])

        if vendedor not in totales:
            totales[vendedor] = 0
            conteo[vendedor] = 0

        totales[vendedor] += ventas
        conteo[vendedor] += 1



print("TOTAL POR VENDEDOR")
for vendedor in totales:
    print(vendedor, ":", totales[vendedor])



print("\nPROMEDIO MENSUAL")
for vendedor in totales:
    promedio = totales[vendedor] / conteo[vendedor]
    print(vendedor, ":", promedio)



mayor = max(totales, key=totales.get)

print("\nVENDEDOR CON MAYORES VENTAS")
print(mayor, ":", totales[mayor])



ranking = sorted(totales.items(), key=lambda x: x[1], reverse=True)

ranking_json = []

for vendedor, total in ranking:
    promedio = total / conteo[vendedor]

    ranking_json.append({
        "vendedor": vendedor,
        "total_ventas": total,
        "promedio_mensual": promedio
    })



with open("ranking.json", "w") as archivo:
    json.dump(ranking_json, archivo, indent=4)

print("\nArchivo ranking.json creado correctamente")