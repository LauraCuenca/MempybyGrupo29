import PySimpleGUI as sg

def build():
    """ Crea la ventana cuando se inicia sesion"""
    tipo_de_tarjetas = ["Texto", "Imagen"]

    layout = [
        #[sg.Text(" "*28), sg.Image("cog.png")],
        [sg.Text("Nivel de Dificultad:", size=(25, 1), pad=((5, 5), (25, 5))), sg.Input(size=(8, 1), pad=((5, 5), (25, 5)))],
        [sg.Text("Tema:", size=(25, 1)), sg.Input(size=(8, 1))],
        [sg.Text("Tipo de tarjetas:", size=(25, 1)), sg.Combo(tipo_de_tarjetas, default_value=tipo_de_tarjetas[0], readonly=True)],
        [sg.Text(" "*18), sg.Button("Jugar", pad=((5, 5), (35, 5)))]
    ]

    iniciar_sesion = sg.Window("Mempy. byGrupo29",layout= layout, size=(480,500),element_justification='c')

    return iniciar_sesion 