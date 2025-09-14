from util import *

def mostrarHabitaciones(habitaciones):
    print("-" * 66)
    print(f"{'Nro_habitación':<15} {'Tipo':<15} {'Capacidad':<10} {'Estado':<12} {'Precio':>10}")
    print("-" * 66)
    for habitacion in habitaciones:
        print(f"{habitacion[0]:<15} {habitacion[1]:<15} {habitacion[2]:<10} {habitacion[3]:<12} {habitacion[4]:>10}")
    esperarVolverMenu()

def modificarHabitacion(habitaciones):
    id_habitacion = pedir_entero("Ingrese el Nro. de habitación: ")

    # se crea una lista con todos los numeros de habitacion
    numeros = [hab[0] for hab in habitaciones]

    if id_habitacion in numeros:
        indice = numeros.index(id_habitacion)
        habitacion = habitaciones[indice]

        nuevo_tipo = input("Ingrese el nuevo tipo (0 para no modificar): ")
        nueva_capacidad = str(pedir_entero("Ingrese la nueva capacidad (0 para no modificar): "))
        nuevo_estado = input("Ingrese el nuevo estado (0 para no modificar): ")
        nuevo_precio = pedir_entero("Ingrese el nuevo precio (0 para no modificar): ")

        # se actualiza solo si corresponde
        if nuevo_tipo != "0":
            habitacion[1] = nuevo_tipo
        if nueva_capacidad != "0":
            habitacion[2] = nueva_capacidad
        if nuevo_estado != "0":
            habitacion[3] = nuevo_estado
        if nuevo_precio != "0":
            habitacion[4] = int(nuevo_precio)

        print("Se han modificado los datos de la habitación correctamente.")
    else:
        print("Error. No hay habitación con ese Nro.")

    esperarVolverMenu()

def bajaHabitacion(habitaciones, habitaciones_baja):
    id = pedir_entero("Ingrese el Nro. de habitación: ")
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
        # se agrega la razón
        habitacion.append(razon)
        # se mueve a la matriz de bajas
        habitaciones_baja.append(habitacion)
        # se elimina de la lista principal
        habitaciones.pop(indice)
        print("La habitación ha sido dada de baja por la siguiente razón:", razon)
    else:
        print("Error. No existe habitación con ese número.")

    esperarVolverMenu()

def reintegrarHabitacion(habitaciones, habitaciones_baja):
    id = pedir_entero("Ingrese el Nro. de habitación a reintegrar: ")
    existe = False
    i = 0
    indice = -1

    while i < len(habitaciones_baja) and not existe:
        if id == habitaciones_baja[i][0]:
            existe = True
            indice = i
        i += 1

    if existe:
        # Se crea una copia de la habitación sin la razón de la baja
        habitacion = habitaciones_baja[indice][:-1]  

        # Se busca la posición que le corresponde en la lista principal según el Nro_habitacion
        pos = 0
        while pos < len(habitaciones) and habitaciones[pos][0] < id:
            pos += 1
        
        habitaciones.insert(pos, habitacion)
        habitaciones_baja.pop(indice)

        print(f"La habitación Nro. {id} ha sido reintegrada correctamente.")
    else:
        print("Error. No existe una habitación con ese número en la lista de bajas.")

    esperarVolverMenu()

def agregarHabitacion(habitaciones):    
    nuevo_id = generarId(habitaciones)
    tipo = input("Ingrese el tipo de habitación: ")
    capacidad = str(pedir_entero("Ingrese la capacidad: "))
    estado = input("Ingrese el estado: ")
    precio = pedir_entero("Ingrese el precio: ")
    
    habitacion = [nuevo_id, tipo, capacidad, estado, precio]
    habitaciones.append(habitacion)
    print(f"\nLa habitación {nuevo_id} se agregó correctamente.")
    
    esperarVolverMenu()

def mostrarHabitacionesBaja(habitaciones_baja):
    print("-" * 87)
    print(f"{'Nro_habitación':<15} {'Tipo':<15} {'Capacidad':<10} {'Estado':<12} {'Precio':<10} {'Razón':>20}")
    print("-" * 87)
    for habitacion in habitaciones_baja:
        print(f"{habitacion[0]:<15} {habitacion[1]:<15} {habitacion[2]:<10} {habitacion[3]:<12} {habitacion[4]:<10} {habitacion[5]:>20}")
    esperarVolverMenu()