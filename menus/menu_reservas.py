from reservas import *

def mostrarMenuReservas():
        print('''
--- Menú Reservas ---

1. Agregar cliente
2. Modificar cliente
3. Borrar cliente
4. Mostrar clientes
-------------------------------
0. Salir
''')
        
def mostrarIngresarMenuReservas(reservas):
    mostrarMenuReservas()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
             pass
            #agregarCliente(clientes)
        elif opcion_seleccionada == "2":
             pass
            #modificarCliente(clientes)
        elif opcion_seleccionada == "3":
             pass
            #borrarCliente(clientes)
        elif opcion_seleccionada == "4":
             pass
            #mostrarClientes(clientes)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuReservas() # Muestra el print del menu luego de salir de la opcion seleccionada