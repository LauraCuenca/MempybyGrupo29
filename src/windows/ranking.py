import PySimpleGUI as sg



def build():
    """ Crea la ventana para registrar el usuario"""
    size= (30,2)

    layout = [
    [sg.Image(filename=("src/recursos/images/ranking.png"),size=(150,150))],   
    [sg.Button("Ranking : Nivel Facil",key=("-RANKING_FACIL-"),size=(size))],
    [sg.Button("Ranking : Nivel Medio",key=("-RANKING_MEDIO-"),size=(size))],
    [sg.Button("Ranking : Nivel Dificil",key=("-RANKING_DIFICIL-"),size=(size))],
    [sg.Button("Salir",key=("-SALIR-"),size=(size))]
    ]
    
    ranking = sg.Window("Ranking",layout=layout,size=(550,550),element_justification='c', resizable=False, modal=True)

    return ranking