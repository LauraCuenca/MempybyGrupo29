import PySimpleGUI as sg
from src.handlers import login, configuracion_h


def build():
    """ Crea la ventana cuando de configuracion"""
    tipo_de_tarjetas = ["Texto", "Imagen", "Mixto"]
    dificultad = ["Fácil", "Medio", "Difícil"]
    ayuda = ["Con", "Sin"]
    tema = ["LightGray1", "Topanga", "DarkBlue17"]
    size= (25,2)
    padding= (5, 5), (25, 5)

    jugador_logueado = login.leer_sesion()
    configuraciones = configuracion_h.leer_config()

    layout = [
        [sg.Text(" "*30),sg.Image(filename=("src/recursos/images/configuracion.png"),size=(150,150))],
        [sg.Text("Nivel de Dificultad:", size=(size), pad=(padding)), sg.Combo(dificultad, default_value=configuraciones[jugador_logueado][0], readonly=True, key="-NIVEL_DE_DIFICULTAD-")],
        [sg.Text("Ayuda:", size=(size), pad=(padding)), sg.Combo(ayuda, default_value=configuraciones[jugador_logueado][1], readonly=True, key="-AYUDA-")],
        [sg.Text("Tipo de tarjetas:", size=(size)), sg.Combo(tipo_de_tarjetas, default_value=configuraciones[jugador_logueado][2], readonly=True, key="-TIPO_DE_TARJETAS-")],
        [sg.Text("Tiempo total de partida:",size=(size),pad=(padding)),sg.Spin(list(range(1000)),size=(8,1),key="-TIEMPO_TOTAL_PARTIDA-", initial_value=configuraciones[jugador_logueado][3])],
        [sg.Text("Tema colores:", size=(size)), sg.Combo(tema, default_value=configuraciones[jugador_logueado][4], readonly=True, key="-TEMA_COLOR-")],
        [sg.Text("Mensajes de alerta:"), sg.Input(key="-MENSAJES_ALERTA-", default_text=configuraciones[jugador_logueado][5])],
        [sg.Text(" "*30), sg.Button("Guardar cambios", size=(20,2), key=("-GUARDAR_CAMBIOS-"))]
    ]

    configuracion= sg.Window("Configuración", layout=layout, resizable=False, modal=True)

    return configuracion