def ordenar_segun_parametro(alumnos, param=0, de_mayor_a_menor=False):
    """Ordena segun parametro (viene del menu)

    param == 0: ordena por nombre
    param == 1: ordena por eval1
    param == 2: ordena por eval2
    param == 3: ordena por suma

    Devuelve la lista ordenada de los alumnos 
    """
    param = int(param) - 1 # Le restamos 1 porque las opciones del menu empiezan en 1 y no en 0
    return sorted(alumnos, key=lambda alumno: alumno[param], reverse=de_mayor_a_menor)
