from util import *

def mostrarHabitaciones(habitaciones):
    print(f"{'Nro_habitación':<10} {'Tipo':<10} {'Capacidad':<10} {'Estado':<10} {'Precio'}")
    print("-" * 40)
    for habitacion in habitaciones:
        print(f"{habitacion[0]:<10} {habitacion[1]:<10} {habitacion[2]:<10} {habitacion[3]:<10} {habitacion[4]}")
    esperarVolverMenu()

def modificarEstadoHabitacion(habitaciones):
    id_habitacion = int(input("Ingrese el Nro. de habitación: "))

    # Creamos una lista con todos los numeros de habitacion
    numeros = [hab[0] for hab in habitaciones]

    # Verificamos si el numero ingresado existe en la lista de habitaciones
    if id_habitacion in numeros:
        
        indice = numeros.index(id_habitacion) # Obtenemos el indice de la habitacion con .index 

        nuevo_estado = input("Ingrese el nuevo estado de la habitación: ")
        habitaciones[indice][3] = nuevo_estado  # Modificamos el estado de la habitacion

        print("Se han modificado el estado de la habitacion correctamente.")
    else:
        print("Error. No hay habitación con ese Nro.")

    esperarVolverMenu()

def bajaHabitacion(habitaciones, habitaciones_baja):
    id = int(input("Ingrese el Nro. de habitación: "))
    existe = False
    i = 0
    indice = -1
    # Se busca si existe una habitacion con ese nro
    while i < len(habitaciones) and not existe:
        if id == habitaciones[i][0]:
            existe = True
            indice = i  # Se guarda la posicion de la habitacion
        i = i + 1

    if existe:
        razon = input("Ingrese la razón de la baja: ")
        # se copia la habitación con slicing
        habitacion = habitaciones[indice][:]
        # se agregamos la razón
        habitacion.append(razon)
        # se mueve a la matriz de bajas
        habitaciones_baja.append(habitacion)
        # se elimina de la lista principal
        habitaciones.pop(indice)
        print(" La habitación ha sido dada de baja por la siguiente razón:", razon)
    else:
        print("Error. No existe habitación con ese número.")

    esperarVolverMenu()

def mostrarHabitacionesBaja(habitaciones_baja):
    print(f"{'Nro_habitación':<10} {'Tipo':<10} {'Capacidad':<10} {'Estado':<10} {'Precio':<10} {'Razón'}")
    print("-" * 40)
    for habitacion in habitaciones_baja:
        print(f"{habitacion[0]:<10} {habitacion[1]:<10} {habitacion[2]:<10} {habitacion[3]:<10} {habitacion[4]:<10} {habitacion[5]}")
    esperarVolverMenu()