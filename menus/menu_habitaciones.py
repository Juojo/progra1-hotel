from habitaciones import *

def mostrarMenuHabitaciones():
    print("""
----------------------------------------
           Menú Habitaciones
----------------------------------------
1. Mostrar habitaciones
2. Modificar habitacion
3. Dar de baja habitacion
4. Mostrar habitaciones no disponibles
5. Reintegrar habitacion
6. Agregar habitacion
----------------------------------------
0. Volver
----------------------------------------
""")
        
def mostrarIngresarMenuHabitaciones(habitaciones):
    mostrarMenuHabitaciones()
    
    opcion_seleccionada = -1 # Se inicializa la variable

    while opcion_seleccionada != 0:
        while True:
            try:
                opcion_seleccionada = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuHabitaciones()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuHabitaciones()

        if opcion_seleccionada == 1:
            mostrarHabitaciones(habitaciones)
        elif opcion_seleccionada == 2:
            modificarHabitacion(habitaciones)
        elif opcion_seleccionada == 3:
            bajaHabitacion(habitaciones, habitaciones_baja)
        elif opcion_seleccionada == 4:
            mostrarHabitacionesBaja(habitaciones_baja)
        elif opcion_seleccionada == 5:
            reintegrarHabitacion(habitaciones, habitaciones_baja)
        elif opcion_seleccionada == 6:
            agregarHabitacion(habitaciones)
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuHabitaciones() # Muestra el print del menu luego de salir de la opcion seleccionada