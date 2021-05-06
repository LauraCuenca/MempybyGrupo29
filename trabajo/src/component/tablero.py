import PySimpleGUI as sg
from src.component import configuracion
from src.windows import tablero
from src.handlers import sonido



def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = tablero.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Cerrar sesión"):
            sonido.reproducir_sonido(1)
            break

        if event == "Configuración":
            sonido.reproducir_sonido(1)
            configuracion.start()


    return window
