import PySimpleGUI as sg


def build():

    layout = [
    #[sg.Text(" "*32), sg.Image("user_add.png")],
    [sg.Text("Nombre de Usuario *")],
    [sg.Input()],
    [sg.Text("Contraseña *")],
    [sg.Input()],
    [sg.Text("Confirmar contraseña *")],
    [sg.Input()],
    [sg.Text("Genero *")],
    [sg.Input()],
    [sg.Text("Edad *")],
    [sg.Input(size=(8, 2))],
    [sg.Text(" "*26), sg.Button('Registrarse', pad=((5, 5), (20, 5)))]
    ]
    
    register = sg.Window("Registrarse",layout=layout,size=(480,500),element_justification='c')

    return register