import PySimpleGUI as sg
import pickle
import os



def archivo_existe(jugador):
    """Verifica si el archivo exite, en caso contrario lo crea"""
    try:
        with open("jugadores", 'rb+') as archivo:
            guardar_reg(jugador)   
    except FileNotFoundError as e:
        arch= open("jugadores", 'xb')
        cargar_jug(jugador)


def cargar_jug(lista_jugador):
    """ Carga el nuevo jugador"""
    with open("jugadores",'wb') as arch:
        pickle.dump(lista_jugador, arch)


def guardar_reg(jugador):
    """ Guarda el jugador en el archivo"""
    with open("jugadores", 'rb') as archivo:
        lista_jugador= pickle.load(archivo)
        print(lista_jugador)
        lista_jugador.append(jugador)
        cargar_jug(lista_jugador)


def iniciar_sesion(usuario,cont,conf,genero,edad):
    """ Valida que los campos se llenen correctamente"""
    edad= str(edad)
    print(usuario,cont,conf,genero,edad)
    if "" in (usuario,cont,conf,genero,edad):
        sg.SystemTray.notify('Error!', 'Debes completar todos los campos', icon="src/recursos/images/exclamation.png")
    else:
        if((edad.isdigit()) and (genero.isalpha()) and cont==conf):
            jugador= [usuario,cont,genero,edad]
            archivo_existe(jugador)
            sg.SystemTray.notify('Guardado...', 'Campos completados correctamente')
        else:
            sg.SystemTray.notify('Error!', 'Campos completados incorrectamente', icon="src/recursos/images/exclamation.png")

