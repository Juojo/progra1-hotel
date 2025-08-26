from menus import *

def imprimirTituloOpcion(titulo):
    print()
    print(f"--- {titulo.upper()} ---")
    print()
        
def mostrarIngresarVolverMenu():
    # Volver al menu principal
    print("\nPresione ENTER para volver al menú principal", end="")
    input()

    mostrarMenuPrincipal()

def limpiarPantalla():
    # \033 = ESC
    print("\033[2J") # Limpia la pantalla
    print("\033[H") # Mueve el cursor al home