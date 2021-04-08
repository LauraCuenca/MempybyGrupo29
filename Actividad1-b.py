alumnos = [("Diego", 2, 7, 9), ("Mauro", 5, 2, 13), ("Laura", 10, 9, 19)]



def reportes(alumnos, opcion, minimo, maximo):
    """ Imprime una tupla de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma

        return: lista de tuplas de los alumnos que estan en el rango
    """

    
    def reporteEval1(alumnos, minimo, maximo, i, alumnos_filtrados):
        nota1 = alumnos[i][1]
        if (nota1 >= minimo) and (nota1 <= maximo):
            alumnos_filtrados.append(alumnos[i])

    def reporteEval2(alumnos,min,max):
        nota2 = alumnos[0][2]
        if (nota2 >= min) and (nota2 <= max):
            return nota2

    def reporteSuma_Notas(alumnos,min,max):
        suma = alumnos[0][3]
        if (suma >= min) and (suma <= max):
            return suma

    
    alumnos_filtrados = [] # Los alumnos que cumplen la condicion (lista auxiliar)

    
    for i in range(len(alumnos)):
        if (opcion == 1):
            reporteEval1(alumnos, minimo, maximo, i, alumnos_filtrados)
            #print(f"los estudiantes con valores dentro del rango son {alumnos[0][0]}")
        elif (opcion == 2):
            reporteEval2(alumnos,min,max)
            print(f"los estudiantes con valores dentro del rango son {alumnos[1][0]}")
        else:
            reporteSuma_Notas(alumnos,min,max)
            print(f"los estudiantes con valores dentro del rango son {alumnos[2][0]}")
    print(alumnos_filtrados)




minimo = 3#input()
maximo = 7#input()

reportes(alumnos, 1, minimo, maximo)   
