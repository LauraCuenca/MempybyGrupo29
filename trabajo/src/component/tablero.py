import os
import PySimpleGUI as sg
from playsound import playsound
from src.component import configuracion
from src.windows import tablero


sonido_boton = os.path.join('src','recursos', 'sonidos', 'click.wav')


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
            playsound(sonido_boton)
            break

        if event == "Configuración":
            playsound(sonido_boton)
            configuracion.start()


    return window
