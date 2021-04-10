def reportes(alumnos, opcion, minimo, maximo):
    """ Imprime una lista de tuplas de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma

        return: lista de tuplas de los alumnos que estan en el rango
    """

    return list(filter(lambda alumno: minimo <= alumno[opcion] <= maximo , alumnos))
