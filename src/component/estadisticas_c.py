import PySimpleGUI as sg
from src.windows import estadisticas
from src.handlers import grafico_estado, grafico_genero, promedio_tiempo, sonido, top_10,timeout



def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = estadisticas.build()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break

        if event == "-TOP_10-":
            window.hide()
            sonido.reproducir_sonido(1)
            top_10.start()
            window.un_hide()

        if event == "-GRAFICO_P_TERM-":
            window.hide()
            sonido.reproducir_sonido(1)
            grafico_estado.start()
            window.un_hide()

        if event == "-GRAFICO_GENERO-":
            window.hide()
            sonido.reproducir_sonido(1)
            grafico_genero.start()
            window.un_hide()

        if event == "-PROMEDIO_PARTIDAS-":
            window.hide()
            sonido.reproducir_sonido(1)
            promedio_tiempo.start()
            window.un_hide()
            
        if event == "-PORCENTAJE_PALABRAS-":
            window.hide()
            sonido.reproducir_sonido(1)
            timeout.start()
            window.un_hide()

    return window
