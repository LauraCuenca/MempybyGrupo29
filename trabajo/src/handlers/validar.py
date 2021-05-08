import PySimpleGUI as sg
import pickle

def iniciar_sesion(usuario,cont,conf,genero,edad):
    edad= str(edad)
    print(usuario,cont,conf,genero,edad)
    if "" in (usuario,cont,conf,genero,edad):
        sg.popup_error("Debes completar todos los campos")
    else :
        if((edad.isdigit()) and (genero.isalpha()) and cont==conf):
            sg.popup_ok("Campos completados correctamente")
            pickle_data= pickle.dumps(usuario,cont,genero,edad)
        else:
            sg.popup_error("Campos completados incorrectamente")
      