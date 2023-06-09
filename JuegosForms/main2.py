import pandas as pd
import numpy as np



def arreglarMMO():
    condition = csv['Cual es tu genero favorito?'] == "MMO RPG NO LINEAL (alvion online)"
    newValue = 'COMO VAS A JUGAR UN MMO SOLO PA'
    csv.loc[condition,"Prefieres jugar solo o con amigos"] = newValue


def genero(valor):
    valor = str(valor)
    if valor == "MOBA":
        valor = "LoL como el joakod"
    return valor

def horas(valor):
    valor = str(valor)
    if valor == "70-100 horas":
        valor = "full gordito vicio"
    return valor



csv = pd.read_csv("./juegodatos.csv")


csv['Cual es tu genero favorito?'] = csv['Cual es tu genero favorito?'].apply(genero)

csv['Cuantas horas juegas al mes?'] = csv['Cuantas horas juegas al mes?'].apply(horas)

arreglarMMO()

csv.dropna(inplace=True)

print(csv)