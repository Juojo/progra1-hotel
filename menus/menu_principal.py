from usuarios import ejecutarOpcionIniciarSesion, ejecutarOpcionRegistrarse, usuarios
from .menu_clientes import *
from .menu_reservas import *
from .menu_habitaciones import *
from .menu_estadisticas import *

# Menus login

def mostrarMenuLogin():
    print("""
----------------------------------------
          Sistema de Gestión
               Hotelera
----------------------------------------
1. Iniciar sesión
2. Registrarse
----------------------------------------
0. Salir
----------------------------------------
""")

def mostrarIngresarMenuLogin():
    # Devuelve True si el login fue exitoso
    # Devuelve False si el usuario decidio salir
    
    login_exitoso = False
    
    salir_menu_login = False # Variable para controlar el ciclo principal
    
    while salir_menu_login == False and login_exitoso == False:
        mostrarMenuLogin()
        opcion = input("Elija una opción: ")

        if opcion == "1": # (Iniciar sesion)
            login_exitoso = ejecutarOpcionIniciarSesion(usuarios)
        elif opcion == "2": # (Registrarse)
            ejecutarOpcionRegistrarse(usuarios)
        elif opcion == "0": # (Salir)
            salir_menu_login = True # Sale del ciclo del menu por opcion seleccionada
        else:
            print("\nOpción no válida. Por favor intente nuevamente.\n")
    
    print()
    return login_exitoso

# Menus principal

def mostrarMenuPrincipal():
    print("""
----------------------------------------
            Menú Principal
----------------------------------------
1. Clientes
2. Reservas
3. Habitaciones
4, Estadisticas
----------------------------------------
0. Salir
----------------------------------------
""")

        
def mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones):
    mostrarMenuPrincipal()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            mostrarIngresarMenuClientes(clientes)
        elif opcion_seleccionada == "2":
            mostrarIngresarMenuReservas(reservas, habitaciones, clientes)
        elif opcion_seleccionada == "3":
            mostrarIngresarMenuHabitaciones(habitaciones)
        elif opcion_seleccionada == '4':
            mostrarIngresarMenuEstadisticas(reservas)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuPrincipal() # Muestra el print del menu principal luego de salir de la opcion seleccionada