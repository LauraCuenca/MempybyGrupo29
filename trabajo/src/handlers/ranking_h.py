import PySimpleGUI as sg
import csv
import pandas as pd
import matplotlib.pyplot as plt
from src.handlers import sonido


#def obtener_datos():
   # datos_puntos = pd.read_csv("datos_de_puntos.csv")
    #filtro= datos_puntos[['nick','puntos']].head(7)
    #ranking= filtro.sort_values(by='puntos',ascending=False)
    #print(ranking)
    #return ranking

#def iterar(data):

    #for x in data:
       # lista_de_listas= [[data[0]],[data[1]],[data[2]],[data[3]],[data[4]]]
    #return lista_de_listas


#fig, ax =plt.subplots(1,1)
#data= obtener_datos()
#data_act=iterar(data)
#column_labels= [['Nick'],['Puntaje']]
#ax.axis('tight')
#ax.axis('off')
#ax.table(cellText=data_act,colLabels=column_labels,loc="center")
#plt.title("Ranking de puntajes")
#plt.savefig("src/recursos/graficos/ranking.png")

def start():
    """ Lanza la ejecución de la ventana del tablero """
    window = loop()
    window.close()

def build():
    """ Crea la ventana para registrar el usuario"""
    size= (15,2)

    layout = [
    [sg.Image(filename="src/recursos/graficos/ranking.png")],
    [sg.Button("Salir",size=(size),key=("-SALIR-"))]
    ]
    
    ranking = sg.Window("Grafico",layout=layout,size=(550,550),element_justification='c', resizable=False, modal=True)

    return ranking


def loop():
    """Loop de la ventana del tablero que capta sus eventos"""
    window = build()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-"):
            sonido.reproducir_sonido(1)
            break
    return window