import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.core.base import DataError


def graficar(canvas, figure):
    """ Arma la figura """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""

    datos_juego= pd.read_csv('datos_de_partidas.csv')

    partidas_genero = datos_juego["genero"].value_counts()
    nombres = datos_juego["genero"].unique()
    
    print(nombres)

    data_dibujo = partidas_genero
    etiquetas = nombres
    return etiquetas, data_dibujo



layout = [[sg.Canvas(key='figCanvas')],
           [sg.Button('Salir')]]

window = sg.Window('Grafico',layout,finalize=True,resizable=True,element_justification="center")

etiquetas, data_dibujo = obtener_datos()


fig = plt.figure()
plt.bar(data_dibujo,height=data_dibujo)

plt.legend(etiquetas)

plt.title("Porcentaje de Partidas por Genero")


graficar(window['figCanvas'].TKCanvas, fig)
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
window.close()