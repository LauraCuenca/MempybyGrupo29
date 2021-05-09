import PySimpleGUI as sg

def build():
    """ Crea la ventana cuando se inicia sesion"""
    tipo_de_tarjetas = ["Texto", "Imagen", "Mixto"]
    dificultad = ["Fácil", "Medio", "Difícil"]
    ayuda = ["Con", "Sin"]
    size= (25,2)

    layout = [
        [sg.Text(" "*30),sg.Image(filename=("src/recursos/images/configuracion.png"),size=(150,150))],
        [sg.Text("Nivel de Dificultad:", size=(size), pad=((5, 5), (25, 5))), sg.Combo(dificultad, default_value=dificultad[0], readonly=True)],
        [sg.InputText(key="-NIVEL_DE_DIFICULTAD-", do_not_clear=false)],
        [sg.Text("Ayuda:", size=(size), pad=((5, 5), (25, 5)), sg.Combo(ayuda, default_value=ayuda[0], readonly=True))],
        [sg.InputText(key="-AYUDA-", do_not_clear=false)],
        [sg.Text("Tipo de tarjetas:", size=(size)), sg.Combo(tipo_de_tarjetas, default_value=tipo_de_tarjetas[0], readonly=True)],
        [sg.InputText(key="-TIPO_DE_TARJETAS-", do_not_clear=false)],
        [sg.Text("Tiempo total de partida:", sg.Input(size=(8, 1)))],
        [sg.Input(key="-TIEMPO_TOTAL_PARTIDA-", do_not_clear=false)],
        [sg.Text("Tema:", size=(size)), sg.Input(size=(8, 1))],
        [sg.InputText(key="-TEMA-", do_not_clear=false)],
        [sg.Text("Mensajes de alerta:", sg.Input(size=(8, 1)))],
        [sg.InputText(key="-MENSAJES_ALERTA-", do_not_clear=false)],
        [sg.Text(" "*30),sg.Button("Guardar cambios",size=(20,2),key=("-GUARDAR_CAMBIOS-"))]
    ]

    configuracion= sg.Window("Configuración", layout=layout, size=(480,500), resizable=False, modal=True, disable_minimize=True)

    return configuracion