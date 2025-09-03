from util import *

def mostrarHabitaciones(habitaciones):
    print(f"{'Nro_habitación':<10} {'Tipo':<10} {'Capacidad':<10} {'Estado':<10} {'Precio'}")
    print("-" * 40)
    for habitacion in habitaciones:
        print(f"{habitacion[0]:<10} {habitacion[1]:<10} {habitacion[2]:<10} {habitacion[3]:<10} {habitacion[4]}")
    esperarVolverMenu()

def modificarEstadoHabitacion(habitaciones):
    id = int(input("Ingrese el Nro. de habitación: "))
    existe = False
    i = 0
    indice = -1
    # Se busca si existe un cliente con ese DNI
    while i < len(habitaciones) and not existe:
        if id == habitaciones[i][0]:
            existe = True
            indice = i
        i = i + 1
        
    if existe:
        nuevo_estado = input("Ingrese el nuevo estado de la habitación: ")
        habitaciones[indice][3] = nuevo_estado
        print("Se han modificado el estado de la habitación correctamente.")
    else:
        print("Error. No hay habitación con ese Nro.")

    esperarVolverMenu()

def BajaHabitacion(habitaciones):
    id = int(input("Ingrese el Nro. de habitación: "))
    existe = False
    i = 0
    indice = -1
    # Se busca si existe un cliente con ese DNI
    while i < len(habitaciones) and not existe:
        if id == habitaciones[i][0]:
            existe = True
            indice = i  # Se guarda la posicion del cliente
        i = i + 1
    if existe:
        habitaciones.pop(indice)
        print("Se ha borrado el cliente correctamente.")
    else:
        print("Error. No hay un cliente registrado con ese DNI.")
    esperarVolverMenu()