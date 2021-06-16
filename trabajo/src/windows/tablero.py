import PySimpleGUI as sg
from src.handlers import configuracion_h, login


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

    config = configuracion_h.leer_config()[login.leer_sesion()]
    if config[0] == "Fácil":
        tamanio = (4, 2)  # Tamaño x,y del tablero segun la dificultad
    elif config[0] == "Medio":
        tamanio = (4, 3)
    else:
        tamanio = (4, 4)
    for y in range(tamanio[1]):
        layout += [
            [sg.Button(' ', size=(16, 8), key=f"-CELL-{x}-{y}-") for x in range(tamanio[0])]
        ]

    board = sg.Window('Mempy').Layout(layout)

    return board
