import PySimpleGUI as sg
import pickle
#from src.recursos import jugadores

def guardar_reg(jugador):
    """ Guarda el jugador en el archivo"""
    with open("jugadores", 'rb+') as archivo:
        lista_jugador=pickle.load(archivo)
        lista_jugador= lista_jugador.append(jugador) 
        archivo.seek(0, 0)
        pickle.dump(lista_jugador, archivo)


def iniciar_sesion(usuario,cont,conf,genero,edad):
    """ Valida que los campos se llenen correctamente"""
    edad= str(edad)
    print(usuario,cont,conf,genero,edad)
    if "" in (usuario,cont,conf,genero,edad):
        sg.popup_error("Debes completar todos los campos")
    else :
        if((edad.isdigit()) and (genero.isalpha()) and cont==conf):
            sg.SystemTray.notify('Guardado', 'Campos completados correctamente')
 
            jugador= [usuario,cont,genero,edad]
            guardar_reg(jugador)
        else:
            sg.popup_error("Campos completados incorrectamente")
