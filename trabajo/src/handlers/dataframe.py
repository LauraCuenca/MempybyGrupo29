import pandas as pd

columnas = ['Tiempo', 'Num de Part', 'Cant Total de Palabras', 'Nombre Evento','Nick','Genero','Edad',
            'Estado','Palabra','Nivel']  # definimos los nombres de las columnas

datos_juego = pd.DataFrame(columns=columnas)

def agrego_filas(datos,datos_juego):
    """ Agrega filas al dataFrame de datos del juego"""
    
    nueva_fila = pd.Series(datos) # creamos un objeto Series
    datos_juego = datos_juego.append(nueva_fila, ignore_index=True)

    return datos_juego

def agrupo_registros(tiempo,num_part,cant_total,nomb_even,nick,genero,edad,estado,palabra,nivel):
    """ Agrupo los registros de todas las variables para registrar"""

    datos=[tiempo,num_part,cant_total,nomb_even,nick,genero,edad,estado,pàlabra,nivel]

    return datos