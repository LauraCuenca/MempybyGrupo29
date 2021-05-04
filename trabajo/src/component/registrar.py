import PySimpleGUI as sg
from src.windows import registrar


def start():
    """
    Lanza la ejecución de la ventana del tablero
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana del tablero que capta sus eventos
    """
    window = registrar.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED,"-Exit-","-REGISTRARSE-"):
            break

        #if event == ("-REGISTRARSE-"):
            #Vuelve a la ventana de inicio
            #""" pickle""""

    return window
