import PySimpleGUI as sg



def build():
    """ Crea la ventana para registrar el usuario"""
    size= (20,2)
    size2= (30,15)

    layout = [
    [sg.Image(filename=("src/recursos/images/acerca_de.png"),size=(150,150))],   
    [sg.Text("Mempy-By grupo29." 
    "Este juego, se realizo entre 3 compañeros que realizan el Seminario de Lenguaje de Python, nuestros nombres son: Diego, Laura y Mauro."
    "Tratamos de ponerle nuestra idea de juego, tantos en los gustos en los criterios, como en el diseño del juego.",size=(size2))],
    [sg.Button("Salir",key=("-SALIR-"),size=(size))]
    ]
    
    acerca_de = sg.Window("Acerca de Nosotros",layout=layout,size=(550,550),element_justification='c', resizable=False, modal=True)

    return acerca_de