import os

def menu():
    """Función que limpia la pantalla y muestra nuevamente el menu"""
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Calcular el promedio de las notas finales de todos los estudiantes")
    print("\t2 - Generar reportes")
    print("\t3 - Ordernar los datos")
    print("\t4 - Salir")
    return input("inserta un numero valor >> ")


def menu_reportes():
    """Limpia la pantalla y muestra nuevamente el menu de reportes"""
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Generar reportes de Evaluacion 1")
    print("\t2 - Generar reportes de Evaluacion 2")
    print("\t3 - Generar reportes de Nota Final")
    print("\t4 - Volver")
    return input("inserta un numero valor >> ")


def menu_ordenar():
    """Limpia la pantalla y muestra nuevamente el menu de ordenar datos"""
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Ordenar por NOMBRE")
    print("\t2 - Ordenar por NOTA DE EVALUACION 1")
    print("\t3 - Ordenar por NOTA DE EVALUACION 2")
    print("\t4 - Ordenar por NOTA FINAL")
    print("\t5 - Volver")
    return input("inserta un numero valor >> ")


def menu_ordenar_aZ():
    """Limpia la pantalla y muestra nuevamente el menu de ordenar datos"""
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Ordenar a-Z")
    print("\t2 - Ordenar Z-a")
    print("\t3 - Volver")
    return input("inserta un numero valor >> ")


def ingresar_datos():
    """Devuelve parametros para los filtros del reporte"""
    minimo = input("Ingrese el limite INFERIOR a filtrar >>")
    maximo = input("Ingrese el limite SUPERIOR a filtrar >>")
    return minimo, maximo


while True:
    # Mostramos el menu
    opcionMenu = menu()


    if opcionMenu == "1":
        print("1.")
        input()
    elif opcionMenu == "2":
        print("2.")
        opcionMenu = menu_reportes()
        if opcionMenu == "1":
            print("1.")
            input()
            print(ingresar_datos())
        elif opcionMenu == "2":
            print("2.")
            input()
            print(ingresar_datos())
        elif opcionMenu == "3":
            print("3.")
            input()
            print(ingresar_datos())
        else:
            input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("3.")
        opcionMenu = menu_ordenar()
        if opcionMenu == "1":
            print("1.")
            input()
            menu_ordenar_aZ()
        elif opcionMenu == "2":
            print("2.")
            input()
            menu_ordenar_aZ()
        elif opcionMenu == "3":
            print("3.")
            input()
            menu_ordenar_aZ()
        elif opcionMenu == "4":
            print("4.")
            input()
            menu_ordenar_aZ()
        else:
            input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        break
    else:
        input("\nNo has pulsado ninguna opción correcta...\npulsa una tecla para continuar")