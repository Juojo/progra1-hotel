from clientes import *

def mostrarMenuClientes():
    print("""
----------------------------------------
               Menú Clientes
----------------------------------------
1. Agregar cliente
2. Modificar cliente
3. Borrar cliente
4. Mostrar clientes
----------------------------------------
0. Volver
----------------------------------------
""")
        
def mostrarIngresarMenuClientes(clientes):
    mostrarMenuClientes()
    
    opcion_seleccionada = -1 # Se inicializa la variable

    while opcion_seleccionada != 0:
        while True:
            try:
                opcion_seleccionada = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuClientes()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuClientes()

        if opcion_seleccionada == 1:
            #agregarCliente(clientes)
            pass
        elif opcion_seleccionada == 2:
            #modificarCliente(clientes)
            pass
        elif opcion_seleccionada == 3:
            #borrarCliente(clientes)
            pass
        elif opcion_seleccionada == 4:
            #mostrarClientes(clientes)
            pass
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuClientes() # Muestra el print del menu luego de salir de la opcion seleccionada