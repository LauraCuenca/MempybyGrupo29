import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

def iterar(data):
    """

    """
    lista_de_listas = []
    for x in range(len(data)):
        lista_de_listas += [[data[x]]]
    return lista_de_listas

datos_juego= pd.read_csv('datos_de_partidas.csv')
    

partidas_timeout= datos_juego[datos_juego["estado"]=='timeout']['nro_de_partida']
partidas_timeout= list(partidas_timeout)


for i in len(partidas_timeout):
        palabras= datos_juego[datos_juego["nro_de_partida"]==int(iterar(partidas_timeout))]['palabra'].dropna()

print(palabras)
