import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from src.handlers import sonido


def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""

    datos_juego= pd.read_csv('datos_de_partidas.csv')
    
    finalizadas_f= datos_juego[(datos_juego['nivel']=='Facil')&(datos_juego['estado']=='finalizada')]
    nro_facil= finalizadas_f['tiempo_partida'].div(14000000)
    sum_f=nro_facil.sum()

    finalizadas_m= datos_juego[(datos_juego['nivel']=='Medio')&(datos_juego['estado']=='finalizada')]
    nro_medio= finalizadas_m['tiempo_partida'].div(14000000)
    sum_m=nro_medio.sum()

    finalizadas_d= datos_juego[(datos_juego['nivel']=='Dificil')&(datos_juego['estado']=='finalizada')]
    nro_dif= finalizadas_d['tiempo_partida'].div(14000000)
    sum_d=nro_dif.sum()


    data_dibujo = [int(sum_f),int(sum_m),int(sum_d)]
    etiquetas = ['Facil','Medio','Dificil']
    return etiquetas, data_dibujo




def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()

def build():
    """ Crea la ventana para registrar el usuario"""
    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/graficos/promedio_tiempo.png")],
    [sg.Button("Salir",size=(size),key=("-SALIR-"))]
    ]
    
    grafico_genero = sg.Window("Grafico",layout=layout,element_justification='c', resizable=False, modal=True)

    return grafico_genero


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = build()

    etiquetas, data_dibujo = obtener_datos()

    fig = plt.figure()
    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.2f%%',explode=None,
            shadow=True, startangle=90, labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Promedio de tiempo de partidas finalizadas por nivel")
    plt.savefig("src/recursos/graficos/promedio_tiempo.png")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break
    return window