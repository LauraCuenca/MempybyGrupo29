import PySimpleGUI as sg

def build():
    """ Crea la ventana cuando se inicia sesion"""
    tipo_de_tarjetas = ["Texto", "Imagen"]
    dificultad = ["Fácil", "Medio", "Difícil"]
    size= (25,2)

    layout = [
        [sg.Text(" "*30),sg.Image(filename=("src/recursos/images/configuracion.png"),size=(150,150))],
        [sg.Text("Nivel de Dificultad:", size=(size), pad=((5, 5), (25, 5))), sg.Combo(dificultad, default_value=dificultad[0], readonly=True)],
        [sg.Text("Tema:", size=(size)), sg.Input(size=(8, 1))],
        [sg.Text("Tipo de tarjetas:", size=(size)), sg.Combo(tipo_de_tarjetas, default_value=tipo_de_tarjetas[0], readonly=True)],
        [sg.Text(" "*30),sg.Button("Guardar cambios",size=(20,2),key=("-GUARDAR_CAMBIOS-"))]
    ]

    configuracion= sg.Window("Configuración", layout=layout, size=(480,500), resizable=False, modal=True, disable_minimize=True)

    return configuracion