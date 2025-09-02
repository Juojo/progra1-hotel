from usuarios import *

from clientes import *
from reservas import *
from habitaciones import *

# Menus login

def mostrarMenuLogin():
    print("------ Menú ------")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("------------------")
    print("0. Salir")
    print()

def mostrarIngresarMenuLogin(usuarios):
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
        print('''
--- Sistema de Reservas de Hotel ---

1. Agregar cliente
2. Modificar cliente
3. Borrar cliente
4. Mostrar clientes
5. Agregar reserva
6. Cancelar reserva
7. Modificar reserva
8. Mostrar todas las reservas
9. Ver estado de habitaciones
10. Modificar estado de habitacion
-------------------------------
0. Salir
''')
        
def mostrarIngresarMenuPrincipal():
    mostrarMenuPrincipal()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            agregarCliente()
        elif opcion_seleccionada == "2":
            modificarCliente()
        elif opcion_seleccionada == "3":
            borrarCliente()
        elif opcion_seleccionada == "4":
            mostrarClientes()
        elif opcion_seleccionada == "5":
            agregarReserva()
        elif opcion_seleccionada == "6":
            darBajaReserva()
        elif opcion_seleccionada == "7":
            modificarReserva()
        elif opcion_seleccionada == "8":
            mostrarReservas()
        elif opcion_seleccionada == "9":
            pass
        elif opcion_seleccionada == "10":
            pass
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuPrincipal() # Muestra el print del menu principal luego de salir de la opcion seleccionada