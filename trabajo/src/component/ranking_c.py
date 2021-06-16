import PySimpleGUI as sg
from src.windows import ranking
from src.handlers import sonido, ranking_h



def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = ranking.build()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break

        if event == "-RANKING-":
            window.hide()
            sonido.reproducir_sonido(1)
            ranking_h()
            window.un_hide()

    return window
