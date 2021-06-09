import datetime
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

    def generar_tablero(self):
        """
        Verifica la hora, el dia, la dificultad y genera la matriz para el tablero del juego
        """
        hoy = datetime.datetime.today()
        dia_de_la_semana = hoy.weekday()
        hora_del_dia = hoy.hour
        if self.dificultad == "Fácil":
            pass
        elif self.dificultad == "Medio":
            pass
        else:
            pass

    def generar_matriz(self, x, y, datos):
        """
        Devuelve una matriz para ser usada como tablero
        """
        matriz = []
        return matriz

    def hay_coincidencia(self):
        """
        Devuelve que si hay coincidencia entre 2 tarjetas
        """
        pass

    def hay_fin_del_juego(self):
        """
        Devuelve si ya alcanzaron todas las coincidencias o se alcanzo el tiempo limite
        """
        pass

    def revelar_tarjeta(self):
        """
        Muestra el resultado de la tarjeta al voltearla
        """
        pass

    def esconder_tarjeta(self):
        """
        Esconde una tarjeta revelada
        """
        pass

    def guardar_datos(self):
        """
        Guarda los datos de las acciones que se producen durante la partida
        """
        pass


if __name__ == '__main__':
    pass
