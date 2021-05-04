import PySimpleGUI as sg


def reg_ventana():

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
    [sg.Button]
    ]
    
    register = sg.Window('Registrarse').Layout(layout)

    return register