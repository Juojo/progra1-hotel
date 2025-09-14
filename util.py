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


def pedir_fecha(mensaje):
    patron = r"^\d{2}/\d{2}/\d{4}$"
    while True:
        valor = input(mensaje)
        if re.match(patron, valor):
            return valor
        else:
            print("Error: Debe ingresar la fecha en formato dd/mm/yyyy.")

def pedir_string(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Error: El campo no puede estar vacío.")
        elif not valor.replace(" ", "").isalpha():
            print("Error: Solo se permiten letras y espacios.")
        else:
            return valor
