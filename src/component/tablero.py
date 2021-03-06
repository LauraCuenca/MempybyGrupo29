import time

import PySimpleGUI as sg
from src.component import configuracion, estadisticas_c, ranking_c, acerca_de
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
    configuraciones = configuracion_h.leer_config()
    datos_de_jugador_logueado = login.listar_jugadores()[jugador_logueado]  # Todos los datos del jugador logueado
    nueva_partida = 0
    tiempo_espera_tarjeta = 0

    while True:
        event, values = window.read(timeout=100)
        tiempo_actual = time.time()  # Actualiza tiempo actual

        window["-P1-"].update(f"Jugador: {jugador_logueado}")
        if nueva_partida:
            if not nueva_partida.hay_fin_del_juego():
                nueva_partida.tiempo_restante = round(nueva_partida.tiempo_maximo - (
                        tiempo_actual - nueva_partida.tiempo_de_inicio))
                window["-TIEMPO_RESTANTE-"].update(f"|    Tiempo restante: {nueva_partida.tiempo_restante}")
                window["-DESCRIPCION_PARTIDA-"].update(nueva_partida.descripcion)
            else:
                if nueva_partida.aciertos == nueva_partida.aciertos_maximos:  # Si ganaste
                    msj = configuraciones[jugador_logueado][5].split(',')
                    if len(msj) >= 1:
                        sg.popup(msj[0], title="fin", image="src/recursos/images/winner.png")  # Mostrar primer mensaje
                    else:
                        sg.popup("Ganaste el juego!!", title="fin", image="src/recursos/images/winner.png")
                else:
                    msj = configuraciones[jugador_logueado][5].split(',')
                    if len(msj) >= 2:
                        sg.popup(msj[1], title="fin", image="src/recursos/images/game-over.png")  # Mostrar segundo mensaje
                    else:
                        sg.popup("Perdiste el juego", title="fin", image="src/recursos/images/game-over.png")
                nueva_partida = 0

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Cerrar sesión"):
            if nueva_partida:
                nueva_partida.guardar_datos('fin', 'abandono', '')
            nueva_partida = 0  # Si se cambia la configuracion, se reinicia la partida
            tiempo_espera_tarjeta = 0
            sonido.reproducir_sonido(1)
            break

        if event == "Estadisticas":
            sonido.reproducir_sonido(1)
            if nueva_partida:
                nueva_partida.guardar_datos('fin', 'abandono', '')
            nueva_partida = 0  # Si se cambia la configuracion, se reinicia la partida
            tiempo_espera_tarjeta = 0
            estadisticas_c.start()

        if event == "Ranking":
            sonido.reproducir_sonido(1)
            if nueva_partida:
                nueva_partida.guardar_datos('fin', 'abandono', '')
            nueva_partida = 0  # Si se cambia la configuracion, se reinicia la partida
            tiempo_espera_tarjeta = 0
            ranking_c.start()

        if event == "Acerca de":
            sonido.reproducir_sonido(1)
            acerca_de.start()

        if event == "Configuración":
            sonido.reproducir_sonido(1)
            configuracion.start()
            window.close()
            configuraciones = configuracion_h.leer_config()
            sg.theme(configuraciones[jugador_logueado][4])
            if nueva_partida:
                nueva_partida.guardar_datos('fin', 'abandono', '')
            nueva_partida = 0  # Si se cambia la configuracion, se reinicia la partida
            tiempo_espera_tarjeta = 0
            window = tablero.build()

        if event == "Nueva partida":
            resp = sg.popup_ok_cancel("¿Iniciar nueva partida?")
            if resp == "OK":
                config = configuracion_h.leer_config()[login.leer_sesion()]
                nueva_partida = juego.Juego(config[0], config[1], config[2], jugador_logueado,
                                            datos_de_jugador_logueado[2], datos_de_jugador_logueado[3])
                nueva_partida.generar_tablero()

                for x in range(len(nueva_partida.matriz_tablero)):  # Limpia tablero
                    for y in range(len(nueva_partida.matriz_tablero[x])):
                        window[f"-CELL-{x}-{y}-"].update(
                            text="",
                            image_filename="src/recursos/datasets/images_pokemon/images/vacio.png")

        if "-CELL-" in event and nueva_partida and not tiempo_espera_tarjeta and not nueva_partida.hay_fin_del_juego():
            # Verifica que tarjeta se apreto
            x = int(event.split("-")[2])
            y = int(event.split("-")[3])
            palabra, imagen = nueva_partida.revelar_tarjeta(x, y)
            window["-AYUDA-"].update(nueva_partida.texto_ayuda)
            window[event].update(text=palabra, image_filename=imagen)
            if imagen == "src/recursos/datasets/images_pokemon/images/vacio.png":  # Si es texto ajusta size boton
                window[event].set_size(size=(98, 110))
            if not nueva_partida.hay_acierto():
                if nueva_partida.get_tarjetas_boca_arriba() >= 2:
                    tiempo_espera_tarjeta = time.time() + 1  # Agrega X secs de espera antes de voltear

        if nueva_partida and tiempo_espera_tarjeta and tiempo_actual > tiempo_espera_tarjeta:
            for t in nueva_partida.esconder_tarjetas():  # Voltear tarjetas
                window[f"-CELL-{t[0]}-{t[1]}-"].update(
                    text="",
                    image_filename="src/recursos/datasets/images_pokemon/images/vacio.png")
            tiempo_espera_tarjeta = 0

    return window
