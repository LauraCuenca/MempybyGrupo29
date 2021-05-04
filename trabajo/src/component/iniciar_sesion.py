import PySimpleGUI as sg
from src.windows import iniciar_sesion
from src.windows import tablero


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
    window = iniciar_sesion.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-SALIR-"):
            break

       # if event == "-TEMA-":
          

        #if event == "-TIPO_DE_TARJETA-":
            #if opc == 
        #if event == "-JUGAR-":
            #tablero.

    return window