import PySimpleGUI as sg
from src.windows import register


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
    window = register.reg_ventana()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event == "-GUARDAR_CAMBIOS-"):
            """ pickle""""

    return window
