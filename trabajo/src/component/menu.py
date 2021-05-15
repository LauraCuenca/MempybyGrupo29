import PySimpleGUI as sg
from src.windows import menu
from src.component import registrar, tablero
from src.handlers import sonido, login


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
    window = menu.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir", "-SALIR-", "-EXIT-"):
            sonido.reproducir_sonido(1)
            break

        if event == "-REGISTER-":
            window.hide()
            sonido.reproducir_sonido(1)
            registrar.start()
            window.un_hide()

        if event == "-INICIAR_SESION-":
            if (login.comparacion(values["-USUARIO-"],values["-CONT-"])):
                sonido.reproducir_sonido(1)
                window.hide()
                tablero.start()
                window.un_hide()
            
    
    return window
