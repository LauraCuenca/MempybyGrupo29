import PySimpleGUI as sg

def register ():
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
    [sg.Input()],
    [sg.Text("Edad *")],
    [sg.Input(size=(8, 1))],
    [sg.Text(" "*26), sg.Button('Registrarse', pad=((5, 5), (20, 5)))]
    ]
 
    

def first_window():
    tipo_de_tarjetas = ["Texto", "Imagen"]

layout = [
    [sg.Text(" "*28), sg.Image("cog.png")],
    [sg.Text("Nivel de Dificultad:", size=(25, 1), pad=((5, 5), (25, 5))), sg.Input(size=(8, 1), pad=((5, 5), (25, 5)))],
    [sg.Text("Tema:", size=(25, 1)), sg.Input(size=(8, 1))],
    [sg.Text("Tipo de tarjetas:", size=(25, 1)), sg.Combo(tipo_de_tarjetas, default_value=tipo_de_tarjetas[0], readonly=True)],
    [sg.Text("Tiempo de partida [segundos]:", size=(25, 1)), sg.Input(size=(8, 1))],
    [sg.Text(" "*18), sg.Button('Guardar cambios', pad=((5, 5), (35, 5)))]
]


