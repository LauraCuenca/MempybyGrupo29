import datetime
import random

from src.handlers import tablero


class Juego:
    def __init__(self, dificultad, con_ayuda, tipo_tarjeta, jugador_nombre, jugador_genero, jugador_edad,
                 nro_de_partida):
        self.dificultad = dificultad
        self.con_ayuda = con_ayuda
        self.tipo_tarjeta = tipo_tarjeta
        self.jugador_nombre = jugador_nombre
        self.jugador_genero = jugador_genero
        self.jugador_edad = jugador_edad
        self.nro_de_partida = nro_de_partida
        self.matriz_tablero = []
        self.tiempo_restante = 0
        self.aciertos = 0
        self.descripcion = ""  # Descripcion de las tarjetas de la partida

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
        if self.dificultad == "Fácil":
            tamanio = (4, 3)  # Tamaño x,y del tablero segun la dificultad
            self.tiempo_restante = 200
        elif self.dificultad == "Medio":
            tamanio = (4, 4)
            self.tiempo_restante = 100
        else:
            tamanio = (8, 4)
            self.tiempo_restante = 50
        datos_de_tarjetas = tablero.get_tabla_criterios()[dias[dia_de_la_semana]][hora_del_dia]
        self.descripcion = datos_de_tarjetas["criterio"]
        datos_de_tarjetas = datos_de_tarjetas["funcion"](modo=datos_de_tarjetas["modo"])[
                            0:(tamanio[0] * tamanio[1]) // 2]
        datos_de_tarjetas = datos_de_tarjetas * 2  # Llamar a la funcion que devuelve los datos, sumarla 2 veces para las coincidencias
        random.shuffle(datos_de_tarjetas)  # Mezcla el orden
        self.matriz_tablero = self.generar_matriz(tamanio[0], tamanio[1], datos_de_tarjetas)

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
                return True
        return False

    def hay_fin_del_juego(self):
        """
        Devuelve si ya alcanzaron todas las aciertos o se llego al tiempo limite
        """
        if self.dificultad == "Fácil":
            tamanio = 6  # Tamaño x,y del tablero segun la dificultad
        elif self.dificultad == "Medio":
            tamanio = 8
        else:
            tamanio = 16
        if self.tiempo_restante <= 0:  # Si se acabo el tiempo, terminar juego
            return True
        elif self.aciertos == tamanio:  # Ganaste el juego
            return True
        return False

    def revelar_tarjeta(self, x, y):
        """
        Muestra el resultado de la tarjeta al voltearla. Devuelve la imagen a mostrar
        """
        if self.matriz_tablero[x][y][0] == 0:  # Si esta boca abajo, revelar tarjeta
            self.matriz_tablero[x][y][0] = 1  # Marca la tarjeta como boca arriba
        return self.matriz_tablero[x][y][2]

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

    def guardar_datos(self):
        """
        Guarda los datos de las acciones que se producen durante la partida
        """
        pass


if __name__ == '__main__':
    nueva_partida = Juego("Medio", True, 'Imagen', 'Diego', 'M', 30, 1)
    nueva_partida.generar_tablero()
