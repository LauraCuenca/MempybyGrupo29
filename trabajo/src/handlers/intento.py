import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos_de_partidas.csv', encoding='utf-8')

#nro_de_partida de las partidas que terminaron en timeout
timeout = df[df['estado'] == 'timeout']["nro_de_partida"].values.tolist()

df2 = df[df['nro_de_partida'].isin(timeout)]
df3= df2['palabra'].unique()

#df2 = df2[df2["estado"] == "ok"]
#df2 = df2.groupby(["nro_de_partida","cant_palabras"])["estado"].count().reset_index(name="ok")

#Calculo porcentaje
#df3 = df2["ok"] * 100 / df2["cant_palabras"]

#print(df2)
print(df3)