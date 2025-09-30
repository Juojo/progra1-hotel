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

        assert (mes > 1 and mes < 12), "El mes debe ser un número entre 1 y 12"
            
        
        assert (año > 1000 and año < 9999), "El año debe tener 4 digitos"
        
            
        # Meses con 31 días
        assert ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia < 1 or dia > 31)), "Para el mes escogido hay un máximo de 31 días"
    
    
                
        # Meses con 30 días
        assert ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and  (dia < 1 or dia > 30)), "Error: Para el mes escogido hay un máximo de 30 días"
                
        # Febrero
        if mes == 2:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):  # Bisiesto
                assert (dia < 1 or dia > 29), "Año bisiesto, febrero tiene hasta 29 días"
            else:
                assert (dia < 1 or dia > 29), "Febrero tiene hasta 28 días este año"
    
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
