def reportes(alumnos, opcion, minimo, maximo):
    """ Imprime una lista de tuplas de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma

        return: lista de tuplas de los alumnos que estan en el rango
    """

    def reporteEval1(alumno, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumno[1] <= maximo):
            alumnos_filtrados.append(alumno)

    def reporteEval2(alumno, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumno[2] <= maximo):
            alumnos_filtrados.append(alumno)

    def reporteSuma_Notas(alumno, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumno[3] <= maximo):
            alumnos_filtrados.append(alumno)

    
    alumnos_filtrados = [] # Los alumnos que cumplen la condicion (lista auxiliar)

    
    for alumno in alumnos:
        if (opcion == 1):
            reporteEval1(alumno, minimo, maximo, alumnos_filtrados)
        elif (opcion == 1):
            reporteEval2(alumno, minimo, maximo, alumnos_filtrados)
        else:
            reporteSuma_Notas(alumno, minimo, maximo, alumnos_filtrados)
            
    return alumnos_filtrados


    #return list(filter(lambda alumno: minimo <= alumno[opcion] <= maximo , alumnos))
