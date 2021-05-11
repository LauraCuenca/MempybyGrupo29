import PySimpleGUI as sg
import pickle
#from src.recursos import jugadores

def guardar_reg(lista_jugador):
    """ Guarda el registro en el archivo"""
    with open("jugadores", 'wb') as archivo:  #probar append, osea ab, o rb+,0 ab+
        pickle.dump(lista_jugador, archivo)

def agregar_jugador(jugador):
    """ Agrega el nuevo jugador a la lista y llama a la funcion guardar """
    lista_jugador=[]
    lista_jugador.append(jugador)
     #Llamamos a la funcion para guardar los temas
    guardar_reg(lista_jugador)

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
            agregar_jugador(jugador)

        else:
            sg.popup_error("Campos completados incorrectamente")
      