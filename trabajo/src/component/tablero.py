import PySimpleGUI as sg
from src.component import configuracion
from src.windows import tablero
from src.handlers import sonido, login, configuracion_h, juego


def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    jugador_logueado = login.leer_sesion()
    configuraciones = configuracion_h.leer_config()
    sg.theme(configuraciones[jugador_logueado][4])
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = tablero.build()
    jugador_logueado = login.leer_sesion()  # Nombre del jugador logueado
    nueva_partida = 0

    while True:
        event, _values = window.read(timeout=100)
        window["-P1-"].update(f"Jugador: {jugador_logueado}")
        if nueva_partida:
            window["-TIEMPO_RESTANTE-"].update(f"|    Tiempo restante: {nueva_partida.tiempo_restante}")
            window["-DESCRIPCION_PARTIDA-"].update(nueva_partida.descripcion)

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Cerrar sesión"):
            sonido.reproducir_sonido(1)
            break

        if event == "Configuración":
            sonido.reproducir_sonido(1)
            configuracion.start()
            window.close()
            configuraciones = configuracion_h.leer_config()
            sg.theme(configuraciones[jugador_logueado][4])
            window = tablero.build()
        if event == "Nueva partida":
            ok = sg.popup_ok_cancel("¿Iniciar nueva partida?")
            if ok:
                config = configuracion_h.leer_config()[login.leer_sesion()]
                nueva_partida = juego.Juego(config[0], True, False, jugador_logueado, 'M', 30, 1)
                nueva_partida.generar_tablero()
                for x in range(len(nueva_partida.matriz_tablero)):
                    for y in range(len(nueva_partida.matriz_tablero[x])):
                        print(nueva_partida.matriz_tablero[x][y])
                        window[f"-CELL-{x}-{y}-"].update(
                            image_filename=f"src/recursos/datasets/images_pokemon/images/{nueva_partida.matriz_tablero[x][y][2]}.png")

    return window
