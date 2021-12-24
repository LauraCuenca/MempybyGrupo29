import PySimpleGUI as sg
from src.windows import registrar
from src.handlers import sonido, registrar_h



def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = registrar.build()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break

        elif event == "-REGISTRARSE-":
            if (registrar_h.validar(values["-NOMBRE_USUARIO-"],values["-CONT-"],values["-CONF_CONT-"],values["-GENERO-"],values["-EDAD-"])):
                sonido.reproducir_sonido(1)
                break

    return window

