import os
from datos import nombres, eval1, eval2
from actividad1_promedios import generar_lista_final, imprimir_datos
from actividad1_reportes import reportes
from actividad1_ordenar import ordenar_segun_parametro


def menu():
    """Función que limpia la pantalla y muestra nuevamente el menu"""
    os.system('cls')
    print("╔═"+"═"*80)
    print("║Seleccioná una opción")
    print("║\t1 - Calcular el promedio de las notas finales de todos los estudiantes")
    print("║\t2 - Generar reportes")
    print("║\t3 - Ordernar los datos")
    print("║\t4 - Salir")
    print("╚═"+"═"*80)
    return input("Insertá un numero valor >> ")


def menu_reportes():
    """Limpia la pantalla y muestra nuevamente el menu de reportes"""
    os.system('cls')
    print("╔═"+"═"*80)
    print("║Seleccioná una opción")
    print("║\t1 - Generar reportes de Evaluacion 1")
    print("║\t2 - Generar reportes de Evaluacion 2")
    print("║\t3 - Generar reportes de Nota Final")
    print("║\t4 - Volver")
    print("╚═"+"═"*80)
    return input("\nInsertá un numero valor >> ")


def menu_ordenar():
    """Limpia la pantalla y muestra nuevamente el menu de ordenar datos"""
    os.system('cls')
    print("╔═"+"═"*80)
    print("║Seleccioná una opción")
    print("║\t1 - Ordenar por NOMBRE")
    print("║\t2 - Ordenar por NOTA DE EVALUACION 1")
    print("║\t3 - Ordenar por NOTA DE EVALUACION 2")
    print("║\t4 - Ordenar por NOTA FINAL")
    print("║\t5 - Volver")
    print("╚═"+"═"*80)
    return input("Insertá un numero valor >> ")


def menu_ordenar_aZ():
    """Limpia la pantalla y muestra nuevamente el menu de ordenar datos"""
    os.system('cls')
    print("╔═"+"═"*80)
    print("║Seleccioná una opción")
    print("║\t1 - Ordenar a-Z, 0-9")
    print("║\t2 - Ordenar Z-a, 9-0")
    print("║\t3 - Volver")
    print("╚═"+"═"*80)
    return input("Insertá un numero valor >> ")


def ingresar_datos():
    """Devuelve parametros para los filtros del reporte"""
    minimo = int(input("Ingrese la nota MINIMA a filtrar >>"))
    maximo = int(input("Ingrese la nota MAXIMA a filtrar >>"))
    return minimo, maximo




alumnos = generar_lista_final(nombres, eval1, eval2)

while True:
    # Mostramos el menu
    opcionMenu = menu()

    if opcionMenu == "1":
        imprimir_datos(alumnos)
        input()
    elif opcionMenu == "2":
        opcionMenu = menu_reportes()
        if opcionMenu == "1" or opcionMenu == "2" or opcionMenu == "3":
            minimo, maximo = ingresar_datos()
            alumnos_filtrados = reportes(alumnos, opcionMenu, minimo, maximo)
            imprimir_datos(alumnos_filtrados) 
            input()
        else:
            input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        opcionMenu = menu_ordenar()
        if opcionMenu == "1" or opcionMenu == "2" or opcionMenu == "3" or opcionMenu == "4":
            de_menor_a_mayor = menu_ordenar_aZ()
            if de_menor_a_mayor == "2":
                de_menor_a_mayor = True
            else:
                de_menor_a_mayor = False
            imprimir_datos(ordenar_segun_parametro(alumnos, opcionMenu, de_menor_a_mayor))
            input()
        else:
            input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        break # Fin del programa
    else:
        input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")