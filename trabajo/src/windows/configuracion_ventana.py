import PySimpleGUI as sg

def jugar_build():
    """
    Construye la ventana del menú del juego
    """
    size = (50, 2)
    layout = [
        [sg.Button('Jugar', size=size, key="-play-")],
        [sg.Button('Configuración', size=size, key="-settings-")],
        [sg.Button('Puntaje', size=size, key="-score-")],
        [sg.Button('Salir', size=size, key="-exit-")]
    ]

    board = sg.Window('mempy').Layout(layout)

    return board
