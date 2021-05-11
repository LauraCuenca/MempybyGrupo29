import PySimpleGUI as sg
import json
from src.windows import configuracion
from src.windows import tablero
from src.handlers import sonido
from src.handlers import verificar


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

        elif event == "-CONFIGURACION-":
            verificar.config(values["-NIVEL_DE_DIFICULTAD-"], values["-AYUDA-"], values["TIPO_DE_TARJETAS"],
                                     values["TIEMPO_TOTAL_PARTIDA"], values["-TEMA-"], values["-MENSAJES_ALERTA-"],
                                     values["-GUARDAR_CAMBIOS-"])
            sonido.reproducir_sonido(1)
            
    return window
