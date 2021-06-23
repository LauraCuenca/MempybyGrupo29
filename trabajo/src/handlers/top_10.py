import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def graficar(canvas, figure, ax):
    """ Arma la figura """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas, ax)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""

    datos_juego= pd.read_csv('datos_de_partidas.csv')

    top_10 = datos_juego[datos_juego["estado"]=='ok']['palabra'].head(10)
    list_nombres= list(top_10.values)
    data = list_nombres
    return data

def iterar(data):

    for x in data:
        lista_de_listas= [[data[0]],[data[1]],[data[2]],[data[3]]]
    return lista_de_listas


layout = [[sg.Canvas(key='figCanvas')],
    [sg.Button('Salir')]]

window = sg.Window('Grafico',layout,finalize=True,resizable=True,element_justification="center")
   

fig, ax =plt.subplots(1,1)
data= obtener_datos()
data_act=iterar(data)
column_labels= ['Top 10']
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data_act,colLabels=column_labels,loc="center")
plt.title("Top 10 de las primeras palabras encontradas")


graficar(window['figCanvas'].TKCanvas, fig, ax)


while True:
     event, values = window.read(timeout=200)
     if event == sg.WIN_CLOSED or event == 'Salir':
        break
window.close()