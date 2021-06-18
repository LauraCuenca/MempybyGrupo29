
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
    print(datos_juego.columns)
    partidas_aband = datos_juego[datos_juego['evento']=='fin']&[datos_juego['estado'].str.contains("abandono").value_counts()]
    partidas_cancel = datos_juego[datos_juego['evento']=='fin']&[datos_juego['estado'].str.contains("cancelado").value_counts()]
    partidas_finalizadas= datos_juego[datos_juego['evento']=='fin']&[datos_juego['estado'].str.contains("finalizada").value_counts()]
    #gol_brasileros = goleadores_x_edicion[goleadores_x_edicion["Selección"].str.contains("Brasil")]

    etiquetas = ["Argentina", "Brasil"]
    data_dibujo = [partidas_aband, partidas_cancel,partidas_finalizadas]
    return etiquetas, data_dibujo



layout = [[sg.Canvas(key='figCanvas')],
          [sg.Button('Salir')]]
window = sg.Window('Argentina vs. Brasil',
                   layout,
                   finalize=True,
                   resizable=True,
                   element_justification="right")

etiquetas, data_dibujo = obtener_datos()

explode = (0.1, 0)
fig = plt.figure()
plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%',
        shadow=True, startangle=90, labeldistance=1.1)
plt.axis('equal')
plt.legend(etiquetas)

plt.title("Esaaaaa!!!!")

graficar(window['figCanvas'].TKCanvas, fig)

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Salir':
        break
window.close()



#datos_juego[datos_juego['Partida']==1]['Estado']=='ok'].str[0:10]

#plt.pie(datos_juego['Estado'])

#datos_juego= datos_juego.sort_values('Genero',ascending= False)
#plt.bar(datos_juego['Genero'],color=['b','g','r','p','y'])

#datos_juego[datos_juego['Nombre de evento']=='fin']['Genero'].value_counts()  
