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

        while True:
            try:
                opcion = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuLogin()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuLogin()

        try:
            if opcion == 1: # (Iniciar sesion)
                login_exitoso = ejecutarOpcionIniciarSesion(usuarios)
            elif opcion == 2: # (Registrarse)
                ejecutarOpcionRegistrarse(usuarios)
            elif opcion == 0: # (Salir)
                salir_menu_login = True # Sale del ciclo del menu por opcion seleccionada
            else:
                raise Exception("Opción no válida. Por favor intente nuevamente.")
        except Exception as e:
            print("Ocurrio un error:", e)
    
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
4. Estadisticas
----------------------------------------
0. Salir
----------------------------------------
""")

        
def mostrarIngresarMenuPrincipal(archivo_clientes, reservas, habitaciones, habitaciones_baja):
    mostrarMenuPrincipal()
    
    opcion_seleccionada = -1
    
    while opcion_seleccionada != 0:
        while True:
            try:    
                opcion_seleccionada = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuPrincipal()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuPrincipal()

        if opcion_seleccionada == 1:
            mostrarIngresarMenuClientes(archivo_clientes)
        elif opcion_seleccionada == 2:
            mostrarIngresarMenuReservas(reservas, habitaciones)
        elif opcion_seleccionada == 3:
            mostrarIngresarMenuHabitaciones(habitaciones, habitaciones_baja)
        elif opcion_seleccionada == 4:
            mostrarIngresarMenuEstadisticas(reservas)
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuPrincipal()