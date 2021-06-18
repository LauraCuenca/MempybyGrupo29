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

    top_10 = datos_juego[datos_juego["estado"]=='ok']['palabra'].head(10)
    
    data_dibujo = [top_10]
    return data_dibujo



layout = [[sg.Canvas(key='figCanvas')],
          [sg.Button('Salir')]]

window = sg.Window('Grafico',layout,finalize=True,resizable=True,element_justification="center")

data_dibujo = obtener_datos()


fig,ax= plt.subplots(1,1)
column_labels=['Top 10']
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data_dibujo,colLabels=column_labels,loc="center",rowLabels=(1,10))

plt.title("Porcentaje de Partidas por Genero")

graficar(window['figCanvas'].TKCanvas, fig)

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
window.close()