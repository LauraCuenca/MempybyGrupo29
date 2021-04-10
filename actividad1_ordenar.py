def ordenar_segun_parametro(alumnos, opcion=0, de_mayor_a_menor=False):
    """Ordena segun opcionetro (viene del menu)

        opcion == 0: ordena por nombre
        opcion == 1: ordena por eval1
        opcion == 2: ordena por eval2
        opcion == 3: ordena por suma

        return: lista ordenada de los alumnos 
    """
    return sorted(alumnos, key=lambda alumno: alumno[opcion], reverse=de_mayor_a_menor)
