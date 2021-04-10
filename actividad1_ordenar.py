def ordenar_segun_parametro(alumnos, param=0, de_mayor_a_menor=False):
    """Ordena segun parametro (viene del menu)

        param == 0: ordena por nombre
        param == 1: ordena por eval1
        param == 2: ordena por eval2
        param == 3: ordena por suma

        return: lista ordenada de los alumnos 
    """
    return sorted(alumnos, key=lambda alumno: alumno[param], reverse=de_mayor_a_menor)
