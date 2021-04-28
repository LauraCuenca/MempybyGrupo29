import PySimpleGUI as sg                        # Part 1 - The import

sg.theme("Topanga")

# Define the window's contents
layout = [
    [sg.Text(" "*32), sg.Image("user_jester.png")],
    [sg.Text("Usuario")],     # Part 2 - The Layout
    [sg.Input()],
    [sg.Text("Contraseña")],
    [sg.Input()],
    [sg.Text(" "*25), sg.Button('Iniciar sesión', pad=((5, 5), (25, 5)))],
    [sg.Text(" "*26), sg.Button('Registrarse', pad=((5, 5), (10, 5)))]
]

generos = ["Femenino", "Masculino", "Otro?"]


layout = [
    [sg.Text(" "*32), sg.Image("user_add.png")],
    [sg.Text("Nombre de Usuario *")],
    [sg.Input()],
    [sg.Text("Contraseña *")],
    [sg.Input()],
    [sg.Text("Confirmar contraseña *")],
    [sg.Input()],
    [sg.Text("Genero *")],
    [sg.Combo(generos, default_value=generos[0], readonly=True)],
    [sg.Text("Edad *")],
    [sg.Input(size=(8, 1))],
    [sg.Text(" "*26), sg.Button('Registrarse', pad=((5, 5), (20, 5)))]
]

tipo_de_tarjetas = ["Texto", "Imagen"]

layout = [
    [sg.Text(" "*28), sg.Image("cog.png")],
    [sg.Text("Cantidad de casillas:", size=(25, 1), pad=((5, 5), (25, 5))), sg.Input(size=(8, 1), pad=((5, 5), (25, 5)))],
    [sg.Text("Cantidad de coincidencias:", size=(25, 1)), sg.Input(size=(8, 1))],
    [sg.Text("Tipo de tarjetas:", size=(25, 1)), sg.Combo(tipo_de_tarjetas, default_value=tipo_de_tarjetas[0], readonly=True)],
    [sg.Text("Tiempo de partida [segundos]:", size=(25, 1)), sg.Input(size=(8, 1))],
    [sg.Text(" "*18), sg.Button('Guardar cambios', pad=((5, 5), (35, 5)))]
]

headings = ["Nombre", "Puntaje"]
ranking = [["Jugador1", 10], ["Jugador2", 8], ["Jugador3", 3]]

layout = [
    [sg.Text(" "*14), sg.Image("pedestal.png", pad=((5, 5), (5, 25)))],
    [sg.Text("Ranking de jugadores")],
    [sg.Table(ranking, headings=headings,  display_row_numbers=True, row_height=20, auto_size_columns=True)],
    [sg.Text(" "*14), sg.Button('Volver', pad=((5, 5), (35, 5)))]
]


menu_def = [
    ['&Archivo', ['Nueva partida', 'Ranking', 'Estadisticas', '---', 'Salir']],
    ['Configuracion', ['Configuracion', 'Ayuda', '---', 'Acerca de']],
]


layout = [
        [sg.Menu(menu_def, pad=((100, 100), 20))],
        [sg.Text('Jugador 1: ' + "Juanito", key='-P1-'), sg.Text('|    Tiempo restante: 9', key='-P2-')],
        [],
        [sg.Text('')]
    ]

for y in range(6):
    layout += [
        [sg.Button(' ', size=(8, 4), key=f"cell-{x}-{y}") for x in range(6)]
    ]




# Create the window
window = sg.Window('Inicio de Sesión', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print(values)

# Finish up by removing from the screen
window.close()

