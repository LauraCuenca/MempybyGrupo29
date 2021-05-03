import PySimpleGUI as sg
from windows import game

sg.theme("Topanga")

image= "cerebro.png"
layout=[ 
        [sg.Image(image, size=(200,200))],
        [sg.Text("Usuario")],
        [sg.Input()],
        [sg.Text("Contraseña")],
        [sg.Input()],
        [sg.Button("Registrarse",pad=((5, 5), (25, 5)),size=(10,2),key="-REGISTER")],
        [sg.Button("Iniciar Sesion",size=(10,2),key= "-INICIAR_SESION-")],
        [sg.Button("Salir",size=(8,2))]]

window= sg.Window("Mempy -byGrupo29",keep_on_top=True, element_justification='c',layout=layout,size=(480,500
))

while True:
    event,values= window.read()
    
    if event == "-REGISTER-":
       game.register()

    if event == "-INICIAR SESION-":
       game.first_window()

    if event == sg.WIN_CLOSED or event == "Salir" :
        break

    
window.close()