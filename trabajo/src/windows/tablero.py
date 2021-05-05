import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú del juego
    """
    menu_def = [
        ['&Archivo', ['Nueva partida', '!Ranking', '!Estadisticas', '---', 'Cerrar sesión']],
        ['&Configuración', ['Configuración', '!Ayuda', '---', '!Acerca de']],
    ]

    layout = [
        [sg.Menu(menu_def, pad=((100, 100), 20))],
        [sg.Text('Jugador 1: ' + "Juanito", key='-P1-'), sg.Text('|    Tiempo restante: 9', key='-P2-')],
        [],
        [sg.Text('')]
    ]

    for y in range(6):
        layout += [
            [sg.Button(' ', size=(8, 4), key=f"cell-{x}-{y}") for x in range(8)]
        ]

    board = sg.Window('Mempy').Layout(layout)

    return board