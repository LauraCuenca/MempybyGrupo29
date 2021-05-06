import os
import PySimpleGUI as sg
from playsound import playsound
from src.windows import registrar


sonido_boton = os.path.join(os.getcwd(), 'src/recursos/sonidos/click.wav')


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
            playsound(sonido_boton)
            break

        elif event == "-REGISTRARSE-":
            #Vuelve a la ventana de inicio
            """ pickle"""
            print("Guardar esto en pickle:", _values)
            playsound(sonido_boton)
            break

    return window
