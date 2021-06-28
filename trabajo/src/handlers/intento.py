import PySimpleGUI as sg
import pandas as pd





datos_juego= pd.read_csv('datos_de_partidas.csv')

#tiempo_facil= datos_juego[datos_juego["nivel"]=='facil']['tiempo_partida']
#print(tiempo_facil)

    
    
partidas_timeout= datos_juego[datos_juego["estado"]=='timeout']['nro_de_partida']
palabras= datos_juego[datos_juego["nro_de_partida"]==int(partidas_timeout)]['palabra'].dropna()
cant= palabras.value_counts()

data_dibujo = list(cant)
etiquetas = list(palabras.unique())
print(data_dibujo)
print(etiquetas)