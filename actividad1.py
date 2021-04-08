def crear_lista(arch):
    """ Crea una lista a partir de los archivos importados"""
    with open(arch) as archivo:
        datos=len(arch.readline())
        for i in range(datos):
            linea=arch.readline(i)
    return linea

nombres= crear_lista('nombres.txt')
eval1= crear_lista('eval1.txt')
eval2= crear_lista ('eval2.txt')

def lista_de_tuplas(nombres,eval1,eval2):
    """ Crea una lista de tuplas, que contiene el nombres, las notas, y la suma de las notas"""
    suma= []
    for i in range(len(eval1)):
        suma.append(sum(eval1[i],eval2[i]))
        alumnos= list(zip(nombres,eval1,eval2,total))

formato = "{:4} {:16} {:10} {:10} {:10}"
formato2= "{:4} {:10} {:10} {:10} {:10}"
print(formato.format('','Nombre','Eval1','Eval2','Total'))
for i in range(len(alumnos)):
    print(formato2.format(i,alumnos[i][0],alumnos[i][1],alumnos[i][2],alumnos[i][3]))




alumnos = [("Mauro", 5, 2, 13), ("Diego", 2, 7, 9), ("Lau", 10, 9, 19)]

def filtrar_segun_parametro(alumnos, param=0):
    """Filtra segun parametro

    param == 0: filtra por nombre
    param == 1: filtra por eval1
    param == 2: filtra por eval2
    param == 3: filtra por suma
    """
    return sorted(alumnos, key=lambda alumno: alumno[param])

print(filtrar_segun_parametro(alumnos,3))