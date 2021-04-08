alumnos = [("Mauro", 5, 2, 13), ("Diego", 2, 7, 9), ("Laura", 10, 9, 19)]

def reportes(alumnos, opcion):
    """ Imprime una tupla de los alumnos que cumplen las condiciones
        mínimas y máximas

        opcion == 1: ingresa por eval1
        opcion == 2: ingresa por eval2
        opcion == 3: ingresa por suma
    """

    min = 0
    max = 9

    def reporteEval1(alumnos,min,max):
        nota1 = alumnos[0][1]
        if (nota1 >= min) and (nota1 <= max):
            return nota1

    def reporteEval2(alumnos,min,max):
        nota2 = alumnos[0][2]
        if (nota2 >= min) and (nota2 <= max):
            return nota2

    def reporteSuma_Notas(alumnos,min,max):
        suma = alumnos[0][3]
        if (suma >= min) and (suma <= max):
            return suma


    for alumno in alumnos:
        if (opcion == 1):
            reporteEval1(alumnos,min,max)
            print(f"los estudiantes con valores dentro del rango son {alumnos[0][0]}")
        
        elif (opcion == 2):
            reporteEval2(alumnos,min,max)
            print(f"los estudiantes con valores dentro del rango son {alumnos[1][0]}")
        else:
            reporteSuma_Notas(alumnos,min,max)
            print(f"los estudiantes con valores dentro del rango son {alumnos[2][0]}")


print(reportes(alumnos,3))    
