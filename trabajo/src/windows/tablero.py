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
        [sg.Text('Jugador: ', key='-P1-', size=(20, 1)), sg.Text('|    Tiempo restante: 9', key='-TIEMPO_RESTANTE-')],
        [],
        [sg.Text('')]
    ]

    for y in range(3):
        layout += [
            [sg.Button(' ', size=(16, 8), image_filename="src/recursos/datasets/images_pokemon/images/pikachu.png",
                       key=f"-CELL-{x}-{y}-") for x in range(4)]
        ]

    board = sg.Window('Mempy').Layout(layout)

    return board
