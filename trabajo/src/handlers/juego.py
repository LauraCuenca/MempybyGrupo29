import csv
import datetime
import time
import random
from src.handlers import tablero


class Juego:
    """
    Clase que contiene toda la logica del tablero de juego
    """
    def __init__(self, dificultad, con_ayuda, tipo_tarjeta, jugador_nombre, jugador_genero, jugador_edad):
        self.dificultad = dificultad  # Facil, Medio, Díficil
        self.con_ayuda = con_ayuda
        self.tipo_tarjeta = tipo_tarjeta  # Texto, Imagen, Mixto
        self.jugador_nombre = jugador_nombre  # Datos del jugador
        self.jugador_genero = jugador_genero
        self.jugador_edad = jugador_edad
        self.nro_de_partida = 0  # Numero de partida
        self.matriz_tablero = []  # Matriz con los datos del tablero
        self.tiempo_de_inicio = time.time()  # Tiempo de inicio de la partida
        self.tiempo_maximo = 0
        self.tiempo_restante = 0  # Tiempo restante para jugar
        self.aciertos_maximos = 0
        self.aciertos = 0  # Cantidad de aciertos obtenidos
        self.descripcion = ""  # Descripcion de las tarjetas de la partida
        self.puntaje = 0  # Puntos obtenidos
        self.texto_ayuda = "Sin ayuda"  # Mensaje de ayuda

    def generar_tablero(self):
        """
        Verifica la hora, el dia, la dificultad y genera la matriz para el tablero del juego
        Genera una matriz para ser usada como tablero

        datos_de_tarjeta: [[estado, texto, imagen],...]
        estado:
            0: boca abajo
            1: boca arriba
            2: ya encontrada, boca arriba permanente
        """
        dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        hoy = datetime.datetime.today()
        dia_de_la_semana = hoy.weekday()
        hora_del_dia = hoy.hour
        if 0 <= hora_del_dia <= 12:
            hora_del_dia = (0, 12)
        else:
            hora_del_dia = (13, 23)
        if self.dificultad == "Facil":
            tamanio = (4, 3)  # Tamaño x,y del tablero segun la dificultad
            self.tiempo_restante = 40
        elif self.dificultad == "Medio":
            tamanio = (4, 4)
            self.tiempo_restante = 80
        else:
            tamanio = (8, 4)
            self.tiempo_restante = 100
        self.tiempo_maximo = self.tiempo_restante  # Setea el tiempo maximo
        self.aciertos_maximos = tamanio[0] * tamanio[1] // 2  # Setea la cantidad de aciertos maximos
        datos_de_tarjetas = tablero.get_tabla_criterios()[dias[dia_de_la_semana]][hora_del_dia]
        self.descripcion = datos_de_tarjetas["criterio"]
        datos_de_tarjetas = datos_de_tarjetas["funcion"](modo=datos_de_tarjetas["modo"])[
                            0:(tamanio[0] * tamanio[1]) // 2]
        datos_de_tarjetas2 = datos_de_tarjetas.copy()
        if self.tipo_tarjeta == "Mixto":  # Si es mixto algunas tiene imagen y otras texto
            datos_de_tarjetas2 = [[x[0], 'src/recursos/datasets/images_pokemon/images/vacio.png'] for x in
                                  datos_de_tarjetas]
        datos_de_tarjetas = datos_de_tarjetas + datos_de_tarjetas2  # Llamar a la funcion que devuelve los datos, sumarla 2 veces para las coincidencias
        random.shuffle(datos_de_tarjetas)  # Mezcla el orden
        self.matriz_tablero = self.generar_matriz(tamanio[0], tamanio[1], datos_de_tarjetas)
        self.guardar_datos("inicio_partida", "", "")

    def generar_matriz(self, x, y, datos_de_tarjetas):
        """
        Devuelve una matriz para ser usada como tablero

        datos_de_tarjeta: [[estado, texto, imagen],...]
        estado:
            0: boca abajo
            1: boca arriba
            2: ya encontrada, boca arriba permanente
        """
        contador_de_datos = 0  # Variable para ir contando cual es la sig tarjeta a guardar
        matriz = []
        for i in range(x):
            fila = []
            for j in range(y):
                fila.append([0, datos_de_tarjetas[contador_de_datos][0],
                             datos_de_tarjetas[contador_de_datos][1]])  # datos = [texto, imagen]
                contador_de_datos += 1
            matriz.append(fila)
        return matriz

    def hay_acierto(self):
        """
        Devuelve si hay acierto entre 2 tarjetas
        """
        tarjetas_volteadas = []
        for x in range(len(self.matriz_tablero)):
            for y in range(len(self.matriz_tablero[x])):
                tarjeta = self.matriz_tablero[x][y]
                if tarjeta[0] == 1:  # Si la tarjeta esta volteada
                    tarjetas_volteadas.append((tarjeta, x, y))
        if len(tarjetas_volteadas) == 2:  # Si hay 2 tarjetas volteadas, verificar acierto
            if tarjetas_volteadas[0][0][1] == tarjetas_volteadas[1][0][1]:  # Si sus textos son iguales
                # Marcar como tarjeta volteada permanentemente
                self.matriz_tablero[tarjetas_volteadas[0][1]][tarjetas_volteadas[0][2]][0] = 2
                self.matriz_tablero[tarjetas_volteadas[1][1]][tarjetas_volteadas[1][2]][0] = 2
                self.aciertos += 1
                self.contar_puntos(10)
                self.guardar_datos("intento", "ok",
                                   self.matriz_tablero[tarjetas_volteadas[1][1]][tarjetas_volteadas[1][2]][1])
                return True
            else:
                self.contar_puntos(-1)
                self.guardar_datos("intento", "error",
                                   self.matriz_tablero[tarjetas_volteadas[1][1]][tarjetas_volteadas[1][2]][1])
        return False

    def buscar_ayuda(self, palabra):
        """
        Devuelve el texto de ayuda para la siguiente tarjeta
        """
        for x in range(len(self.matriz_tablero)):
            for y in range(len(self.matriz_tablero[x])):
                if self.matriz_tablero[x][y][0] == 0 and self.matriz_tablero[x][y][1] == palabra:
                    return f"AYUDA: la próxima tarjeta está en la columna {x + 1}"

    def hay_fin_del_juego(self):
        """
        Devuelve si ya alcanzaron todas las aciertos o se llego al tiempo limite
        """
        if self.tiempo_restante <= 0:  # Si se acabo el tiempo, terminar juego
            self.guardar_datos("fin", "timeout", "")
            self.guardar_puntos()
            return True
        elif self.aciertos == self.aciertos_maximos:  # Ganaste el juego
            self.guardar_datos("fin", "finalizada", "")
            self.guardar_puntos()
            return True
        return False

    def revelar_tarjeta(self, x, y):
        """
        Muestra el resultado de la tarjeta al voltearla. Devuelve la imagen o texto a mostrar
        """
        palabra = ""
        if self.matriz_tablero[x][y][0] == 0:  # Si esta boca abajo, revelar tarjeta
            self.matriz_tablero[x][y][0] = 1  # Marca la tarjeta como boca arriba
        if self.tipo_tarjeta == "Imagen":
            imagen = self.matriz_tablero[x][y][2]
        elif self.tipo_tarjeta == "Texto":
            palabra = self.matriz_tablero[x][y][1]
            imagen = "src/recursos/datasets/images_pokemon/images/vacio.png"
        else:
            imagen = self.matriz_tablero[x][y][2]
            if imagen != "src/recursos/datasets/images_pokemon/images/vacio.png":
                palabra = ""
            else:
                palabra = self.matriz_tablero[x][y][1]
        # Si no hay 2 tarjetas volteadas actualizar ayuda
        if self.con_ayuda == "Con":
            self.texto_ayuda = self.buscar_ayuda(self.matriz_tablero[x][y][1])
        return palabra.upper(), imagen

    def get_tarjetas_boca_arriba(self):
        """
        Devuelve la cantidad de tarjetas boca arriba, estado = 1
        """
        tarjetas_volteadas = 0
        for x in range(len(self.matriz_tablero)):
            for y in range(len(self.matriz_tablero[x])):
                if self.matriz_tablero[x][y][0] == 1:  # Si la tarjeta esta boca arriba
                    tarjetas_volteadas += 1
        return tarjetas_volteadas

    def esconder_tarjetas(self):
        """
        Devuelve una lista con todas las tarjetas a esconder si hay al menos dos con estado = 1
        No voltea las tarjetas ya encontradas con estado = 2
        """
        tarjetas_a_esconder = []
        for x in range(len(self.matriz_tablero)):
            for y in range(len(self.matriz_tablero[x])):
                if self.matriz_tablero[x][y][0] == 1:  # Si la tarjeta esta boca arriba
                    tarjetas_a_esconder.append((x, y))
        if len(tarjetas_a_esconder) < 2:
            tarjetas_a_esconder = []
        else:
            for t in tarjetas_a_esconder:  # Si hay 2 tarjetas boca arriba, voltearlas
                self.matriz_tablero[t[0]][t[1]][0] = 0
        return tarjetas_a_esconder

    def guardar_datos(self, evento, estado, palabra):
        """
        Guarda los datos de las acciones que se producen durante la partida
        """
        try:
            with open('datos_de_partidas.csv') as archivo:
                datos = list(csv.reader(archivo, delimiter=','))
        except FileNotFoundError:
            # Si el archivo no existe, crea la cabecera
            datos = [["tiempo_partida", "nro_de_partida", "cant_palabras", "evento", "nick", "genero", "edad", "estado",
                      "palabra", "nivel"]]
        nro_de_partida = datos
        if self.nro_de_partida == 0:  # Si no esta seteado el nro de la partida, buscarlo
            if len(nro_de_partida) <= 3:
                self.nro_de_partida = 1
            else:
                self.nro_de_partida = nro_de_partida[-2]
                self.nro_de_partida = int(self.nro_de_partida[1]) + 1
        with open('datos_de_partidas.csv', mode='a+') as archivo:
            datos_de_partida = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if len(datos) == 1:  # Si no hay datos escribir la cabecera primero
                datos_de_partida.writerow(datos[0])
            datos_de_partida.writerow(
                [round(time.time()), self.nro_de_partida, self.aciertos_maximos, evento, self.jugador_nombre,
                 self.jugador_genero, self.jugador_edad, estado, palabra, self.dificultad])

    def contar_puntos(self, puntos):
        """
        Cuenta los puntos ganados en la partida
        """
        self.puntaje += puntos

    def guardar_puntos(self):
        """
        Guarda los puntos obtenidos al final de la partida
        """
        try:
            with open('datos_de_puntos.csv') as archivo:
                datos = list(csv.reader(archivo, delimiter=','))
        except FileNotFoundError:
            # Si el archivo no existe, crea la cabecera
            datos = [["nro_de_partida", "nick", "puntos", "nivel"]]
        with open('datos_de_puntos.csv', mode='a+') as archivo:
            puntaje = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if len(datos) == 1:  # Si no hay datos escribir la cabecera primero
                puntaje.writerow(datos[0])
            puntaje.writerow([self.nro_de_partida, self.jugador_nombre, self.puntaje, self.dificultad])


if __name__ == '__main__':
    nueva_partida = Juego("Medio", True, 'Imagen', 'Diego', 'M', 30)
    nueva_partida.generar_tablero()
