import PySimpleGUI as sg

def build():

    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/images/register.png",size=(80,80))],
    [sg.Text("*Max de caracteres: 10*",text_color='red')],
    [sg.Text("Nombre de Usuario *",size=(size))],
    [sg.InputText(key="-NOMBRE_USUARIO-",do_not_clear=False)],
    [sg.Text("Contraseña *",size=(size))],
    [sg.Input(key="-CONT-",password_char="*",do_not_clear=False)],
    [sg.Text("Confirmar cont. *",size=(size))],
    [sg.Input(key="-CONF_CONT-",password_char="*",do_not_clear=False)],
    [sg.Text("Genero *",size=(size))],
    [sg.Input(key="-GENERO-",do_not_clear=False)],
    [sg.Text("Edad *",size=(size))],
    [sg.Spin(list(range(100)),size=(size),key="-EDAD-")],
    [sg.Button("Registrarse",size=(size),pad=(5,5),key=("-REGISTRARSE-"))]
    ]
    
    registrar = sg.Window("Registrarse",layout=layout,size=(550,500),element_justification='c')

    return registrar