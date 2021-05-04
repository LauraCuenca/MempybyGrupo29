import PySimpleGUI as sg
from src.windows.jugar import build as jugar_build

def start():
    window = loop()
    window = close()


def loop():
    window = jugar_build("Mauro", "Diego")

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break

        if event.startswith("cell"):
            _prefix, x, y = event.split("-")
            print(f"Celda: {x}, {y}")

    return window
