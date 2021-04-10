def reportes(alumnos, opcion, minimo, maximo):
    """ Imprime una lista de tuplas de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma

        return: lista de tuplas de los alumnos que estan en el rango
    """


    def reporteEval1(alumnos, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumnos[1] <= maximo):
            alumnos_filtrados.append(alumnos)

    def reporteEval2(alumnos, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumnos[2] <= maximo):
            alumnos_filtrados.append(alumnos)

    def reporteSuma_Notas(alumnos, minimo, maximo, alumnos_filtrados):
        if (minimo <= alumnos[3] <= maximo):
            alumnos_filtrados.append(alumnos)

    
    alumnos_filtrados = [] # Los alumnos que cumplen la condicion (lista auxiliar)

    
    for i in range(len(alumnos)):
        if (opcion == "1"):
            reporteEval1(alumnos, minimo, maximo, alumnos_filtrados)
        elif (opcion == "2"):
            reporteEval2(alumnos, minimo, maximo, alumnos_filtrados)
        else:
            reporteSuma_Notas(alumnos, minimo, maximo, alumnos_filtrados)
            
    return alumnos_filtrados

 
