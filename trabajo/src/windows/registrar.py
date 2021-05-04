import PySimpleGUI as sg

def build():

    size= (12,2)

    layout = [
    #[sg.Image(filename="src/images/vcard_edit.png")],
    [sg.Text("Nombre de Usuario *",size=(size))],
    [sg.Input()],
    [sg.Text("Contraseña *",size=(size))],
    [sg.Input()],
    [sg.Text("Confirmar contraseña *",size=(size))],
    [sg.Input()],
    [sg.Text("Genero *",size=(size))],
    [sg.Input()],
    [sg.Text("Edad *",size=(size))],
    [sg.Input()],
    [sg.Button("Registrarse",size=(size),pad=(5,5),key=("-REGISTRARSE-"))]
    ]
    
    registrar = sg.Window("Registrarse",layout=layout,size=(480,500),element_justification='c')

    return registrar