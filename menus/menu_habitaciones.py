from habitaciones import *

def mostrarMenuHabitaciones():
        print('''
--- Menú Habitaciones ---

1. Mostrar habitaciones
2. Modificar estado de habitacion
3. Dar de baja habitacion
-------------------------------
0. Salir
''')
        
def mostrarIngresarMenuHabitaciones(habitaciones):
    mostrarMenuHabitaciones()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
             pass
            #mostrarHabitaciones(habitaciones)
        elif opcion_seleccionada == "2":
             pass
            #modificarEstadoHabitacion(habitaciones)
        elif opcion_seleccionada == "3":
             pass
            #BajaHabitacion(habitaciones)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuHabitaciones() # Muestra el print del menu luego de salir de la opcion seleccionada