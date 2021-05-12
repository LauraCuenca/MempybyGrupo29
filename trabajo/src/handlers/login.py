import pickle


def comparacion(usuario,cont):
    with open("jugadores",'rb') as archivo:
        jugadores= pickle.load(archivo)
        if jugadores[0]
