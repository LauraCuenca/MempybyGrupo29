import PySimpleGUI as sg
import pickle
from src.handlers import configuracion_h


def archivo_existe(jugador):
    """
    Verifica si el archivo exite, en caso contrario lo crea
    {'diego': ['diego', '123', 'm', '30'], 'mauro': ['mauro', '123', 'm', '32']}
    """
    try:
        with open("jugadores", 'rb') as archivo:
            lista_jugador= pickle.load(archivo)
    except FileNotFoundError as e:
        lista_jugador = {}
    finally:
        lista_jugador[jugador[0]] = jugador
        with open("jugadores", 'wb') as archivo:
            pickle.dump(lista_jugador, archivo)


def jugador_existe(jugador):
    """Verifica si el usuario ya existe"""
    try:
        with open("jugadores", 'rb') as archivo:
            lista_jugador= pickle.load(archivo)
        print(lista_jugador)
        return (jugador in lista_jugador)
    except FileNotFoundError as e:
        return False


def validar(usuario,cont,conf,genero,edad):
    """ Valida que los campos del registro se llenen correctamente"""
    edad= str(edad)
    if "" in (usuario,cont,conf,genero,edad):
        sg.SystemTray.notify('Error!', 'Debes completar todos los campos', icon="src/recursos/images/exclamation.png")
        return False
    else:
        if (jugador_existe(usuario)):
            sg.SystemTray.notify('Error!', 'Ese usuario ya existe', icon="src/recursos/images/exclamation.png")
            return False
        if((edad.isdigit()) and (genero.isalpha()) and cont==conf):
            jugador= [usuario,cont,genero,edad]
            archivo_existe(jugador)
            configuracion_h.crear_configuracion_default(usuario)
            sg.SystemTray.notify('Guardado...', 'Campos completados correctamente')
            return True
        else:
            sg.SystemTray.notify('Error!', 'Campos completados incorrectamente', icon="src/recursos/images/exclamation.png")
            return False

