import PySimpleGUI as sg



def build():
    """ Crea la ventana para registrar el usuario"""
    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/images/register2.png")],
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
    [sg.Button("Registrarse",key=("-REGISTRARSE-"),size=(size)),sg.Button("Salir",size=(size),key=("-SALIR-"))]
    ]
    
    registrar = sg.Window("Registrarse",layout=layout,size=(550,550),element_justification='c', resizable=False, modal=True)

    return registrar

