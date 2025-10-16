from util import *

import manejo_archivos

habitaciones = manejo_archivos.leerArchivoJson("h") # "h" es el prefijo definido para la ruta del archivo habitaciones.json

def mostrarHabitaciones(habitaciones):
    print("-" * 66)
    print(f"{'Nro_habitación':<15} {'Tipo':<15} {'Capacidad':<10} {'Estado':<12} {'Precio':>10}")
    print("-" * 66)
    
    for numero_hab, datos_hab in habitaciones.items(): # Itera sobre cada key, value del diccionario
        numero = numero_hab.split("_")[1] # Formato recibido: "hab_101"
        tipo = datos_hab["tipo"]
        capacidad = str(datos_hab["capacidad"])
        estado = datos_hab["estado"]
        precio = str(datos_hab["precio"])

        print(f"{numero:<15} {tipo:<15} {capacidad:<10} {estado:<12} {precio:>10}")
    
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
    habitacion_encontrada = None  # Inicialmente no encontrada

    for hab in habitaciones:
        if hab[0] == id:
            habitacion_encontrada = hab  # Se guarda la habitación encontrada

    if habitacion_encontrada is not None:
        razon = input("Ingrese la razón de la baja: ")
        # se copia la habitación con slicing
        habitacion = habitacion_encontrada[:]
        # se agrega la razón
        habitacion.append(razon)
        # se mueve a la matriz de bajas
        habitaciones_baja.append(habitacion)
        # se elimina de la lista principal
        habitaciones.remove(habitacion_encontrada)
        print("La habitación ha sido dada de baja por la siguiente razón:", razon)
    else:
        print("Error. No existe habitación con ese número.")

    esperarVolverMenu()

def reintegrarHabitacion(habitaciones, habitaciones_baja):
    id = pedir_entero("Ingrese el Nro. de habitación a reintegrar: ")
    habitacion_baja = None  # Inicialmente no encontrada

    for hab in habitaciones_baja:
        if hab[0] == id:
            habitacion_baja = hab  # Se guarda si se encuentra

    if habitacion_baja is not None:
        # Se crea una copia de la habitación sin la razón de la baja
        habitacion = habitacion_baja[:-1]  

        # Se busca la posición que le corresponde en la lista principal según el Nro_habitacion
        pos = 0
        for hab in habitaciones:
            if hab[0] < id:
                pos += 1
        
        habitaciones.insert(pos, habitacion)
        habitaciones_baja.remove(habitacion_baja)

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