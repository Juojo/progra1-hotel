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
    while True:
        try:
            dia = int(input("Introduzca el día: "))
            mes = int(input("Introduzca el mes: "))
            año = int(input("Introduzca el año: "))

            assert 1 <= mes <= 12, "El mes debe ser un número entre 1 y 12"
            assert 1000 <= año <= 9999, "El año debe tener 4 digitos"
            # Meses con 31 días
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                assert 1 <= dia <= 31, "Para el mes escogido hay un máximo de 31 días"
            # Meses con 30 días
            elif mes in [4, 6, 9, 11]:
                assert 1 <= dia <= 30, "Para el mes escogido hay un máximo de 30 días"
            # Febrero
            elif mes == 2:
                if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):  # Bisiesto
                    assert 1 <= dia <= 29, "Año bisiesto, febrero tiene hasta 29 días"
                else:
                    assert 1 <= dia <= 28, "Febrero tiene hasta 28 días este año"
            break
        except ValueError:
            print("Error: Solo se permite el ingreso de numeros enteros")
        except AssertionError as e:
            print("Error:", e)
        except Exception as e:
            print("Error no contemplado:", type(e).__name__)

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
