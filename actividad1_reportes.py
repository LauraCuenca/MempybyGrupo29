def reportes(alumnos, opcion, minimo, maximo):
    """ Imprime una lista de tuplas de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma

        return: lista de tuplas de los alumnos que estan en el rango
    """



    """
    def reporteEval1(alumno,minimo,maximo,alumnos_filtrados):
        if minimo <= alumno[1] <= maximo:
            alumnos_filtrados.append(alumno)
    """

    def reporteEval1(alumnos,minimo,maximo,i,alumnos_filtrados):
        nota1 = alumnos[i][1]
        if (nota1 >= minimo) and (nota1 <= maximo):
            alumnos_filtrados.append(alumnos[i])

    def reporteEval2(alumnos,minimo,maximo,i,alumnos_filtrados):
        nota2 = alumnos[i][2]
        if (nota2 >= minimo) and (nota2 <= maximo):
            alumnos_filtrados.append(alumnos[i])

    def reporteSuma_Notas(alumnos,minimo,maximo,i,alumnos_filtrados):
        suma = alumnos[i][3]
        if (suma >= minimo) and (suma <= maximo):
            alumnos_filtrados.append(alumnos[i])

    
    alumnos_filtrados = [] # Los alumnos que cumplen la condicion (lista auxiliar)

    
    for i in range(len(alumnos)):
        if (opcion == "1"):
            reporteEval1(alumnos,minimo,maximo,i,alumnos_filtrados)
        elif (opcion == "2"):
            reporteEval2(alumnos,minimo,maximo,i,alumnos_filtrados)
        else:
            reporteSuma_Notas(alumnos,minimo,maximo,i,alumnos_filtrados)
            
    return alumnos_filtrados

 