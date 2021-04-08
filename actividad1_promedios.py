from datos import nombres, eval1, eval2
from statistics import mean


def crear_lista(arch):
    """ Crea una lista a partir del string enviado"""
    lista = arch.replace("'", "").replace(" ", "").replace("\n", "").split(",")
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


def imprimir_datos(alumnos, suma):
    """ Imprime los datos de los alumnos en el formato dispuesto"""
    formato = "{:16} {:10} {:10} {:10}"
    formato2 = "{:10} {:10} {:10} {:10}"
    formato3 = "{:28} {:10} {:3}"
    print(formato.format('Nombre', 'Eval1', 'Eval2', 'Sumas'))
    for i in range(len(alumnos)):
        print(formato2.format(alumnos[i][0], alumnos[i]
                              [1], alumnos[i][2], alumnos[i][3]))
    total = sum(suma)
    print(formato3.format(" ", "suma", total))
    promedio = mean(suma)
    print(formato3.format(" ", "promedio", promedio))


nombres = crear_lista(nombres)
eval1 = crear_lista(eval1)
eval2 = crear_lista(eval2)
eval1 = convertir_a_int(eval1)
eval2 = convertir_a_int(eval2)
suma = lista_suma(eval1, eval2)
alumnos = lista_de_tuplas(nombres, eval1, eval2, suma)
imprimir = imprimir_datos(alumnos, suma)