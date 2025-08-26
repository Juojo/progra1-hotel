from usuarios.login import ejecutarOpcionIniciarSesion
from usuarios.register import ejecutarOpcionRegistrarse

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