import pickle
import PySimpleGUI as sg
from src.windows import menu

def comparacion(usuario,cont):
    """ Valida los datos para iniciar sesion"""
    try:
        with open("jugadores",'rb') as archivo:
            jugadores= pickle.load(archivo)
            jugadores_dict = {}
            for jugador in jugadores:
                for usuario, v in jugador.items():
                     jugadores_dict[k] = v
            
            if (usuario in jugadores_dict) and jugadores_dict[usuario][1]== cont:
                    return True
            else:
                sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")
    except FileNotFoundError as e:
        menu.build()
        sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")
        