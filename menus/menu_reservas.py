from reservas import *

def mostrarMenuReservas():
    print("""
----------------------------------------
               Menú Reservas
----------------------------------------
1. Agregar Reserva
2. Modificar Reserva
3. Cancelar Reserva
4. Mostrar Reservas
----------------------------------------
0. Volver
----------------------------------------
""")
        
def mostrarIngresarMenuReservas(reservas, habitaciones, clientes):    
    mostrarMenuReservas()

    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            agregarReserva(reservas, habitaciones, clientes)
        elif opcion_seleccionada == "2":
            modificarReserva(reservas)
        elif opcion_seleccionada == "3":
            darBajaReserva(reservas)
        elif opcion_seleccionada == "4":
            mostrarReservas(reservas)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuReservas() # Muestra el print del menu luego de salir de la opcion seleccionada