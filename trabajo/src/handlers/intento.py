from os import X_OK
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


datos_puntos= pd.read_csv('datos_de_puntos.csv')


facil= datos_puntos[datos_puntos['nivel']=='Facil']
filtro = facil[['nick', 'puntos']]
filtro = filtro.groupby('nick')[['nick', 'puntos']].sum()
ranking = filtro.sort_values(by='puntos', ascending=False).reset_index()[:3]
#ranking = filtro_f.sort_values(by='puntos', ascending=False)[:5]

medio= datos_puntos[datos_puntos['nivel']=='Medio']
filtro = medio[['nick', 'puntos']]
filtro = filtro.groupby('nick')[['nick', 'puntos']].sum()
ranking_m = filtro.sort_values(by='puntos', ascending=False).reset_index()[:3]

dif= datos_puntos[datos_puntos['nivel']=='Dificil']
filtro = dif[['nick', 'puntos']]
filtro = filtro.groupby('nick')[['nick', 'puntos']].sum()
ranking_d = filtro.sort_values(by='puntos', ascending=False).reset_index()[:3]

print(ranking_d)

