import PySimpleGUI as sg
from src.component import configuracion
from src.windows import tablero
from src.handlers import sonido, login, configuracion_h



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


    while True:
        event, _values = window.read()
        window["-P1-"].update(f"Jugador: {jugador_logueado}")

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


    return window
