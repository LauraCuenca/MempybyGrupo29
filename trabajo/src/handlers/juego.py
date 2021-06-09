import datetime
import random

from src.handlers import tablero


class Juego:
    def __init__(self, dificultad, con_imagen, con_texto, jugador_nombre, jugador_genero, jugador_edad, nro_de_partida):
        self.dificultad = dificultad
        self.con_imagen = con_imagen
        self.con_texto = con_texto
        self.criterios = tablero.get_tabla_criterios()
        self.jugador_nombre = jugador_nombre
        self.jugador_genero = jugador_genero
        self.jugador_edad = jugador_edad
        self.nro_de_partida = nro_de_partida
        self.matriz_tablero = []
        self.tiempo_restante = 0
        self.aciertos = 0

    def generar_tablero(self):
        """
        Verifica la hora, el dia, la dificultad y genera la matriz para el tablero del juego
        """
        hoy = datetime.datetime.today()
        dia_de_la_semana = hoy.weekday()
        hora_del_dia = hoy.hour
        datos_de_tarjetas = []  # Llamar a la funcion que devuelve los datos, sumarla 2 veces
        random.shuffle(datos_de_tarjetas)  # Mezcla el orden
        if self.dificultad == "Fácil":
            tamanio = ()  # Tamaño del tablero segun la dificultad
            self.tiempo_restante = 200
        elif self.dificultad == "Medio":
            tamanio = ()
            self.tiempo_restante = 100
        else:
            tamanio = ()
            self.tiempo_restante = 50
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
            for j in range(y):
                matriz.append([0, datos_de_tarjetas[contador_de_datos][0],
                               datos_de_tarjetas[contador_de_datos][1]])  # datos = [texto, imagen]
                contador_de_datos += 1
        return matriz

    def hay_acierto(self):
        """
        Devuelve si hay acierto entre 2 tarjetas
        """
        tarjetas_volteadas = []
        for tarjeta in self.matriz_tablero:
            if tarjeta[0] == 1:  # Si la tarjeta esta volteada
                tarjetas_volteadas.append(tarjeta)
        if len(tarjetas_volteadas) == 2:  # Si hay 2 tarjetas volteadas, verificar acierto
            if tarjetas_volteadas[0][1] == tarjetas_volteadas[1][1]:  # Si sus textos son iguales
                return True
        return False

    def hay_fin_del_juego(self):
        """
        Devuelve si ya alcanzaron todas las aciertos o se llego al tiempo limite
        """
        if self.tiempo_restante <= 0 or self.aciertos == self:  # Si se acabo el tiempo, terminar juego
            return True

    def revelar_tarjeta(self):
        """
        Muestra el resultado de la tarjeta al voltearla. Actualiza el boton con el contenido de la pos de la matriz
        """
        pass

    def esconder_tarjetas(self):
        """
        Esconde todas las tarjetas reveladas. Actualiza los botones y les coloca la imagen generica.
        No voltea las tarjetas ya encontradas con estado = 2
        """
        pass

    def guardar_datos(self):
        """
        Guarda los datos de las acciones que se producen durante la partida
        """
        pass


if __name__ == '__main__':
    pass
