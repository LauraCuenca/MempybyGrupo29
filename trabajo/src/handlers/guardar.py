import PySimpleGUI as sg
import json

def config(dificultad,ayuda,tarjeta,tiempo,color,alerta):

    print(dificultad,ayuda,tarjeta,tiempo,color,alerta)
    
    sg.popup_ok("Campos correctos")
    datos_json = json.dumps(dificultad,ayuda,tarjeta,tiempo,color,alerta)


    with open("configuracion.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(datos_json)
