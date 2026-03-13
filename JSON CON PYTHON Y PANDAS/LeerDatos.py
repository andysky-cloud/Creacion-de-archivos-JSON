import pandas as pd
import os

archivo = "registros.csv"

df = pd.read_csv(archivo)

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

while True:

    limpiar()

    print("SISTEMA DE REGISTROS")
    print("1. Ver registros")
    print("2. Agregar registro")
    print("3. Ver estadisticas")
    print("4. Exportar datos")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        limpiar()
        print(df)
        input("\nPresione ENTER para continuar")

    elif opcion == "2":
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        programa = input("Programa: ")

        nuevo = pd.DataFrame([[nombre, edad, programa]], columns=df.columns)

        df = pd.concat([df, nuevo], ignore_index=True)

        df.to_csv(archivo, index=False)

        print("Registro agregado")
        input("Presione ENTER")

    elif opcion == "3":
        limpiar()
        print("REPORTE ESTADISTICO\n")
        print(df.describe())
        print("\nCantidad por programa\n")
        print(df["programa"].value_counts())
        input("\nPresione ENTER")

    elif opcion == "4":
        df.to_csv("exportado.csv", index=False)
        df.to_json("exportado.json", orient="records", indent=4)
        print("Archivos exportados")
        input("Presione ENTER")

    elif opcion == "5":
        break

    else:
        print("Opcion invalida")
        input("Presione ENTER")