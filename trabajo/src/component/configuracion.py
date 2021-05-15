import json
import PySimpleGUI as sg
from src.windows import configuracion
from src.handlers import sonido, configuracion_h


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
    window = configuracion.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-CONFIGURACION-"):
            sonido.reproducir_sonido(1)
            break

        elif event == "-GUARDAR_CAMBIOS-":
            configuracion_h.config(values["-NIVEL_DE_DIFICULTAD-"], values["-AYUDA-"], values["-TIPO_DE_TARJETAS-"], 
                           values["-TIEMPO_TOTAL_PARTIDA-"], values["-TEMA_COLOR-"], values["-MENSAJES_ALERTA-"])
            sonido.reproducir_sonido(1)
            break
            
    return window
