import PySimpleGUI as sg
import csv
import pandas as pd

def procesar_puntos():

    datos_puntos = pd.read_csv("src/handlers/datos_de_puntos.csv", encoding="utf-8")

    print(datos_puntos.head(10))

    ranking = datos_puntos['puntos'].sort_value()[:10]

    print(ranking)