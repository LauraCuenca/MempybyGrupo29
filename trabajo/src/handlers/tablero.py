import csv



def procesar_pokemon(ruta="src/recursos/datasets/pokemon.csv"):
    """
    Devuelve una lista de pokemons dependiendo las condiciones
    """

    archivo = open(ruta, "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader) 
    archivo.close()

    print(encabezado)
    #print(datos)

    # Devuelve todos los pokemones tipo Grass y Poison al mismo tiempo (14)
    pokemones = list(filter(lambda x: x if len(x) == 3 and x[1]=="Grass" and x[2]=="Poison" else None, datos))
    #print(pokemones)
    #print(len(pokemones))

    # Devuelve todos los pokemones tipo Normal y Volador al mismo tiempo (26)
    pokemones = list(filter(lambda x: x if len(x) == 3 and x[1]=="Normal" and x[2]=="Flying" else None, datos))
    #print(pokemones)
    #print(len(pokemones))

    # Devuelve todos los pokemones tipo Bug y diferentes a Poison o Flying (30)
    pokemones = list(filter(lambda x: x if len(x) == 3 and x[1]=="Bug" and x[2]!="Poison" and x[2]!="Flying" else None, datos))
    #print(pokemones)
    #print(len(pokemones))

    # Devuelve todos los pokemones tipo Dragon y que no tengan segundo tipo (12)
    pokemones = list(filter(lambda x: x if len(x) == 2 and x[1]=="Dragon" else None, datos))
    #print(pokemones)
    #print(len(pokemones))

    # Devuelve todos los pokemones que contengan la letra "k" en su nombre,
    # que la longitud de su nombre sea mayor a 8 y que solo tengan 1 tipo (15)
    pokemones = list(filter(lambda x: x if "k" in x[0] and len(x[0]) > 8 and len(x) == 2 else None, datos))
    #print(pokemones)
    #print(len(pokemones))

    # Devuelve todos los pokemones que terminen su nombre en "on" (44)
    pokemones = list(filter(lambda x: x if x[0][-2:] == "on" else None, datos))
    #print(pokemones)
    #print(len(pokemones))


def procesar_fifa(ruta="src/recursos/datasets/fifa20data.csv"):
    """
    Devuelve una lista de todos los jugadores dependiendo las condiciones
    """

    archivo = open(ruta, "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader) 
    archivo.close()

    print(encabezado)

    # Devuelve todos los jugadores con imagen, pais==Argentina, edad entre 30 y 35 años
    # que sean zurdos y pesen menos de 170lbs (17)
    jugadores = list(filter(lambda x: x if x[1] and x[2]=="Argentina" and 30 < int(x[4]) < 35 and 
                x[11]=="Left" and int(x[10][:-3]) < 170 else None, datos))
    #print(jugadores)
    #print(len(jugadores))

    # Devuelve todos los jugadores con imagen, edad menos a 18 años y jueguen de arquero (11)
    jugadores = list(filter(lambda x: x if x[1] and int(x[4]) < 17 and x[3]=="GK" else None, datos))
    #print(jugadores)
    #print(len(jugadores))

    # Devuelve todos los jugadores con imagen, edad==23, Overall==Potential y que sean zurdos (32)
    jugadores = list(filter(lambda x: x if x[1] and int(x[4])==23 and x[5]==x[6] and x[11]=="Left" else None, datos))
    #print(jugadores)
    #print(len(jugadores))

    # Devuelve todos los jugadores con imagen, cuyos nombres sean mas de 18 caracteres y contengan
    # las letras k,z y w (16)
    jugadores = list(filter(lambda x: x if x[1] and "k" in x[0] and "z" in x[0] and "w" in x[0]
                            and len(x[0]) > 18 else None, datos))
    #print(jugadores)
    #print(len(jugadores))



if __name__ == '__main__':
    procesar_pokemon("../recursos/datasets/pokemon.csv")
    procesar_fifa("../recursos/datasets/fifa20data.csv")

