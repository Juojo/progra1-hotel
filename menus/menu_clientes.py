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
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            agregarCliente(clientes)
        elif opcion_seleccionada == "2":
            modificarCliente(clientes)
        elif opcion_seleccionada == "3":
            borrarCliente(clientes)
        elif opcion_seleccionada == "4":
            mostrarClientes(clientes)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuClientes() # Muestra el print del menu luego de salir de la opcion seleccionada