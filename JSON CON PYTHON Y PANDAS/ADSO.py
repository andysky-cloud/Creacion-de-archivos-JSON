import json
import urllib.request

url = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/SENA.matriculados.json"

with urllib.request.urlopen(url) as respuesta:
    datos = json.loads(respuesta.read().decode())

adso = []

for aprendiz in datos:
    if "ANALISIS Y DESARROLLO DE SOFTWARE" in aprendiz["PROGRAMA"].upper():
        adso.append(aprendiz)

print("Cantidad aprendices ADSO:", len(adso))

with open("ADSO-CTPI.json", "w", encoding="utf-8") as archivo:
    json.dump(adso, archivo, indent=4, ensure_ascii=False)

print("Archivo ADSO-CTPI.json creado")

ficha = []

for aprendiz in adso:
    if aprendiz["FICHA"] == 3312932:
        ficha.append(aprendiz)

print("Aprendices ficha 3312932:", len(ficha))

filtro = []

for aprendiz in datos:
    if aprendiz["CODIGO_PROGRAMA"] == 228118 and aprendiz["ESTADO_APRENDIZ"] == "En transito":
        filtro.append(aprendiz)

print("Cantidad con codigo 228118 y estado En transito:", len(filtro))