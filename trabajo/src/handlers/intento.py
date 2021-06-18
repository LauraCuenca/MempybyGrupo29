import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

datos_juego= pd.read_csv('datos_de_partidas.csv')

top_10 = datos_juego[datos_juego["estado"]=='ok']['palabra'].head(10)
print(top_10)