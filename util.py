import re

def imprimirTituloOpcion(titulo):
    print()
    print(f"--- {titulo.upper()} ---")
    print()

def limpiarPantalla():
    # \033 = ESC
    print("\033[2J") # Limpia la pantalla
    print("\033[H") # Mueve el cursor al home

def esperarVolverMenu():
    # Volver al menu principal
    print("\nPresione ENTER para volver al menú anterior", end="")
    input()

def generarId(matriz):
    nuevoId = 1

    if len(matriz) != 0:
        ultimoId = matriz[len(matriz)-1][0]
        nuevoId = ultimoId + 1

    return nuevoId

def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Error: Debe ingresar un numero entero valido.")


def pedir_fecha():
    fecha_valida = False

    while fecha_valida == False:
        dia = int(input("Introduzca el día: "))
        mes = int(input("Introduzca el mes: "))
        año = int(input("Introduzca el año: "))

        fecha_valida = True  # Se asume que es válida salvo que encuentre error

        if mes < 1 or mes > 12:
            print("Error: El mes debe ser un número entre 1 y 12")
            fecha_valida = False
        elif año < 1000 or año > 9999:
            print("Error: El año debe tener 4 digitos")
            fecha_valida = False
        # Meses con 31 días
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
            if dia < 1 or dia > 31:
                print("Error: Para el mes escogido hay un máximo de 31 días")
                fecha_valida = False
        # Meses con 30 días
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
            if dia < 1 or dia > 30:
                print("Error: Para el mes escogido hay un máximo de 30 días")
                fecha_valida = False
        # Febrero
        elif mes == 2:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):  # Bisiesto
                if dia < 1 or dia > 29:
                    print("Error: Año bisiesto, febrero tiene hasta 29 días")
                    fecha_valida = False
            else:
                if dia < 1 or dia > 28:
                    print("Error: Febrero tiene hasta 28 días este año")
                    fecha_valida = False
    
    # Se pasa a string para concatenar la fecha
    # Dia y mes se le agrega un 0 si es menor a 10

    if dia < 10:
        dia = "0"+str(dia)
    else:
        dia = str(dia)

    if mes < 10:
        mes = "0"+str(mes)
    else:
        mes = str(mes)

    año=str(año)
    
    # Se crea el string de fecha siguiendo el formato utilizado en la lista almacenada (vuelos_fecha)
    fecha = dia+"/"+mes+"/"+año

    return fecha

def pedir_string(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: El campo no puede estar vacío.")
        elif not valor.replace(" ", "").isalpha():
            print("Error: Solo se permiten letras y espacios.")
        else:
            return valor
