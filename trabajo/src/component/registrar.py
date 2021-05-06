import PySimpleGUI as sg
from src.windows import registrar
from src.handlers import sonido



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

        if event in (sg.WINDOW_CLOSED,"-Exit-"):
            sonido.reproducir_sonido(1)
            break

        elif event == "-REGISTRARSE-":
            #Vuelve a la ventana de inicio
            """ pickle"""
            print("Guardar esto en pickle:", _values)
            sonido.reproducir_sonido(1)
            break

    return window
