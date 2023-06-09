import pandas as pd
import numpy as np


def arreglarDelitos():
    condition = csv['codigo_delito_snic_nombre'] == "Suicidios (consumados)"
    newValue = 0
    csv.loc[condition,"cantidad_victimas"] = newValue

def cambiarPalabra(valor):
    valor = str(valor)
    if "estupefacientes" in str(valor):
        valor = valor.replace("estupefacientes", "droga")
    return valor

def pais(valor):
    valor = str(valor)
    if valor == "ARG":
        valor = "Argentina"
    return valor



csv = pd.read_csv("./data/datos.csv")

csvRow = list(csv.columns)

csv['pais_nombre'] = csv['pais_nombre'].apply(pais)

csv['codigo_delito_snic_nombre'] = csv['codigo_delito_snic_nombre'].apply(cambiarPalabra)

arreglarDelitos()

csv.dropna(inplace=True)

print(csv)
