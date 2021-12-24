import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from src.handlers import sonido


def obtener_datos():
    """ Filtro los datos que se quieren obtener del csv"""
    try:
        datos_juego = pd.read_csv('datos_de_partidas.csv')
        timeout = datos_juego[datos_juego["estado"] == 'timeout']['nro_de_partida'].values.tolist()
        # palabras= datos_juego[datos_juego["nro_de_partida"]==int(partidas_timeout)]['palabra'].dropna()

        df2 = datos_juego[datos_juego['nro_de_partida'].isin(timeout)].dropna()
        cant = df2['palabra'].value_counts()
        palabras = df2['palabra'].unique()

        # cant= palabras.value_counts()
        data_dibujo = list(cant)
        etiquetas = list(palabras)
        if len(data_dibujo) == 0:
            data_dibujo = [1]
            etiquetas = ["Datos insuficientes"]
        return etiquetas, data_dibujo
    except OSError:
        return ["Datos insuficientes"], [1]


def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()


def build():
    """ Crea la ventana para registrar el usuario"""
    size = (15, 2)

    layout = [
        [sg.Image(filename="src/recursos/graficos/grafico_timeout.png")],
        [sg.Button("Salir", size=(size), key=("-SALIR-"))]
    ]

    grafico_genero = sg.Window("Grafico", layout=layout, element_justification='c', resizable=False, modal=True)

    return grafico_genero


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = build()

    etiquetas, data_dibujo = obtener_datos()

    fig = plt.figure()
    plt.pie(data_dibujo, labels=etiquetas, autopct='%1.2f%%', explode=None, shadow=True, startangle=90,
            labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas)
    plt.title("Porcentaje de palabras en partidas Timeout")
    plt.savefig("src/recursos/graficos/grafico_timeout.png")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "-SALIR-"):
            sonido.reproducir_sonido(1)
            break
    return window
