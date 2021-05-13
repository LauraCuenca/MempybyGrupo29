import pickle
import PySimpleGUI as sg
from src.windows import menu

def comparacion(usuario,cont):
    """ Valida los datos para iniciar sesion"""
    try:
        with open("jugadores",'rb') as archivo:
            jugadores= pickle.load(archivo)
            if usuario in jugadores and jugadores[0][1]== cont:
                return True
            else:
                sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")
    except FileNotFoundError as e:
        menu.build()
        sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")
        