import pickle
import PySimpleGUI as sg
from src.windows import menu


def comparacion(usuario,cont):
    """ Valida los datos para iniciar sesion"""
    try:
        with open("jugadores",'rb') as archivo:
            jugadores= pickle.load(archivo)            
            if (usuario in jugadores) and jugadores[usuario][1]== cont:
                crear_sesion(usuario)  # guarda la sesion del jugador
                return True
            else:
                sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")
                return False
    except FileNotFoundError as e:
        menu.build()
        sg.SystemTray.notify('Error!', 'Debe registrarse', icon="src/recursos/images/exclamation.png")


def crear_sesion(jugador):
    """Crea un archivo con el nombre del jugador logueado"""
    with open("jugador_logueado",'wb') as archivo:
        pickle.dump(jugador, archivo)


def leer_sesion():
    """Lee los datos del jugador logueado"""
    jugador = ""
    with open("jugador_logueado",'rb') as archivo:
        jugador = pickle.load(archivo)
    return jugador

