import PySimpleGUI as sg
import json

def config(dificultad,ayuda,tarjeta,tiempo,tema,alerta,cambios):

    """ GUARDO EN UN JSON LOS DATOS """
    archivo = open("archivo.csv", "r", encoding="utf8")
    cvsreader = csv.reader(archivo, delimiter=",")
    encabezado = next(csvreader)
    print(encabezado)
    
    archivo.close()

    print(dificultad,ayuda,tarjeta,tiempo,tema,alerta,cambios)
    if "" in (dificultad,ayuda,tarjeta,tiempo,tema,alerta,cambios):
        sg.popup_error("Debes completar todos los campos")
    else:
        if((dificultad.isalpha()) and (ayuda.isalpha()) and (tarjeta.isalpha()) and (tiempo.isdigit())):
            sg.popup_ok("Campos correctos")
            datos_json = json.dumps(archivo, dificultad,ayuda,tarjeta,tiempo)
            print("archivo exportado")
        else:
            sg.popup_error("Campos incorrectos")

    with open("verificar.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(datos_json)
