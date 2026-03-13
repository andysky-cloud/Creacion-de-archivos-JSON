import json

# Leer archivo JSON
with open("productos.json", "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)

total_inventario = 0
bajo_stock = []

for p in productos:
    # valor total por producto
    valor_total = p["precio"] * p["cantidad"]
    print(p["producto"], "- Valor total:", valor_total)

    total_inventario += valor_total

    # verificar bajo stock
    if p["cantidad"] < 5:
        bajo_stock.append(p)

# valor total del inventario
print("\nValor total del inventario:", total_inventario)

# exportar productos con bajo stock
with open("bajo_stock.json", "w", encoding="utf-8") as archivo:
    json.dump(bajo_stock, archivo, indent=4)

print("Archivo de productos con bajo stock creado")