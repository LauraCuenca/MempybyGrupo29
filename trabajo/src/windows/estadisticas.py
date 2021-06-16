import PySimpleGUI as sg



def build():
    """ Crea la ventana para registrar el usuario"""
    size= (30,2)

    layout = [
    [sg.Image(filename=("src/recursos/images/estadistica.png"),size=(150,150))],   
    [sg.Button("Top 10 de Palabras",key=("-TOP_10-"),size=(size))],
    [sg.Button("Grafico de partidas por estado",key=("-GRAFICO_P_TERM-"),size=(size))],
    [sg.Button("Grafico de partidas segun genero",key=("-GRAFICO_GENERO-"),size=(size))],
    [sg.Button("Grafico segun partidas de la semana",key=("-GRAFICO_SEMANA-"),size=(size))],
    [sg.Button("Promedio de partidas segun nivel",key=("-PROMEDIO_PARTIDAS-"),size=(size))],
    [sg.Button("Porcentaje de palabras sin encontrar",key=("-PORCENTAJE_PALABRAS-"),size=(size))],
    [sg.Button("Salir",key=("-SALIR-"),size=(size))]
    ]
    
    estadistica = sg.Window("Estadistica",layout=layout,size=(550,550),element_justification='c', resizable=False, modal=True)

    return estadistica