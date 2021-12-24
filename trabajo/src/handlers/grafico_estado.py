import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from src.handlers import sonido

def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""
    try:
        datos_juego= pd.read_csv('datos_de_partidas.csv')

        try:
            partidas_aband = datos_juego['estado'].str.contains('abandono').value_counts()[True]
        except:
            partidas_aband = 0
        try:
            partidas_cancel = datos_juego['estado'].str.contains('finalizada').value_counts()[True]
        except:
            partidas_cancel = 0
        try:
            partidas_finalizadas= datos_juego['estado'].str.contains('finalizada').value_counts()[True]
        except:
            partidas_finalizadas = 0
        etiquetas = ["Abandonada", "Cancelada", "Terminada"]
        data_dibujo = [partidas_aband, partidas_cancel, partidas_finalizadas]
        return etiquetas, data_dibujo
    except OSError:
        return ["Datos insuficientes", "Datos insuficientes", "Datos insuficientes"], [1, 1, 1]


def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()

def build():
    """ Crea la ventana para registrar el usuario"""
    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/graficos/grafico_estado.png")],
    [sg.Button("Salir",size=(size),key=("-SALIR-"))]
    ]
    
    grafico_estado = sg.Window("Grafico",layout=layout,element_justification='c', resizable=False, modal=True)

    return grafico_estado


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = build()

    etiquetas, data_dibujo = obtener_datos()

    explode = (0, 0, 0)
    fig = plt.figure()
    plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%',
            shadow=True, startangle=90, labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Porcentaje de Partidas por Estado")
    plt.savefig("src/recursos/graficos/grafico_estado.png")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break
    return window
