
import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def graficar(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def obtener_datos():

    datos_juego= pd.read_csv('datos_de_partidas.csv')

    partidas_aband = datos_juego['estado'].str.contains('abandono').value_counts()[True]
    partidas_cancel = datos_juego['estado'].str.contains('finalizada').value_counts()[True]
    partidas_finalizadas= datos_juego['estado'].str.contains('abandono').value_counts()[True]
    

    etiquetas = ["Abandonada","Cancelada","Terminada"]
    data_dibujo = [partidas_aband, partidas_cancel,partidas_finalizadas]
    return etiquetas, data_dibujo



layout = [[sg.Canvas(key='figCanvas')],
          [sg.Button('Salir')]]

window = sg.Window('Grafico',layout,finalize=True,resizable=True,element_justification="center")

etiquetas, data_dibujo = obtener_datos()

explode = (0,0,0)
fig = plt.figure()
plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%',
        shadow=True, startangle=90, labeldistance=1.1)
plt.axis('equal')
plt.legend(etiquetas)

plt.title("Porcentaje de Partidas por Estado")

graficar(window['figCanvas'].TKCanvas, fig)

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
window.close()