import PySimpleGUI as sg
from src.windows import configuracion
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
    window = configuracion.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-SALIR-"):
            break

        if event == "-NIVEL_DE_DIFICULTAD-":
            pass
            
        if event == "-TIPO_DE_TARJETA-":
        
            if opc == "Texto":
                pass
        
            if opc == "Imagen":
                pass
        
        if event == "-GUARDAR_CAMBIOS-":
            pass
            
    return window
