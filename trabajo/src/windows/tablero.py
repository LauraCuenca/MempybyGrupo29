import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú del juego
    """
    menu_def = [
        ['&Archivo', ['Nueva partida', 'Ranking', 'Estadisticas', '---', 'Salir']],
        ['Configuracion', ['Configuracion', 'Ayuda', '---', 'Acerca de']],
    ]
    layout = [
        [sg.Button('Jugar', size=(50, 2), key="-play-")],
        [sg.Button('Configuración', size=(50, 2), key="-settings-")],
        [sg.Button('Score', size=(50, 2), key="-score-")],
        [sg.Button('Salir', size=(50, 2), key="-exit-")]
    ]

    board = sg.Window('Ta Te Ti').Layout(layout)

    return board