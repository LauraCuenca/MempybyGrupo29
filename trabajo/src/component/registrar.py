import PySimpleGUI as sg
import pickle
import string
from src.windows import registrar
from src.handlers import sonido

def iniciar_sesion(usuario,cont,conf,genero,edad):
    print(usuario,cont,conf,genero,edad)
    if "" in (usuario,cont,conf,genero,edad):
        sg.popup_error("Debes completar todos los campos")
    else :
        if((edad.isdigit()) and (genero.isalpha())):
            sg.popup_ok("Campos completados correctamente")
            pickle_data= pickle.dumps(usuario,cont,genero,edad)
        else:
            sg.popup_error("Campos completados incorrectamente")
      
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
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED,"-Exit-","-REGISTRARSE"):
            sonido.reproducir_sonido(1)
            break

        elif event == "-REGISTRARSE-":
            iniciar_sesion(values["-NOMBRE_USUARIO-"],values["-CONT-"],values["-CONF_CONT-"],values["-GENERO-"],values["-EDAD-"])
            sonido.reproducir_sonido(1)

    return window
