from statistics import mean


def crear_lista(arch):
    """ Crea una lista a partir del string enviado"""
    lista = arch.replace('"', "").replace(" ", "").replace("\n", "").split(",")
    return lista


def convertir_a_int(str):
    """Convierte la lista de strings, a int"""
    str = [int(x) for x in str]
    return str


def lista_suma(eval1, eval2):
    """ Crea una lista, sumanod las notas de eval1 y eval2"""
    suma = list(map(lambda x, y: x+y, eval1, eval2))
    return suma


def lista_de_tuplas(nombres, eval1, eval2, suma):
    """ Crea una lista de tuplas, que contiene el nombres, las notas, y la suma de las notas"""
    alumnos = list(zip(nombres, eval1, eval2, suma))
    return alumnos


def imprimir_datos(alumnos):
    """ Imprime los datos de los alumnos en el formato dispuesto"""
    formato = "{:16} {:10} {:10} {:10}"
    formato2 = "\033[{}m{:10} {:10} {:10} {:10}\033[40m"
    formato3 = "{:28} {:10} {:3}"
    print("="*60)
    print(formato.format('Nombre', 'Eval1', 'Eval2', 'Sumas'))
    print("="*60)
    alternar = 0
    colores = (40, 100) # negro, gris
    for i in range(len(alumnos)):
        alternar = alternar % 2
        print(formato2.format(colores[alternar], alumnos[i][0], alumnos[i]
                              [1], alumnos[i][2], alumnos[i][3]))
        alternar += 1
    suma = [alumno[i] for alumno in alumnos for i in range(len(alumno)) if i==3]
    total = sum(suma)
    print(formato3.format(" ", "suma", total))
    promedio = 0
    if len(suma) > 0:  # Tiraba error porque no puede dividir por cero
        promedio = mean(suma)        
    print(formato3.format(" ", "promedio", promedio))


def generar_lista_final(nombres, eval1, eval2):
    """Genera la lista final para ser utilizada por el menu"""
    nombres = crear_lista(nombres)
    eval1 = crear_lista(eval1)
    eval2 = crear_lista(eval2)
    eval1 = convertir_a_int(eval1)
    eval2 = convertir_a_int(eval2)
    suma = lista_suma(eval1, eval2)
    alumnos = lista_de_tuplas(nombres, eval1, eval2, suma)
    return (alumnos)

