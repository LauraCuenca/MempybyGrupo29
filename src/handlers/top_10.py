import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from src.handlers import sonido


def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""
    try:
        datos_juego= pd.read_csv('datos_de_partidas.csv')

        top_10 = datos_juego[datos_juego['estado'] == 'ok'].groupby('nro_de_partida')['palabra'].first().value_counts().head(10)
        data = top_10.keys()
        return data
    except OSError:
        return ["Datos insuficientes"]

def iterar(data):
    """ """
    lista_de_listas = []
    for x in range(len(data)):
        lista_de_listas += [[data[x]]]
    return lista_de_listas




def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()

def build():
    """ Crea la ventana para registrar el usuario"""
    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/graficos/top_10.png")],
    [sg.Button("Salir",size=(size),key=("-SALIR-"))]
    ]
    
    top_10 = sg.Window("Grafico",layout=layout,element_justification='c', resizable=False, modal=True)

    return top_10


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = build()

    fig, ax = plt.subplots(1, 1)
    data = obtener_datos()
    data_act = iterar(data)
    column_labels = ['Top 10']
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data_act, colLabels=column_labels, loc="center")
    plt.title("Top 10 de las primeras palabras encontradas")
    plt.savefig("src/recursos/graficos/top_10.png")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break
    return window
