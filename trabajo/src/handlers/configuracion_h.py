import json
import PySimpleGUI as sg
from src.handlers import login


def config(dificultad,ayuda,tarjeta,tiempo,color,alerta):
    """ Guarda la configuracion del usuario en un archivo json"""
    datos_config = [dificultad,ayuda,tarjeta,tiempo,color,alerta]
    
    tiempo = str(tiempo)
    if (tiempo.isdigit()):
        configuraciones = leer_config()  # Carga todas las configuraciones
        jugador_logueado = login.leer_sesion()
        configuraciones[jugador_logueado] = datos_config  # Actualiza las configuraciones del usuario
        datos_json = json.dumps(configuraciones)  
        # Guarda la configuracion en un json
        with open("configuracion.json", "w", encoding="utf8") as archivoJSON:
            archivoJSON.write(datos_json)
        sg.SystemTray.notify('Éxito!', 'Cambios guardados')


def leer_config():
    """Devuelve todas las configuraciones guardadas"""
    configuraciones = {}
    with open("configuracion.json", "r", encoding="utf8") as archivoJSON:
        configuraciones = json.load(archivoJSON)
    #print(configuraciones)
    return configuraciones


def crear_configuracion_default(usuario):
    """Crea la configuracion default cuando el jugador se registra"""
    try:
        configuraciones = leer_config()
    except Exception:
        # Si el archivo no existe
        configuraciones = {}
    configuraciones[usuario] = ["Fácil", "Con", "Texto", "60", "Topanga", "Ganaste, Perdiste"]
    datos_json = json.dumps(configuraciones)  
    # Guarda la configuracion en un json
    with open("configuracion.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(datos_json)
