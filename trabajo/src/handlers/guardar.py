import PySimpleGUI as sg
import json

def config(dificultad,ayuda,tarjeta,tiempo,color,alerta):
    """ Guarda la configuracion del usuario en un archivo json"""
    datos_config = [dificultad,ayuda,tarjeta,tiempo,color,alerta]
    
    sg.popup_ok("Campos correctos")
    datos_json = json.dumps(datos_config)


    with open("configuracion.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(datos_json)

