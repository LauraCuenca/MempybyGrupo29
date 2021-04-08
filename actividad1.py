alumnos = [("Mauro", 5, 2, 13), ("Diego", 2, 7, 9), ("Lau", 10, 9, 19)]

def filtrar_segun_parametro(alumnos, param=0):
    """Filtra segun parametro

    param == 0: filtra por nombre
    param == 1: filtra por eval1
    param == 2: filtra por eval2
    param == 3: filtra por suma
    """
    return sorted(alumnos, key=lambda alumno: alumno[param])

print(filtrar_segun_parametro(alumnos,3))