import csv


def procesar_pokemon(ruta="src/recursos/datasets/pokemon.csv", modo=1):
    """
    Devuelve una lista de pokemons dependiendo las condiciones
    """

    archivo = open(ruta, "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader)
    archivo.close()

    print(encabezado)

    pokemones = []
    if modo == 1:
        # Devuelve todos los pokemones tipo Grass o Fantasma y Poison al mismo tiempo (17)
        pokemones = list(
            filter(lambda x: x if len(x) == 3 and (x[1] == "Grass" or x[1] == 'Ghost') and x[2] == "Poison" else None,
                   datos))
        print(pokemones[0])
        print(len(pokemones))
    elif modo == 2:
        # Devuelve todos los pokemones tipo Normal y Volador al mismo tiempo (26)
        pokemones = list(filter(lambda x: x if len(x) == 3 and x[1] == "Normal" and x[2] == "Flying" else None, datos))
        print(pokemones[0])
        print(len(pokemones))
    elif modo == 3:
        # Devuelve todos los pokemones tipo Bug y diferentes a Poison o Flying (30)
        pokemones = list(
            filter(lambda x: x if len(x) == 3 and x[1] == "Bug" and x[2] != "Poison" and x[2] != "Flying" else None,
                   datos))
        print(pokemones[0])
        print(len(pokemones))
    elif modo == 4:
        # Devuelve todos los pokemones tipo Dragon o Hada y que no tengan segundo tipo (28)
        pokemones = list(filter(lambda x: x if len(x) == 2 and (x[1] == "Dragon" or x[1] == "Fairy") else None, datos))
        print(pokemones[0])
        print(len(pokemones))
    elif modo == 5:
        # Devuelve todos los pokemones que contengan la letra "k" o "z" en su nombre,
        # que la longitud de su nombre sea mayor a 8 y que solo tengan 1 tipo (19)
        pokemones = list(
            filter(lambda x: x if ("k" in x[0] or "z" in x[0]) and len(x[0]) > 8 and len(x) == 2 else None, datos))
        print(pokemones[0])
        print(len(pokemones))
    elif modo == 6:
        # Devuelve todos los pokemones que terminen su nombre en "on" (44)
        pokemones = list(filter(lambda x: x if x[0][-2:] == "on" else None, datos))
        print(pokemones[0])
        print(len(pokemones))
    return [[x[0], x[0]] for x in pokemones]


def procesar_fifa(ruta="src/recursos/datasets/fifa20data.csv", modo=2):
    """
    Devuelve una lista de todos los jugadores dependiendo las condiciones
    """

    archivo = open(ruta, "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader)
    archivo.close()

    print(encabezado)

    jugadores = []
    if modo == 1:
        # Devuelve todos los jugadores con imagen, pais==Argentina, edad entre 30 y 35 años
        # que sean zurdos y pesen menos de 170lbs (17)
        jugadores = list(filter(lambda x: x if x[1] and x[2] == "Argentina" and 30 < int(x[4]) < 35 and
                                               x[11] == "Left" and int(x[10][:-3]) < 170 else None, datos))
        print(jugadores[0])
        print(len(jugadores))
    elif modo == 2:
        # Devuelve todos los jugadores con imagen, edad menor a 18 años y jueguen de arquero (64)
        jugadores = list(filter(lambda x: x if x[1] and int(x[4]) < 18 and x[3] == "GK" else None, datos))
        print(jugadores[0])
        print(len(jugadores))
    elif modo == 3:
        # Devuelve todos los jugadores con imagen, edad==23, Overall==Potential y que sean zurdos (32)
        jugadores = list(
            filter(lambda x: x if x[1] and int(x[4]) == 23 and x[5] == x[6] and x[11] == "Left" else None, datos))
        print(jugadores[0])
        print(len(jugadores))
    elif modo == 4:
        # Devuelve todos los jugadores con imagen, cuyos nombres sean mas de 18 caracteres y contengan
        # las letras k,z y w (16)
        jugadores = list(filter(lambda x: x if x[1] and "k" in x[0] and "w" in x[0] and "w" in x[0]
                                               and len(x[0]) > 18 else None, datos))
        print(jugadores[0])
        print(len(jugadores))
    elif modo == 5:
        # Devuelve todos los jugadores con imagen, edad menor a 25 y equipo barcelona (18)
        jugadores = list(filter(lambda x: x if x[1] and int(x[4]) < 25 and x[7] == "FC Barcelona" else None, datos))
        print(jugadores[0])
        print(len(jugadores))
    elif modo == 6:
        # Devuelve todos los jugadores con imagen y que sean extranjeros jugando en Boca, River o San Lorenzo (18)
        jugadores = list(filter(
            lambda x: x if x[1] and x[2] != "Argentina" and (
                    x[7] == "Boca Juniors" or x[7] == "River Plate" or x[7] == "San Lorenzo de Almagro") else None,
            datos))
        print(jugadores[0])
        print(len(jugadores))
    return [[x[0], x[1]] for x in jugadores]


def procesar_logos(ruta="src/recursos/datasets/companies.csv", modo=1):
    """
    Devuelve una lista de todos los logos de autos dependiendo las condiciones
    """

    archivo = open(ruta, "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader)
    archivo.close()

    print(encabezado)

    logos = []
    if modo == 1:
        # Devuelve todos los logos con imagen, con origen distinto a estados unidos o reino unido (29)
        logos = list(filter(lambda x: x if x[1] and x[2] != "United States" and x[2] != "United Kingdom"
        else None, datos))
        print(logos[0])
        print(len(logos))
    elif modo == 2:
        # Devuelve todos los logos con imagen, y segment igual a "Mass-Market Cars" (16)
        logos = list(filter(lambda x: x if x[1] and x[4] == "Mass-Market Cars" else None, datos))
        print(logos[0])
        print(len(logos))
    return [[x[3], x[1]] for x in logos]


def get_tabla_criterios():
    criterios = {'lunes': {(0, 12): {"criterio": "Pokemones tipo Grass o Fantasma y Veneno",
                                     "funcion": procesar_pokemon, "modo": 1},
                           (13, 23): {"criterio": "Pokemones tipo Normal y Volador",
                                      "funcion": procesar_pokemon, "modo": 2}
                           },
                 'martes': {(0, 12): {"criterio": "Pokemones tipo Bug y diferentes a Poison o Flying",
                                      "funcion": procesar_pokemon, "modo": 3},
                            (13, 23): {"criterio": "Pokemones tipo Dragon o Hada y que no tengan segundo tipo",
                                       "funcion": procesar_pokemon, "modo": 4}
                            },
                 'miercoles': {(0, 12): {
                     "criterio": "Pokemones que contengan la letra k o z en su nombre, que la longitud de su nombre sea mayor a 8 y que solo tengan 1 tipo",
                     "funcion": procesar_pokemon, "modo": 5},
                     (13, 23): {"criterio": "Pokemones que terminen su nombre en on",
                                "funcion": procesar_pokemon, "modo": 6}
                 },
                 'jueves': {(0, 12): {
                     "criterio": "Jugadores con imagen, pais==Argentina, edad entre 30 y 35 años que sean zurdos y pesen menos de 170lbs",
                     "funcion": procesar_fifa, "modo": 1},
                     (13, 23): {"criterio": "Jugadores con imagen, edad menor a 18 años y jueguen de arquero",
                                "funcion": procesar_fifa, "modo": 2}
                 },
                 'viernes': {
                     (0, 12): {"criterio": "Jugadores con imagen, edad==23, Overall==Potential y que sean zurdos",
                               "funcion": procesar_fifa, "modo": 3},
                     (13, 23): {
                         "criterio": "Jugadores con imagen, cuyos nombres sean mas de 18 caracteres y contengan las letras k,z y w",
                         "funcion": procesar_fifa, "modo": 4}
                 },
                 'sabado': {(0, 12): {"criterio": "Jugadores con imagen, edad menor a 25 y equipo barcelona",
                                      "funcion": procesar_fifa, "modo": 5},
                            (13, 23): {
                                "criterio": "Jugadores con imagen que sean extranjeros jugando en Boca, River o San Lorenzo",
                                "funcion": procesar_fifa, "modo": 6}
                            },
                 'domingo': {
                     (0, 12): {"criterio": "Logos con imagen, con origen distinto a estados unidos o reino unido",
                               "funcion": procesar_logos, "modo": 1},
                     (13, 23): {"criterio": "Logos con imagen, y segment igual a Mass-Market Cars",
                                "funcion": procesar_logos, "modo": 2}
                 },
                 }

    return criterios


if __name__ == '__main__':
    # procesar_pokemon("../recursos/datasets/pokemon.csv")
    # procesar_fifa("../recursos/datasets/fifa20data.csv")
    procesar_logos("../recursos/datasets/companies.csv")
