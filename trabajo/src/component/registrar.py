import PySimpleGUI as sg
from src.windows import registrar
from src.handlers import sonido
from src.handlers import validar

def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = registrar.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED,"-Exit-","-REGISTRARSE"):
            sonido.reproducir_sonido(1)
            break

        elif event == "-REGISTRARSE-":
            validar.iniciar_sesion(values["-NOMBRE_USUARIO-"],values["-CONT-"],values["-CONF_CONT-"],values["-GENERO-"],values["-EDAD-"])
            sonido.reproducir_sonido(1)

    return window
