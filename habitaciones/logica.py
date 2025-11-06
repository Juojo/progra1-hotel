import json
from util import *
import manejo_archivos

formatearCodigoHab = lambda numero_hab: "hab_"+str(numero_hab)

def mostrarHabitaciones(habitaciones):
    try:
        archivo = open(habitaciones, "r")

        try:
            print("-" * 66)
            print(f"{'Nro_habitación':<15} {'Tipo':<15} {'Capacidad':<10} {'Estado':<12} {'Precio':>10}")
            print("-" * 66)

            datos = json.load(archivo)
    
            for codigo_hab, datos_hab in datos.items(): # Itera sobre cada key, value del diccionario
                numero = codigo_hab.split("_")[1] # Formato recibido: "hab_101"
                tipo = datos_hab["tipo"]
                capacidad = str(datos_hab["capacidad"])
                estado = datos_hab["estado"]
                precio = str(datos_hab["precio"])

                print(f"{numero:<15} {tipo:<15} {capacidad:<10} {estado:<12} {precio:>10}")

        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
    except FileNotFoundError as e:
        print("No se encontro el archivo:", e)
    except Exception as e:
        print("Ocurrio un error con la lectura del archivo:", e)
    
    esperarVolverMenu()

def mostrarHabitacionesBaja(habitaciones_baja):
    print("-" * 87)
    print(f"{'Nro_habitación':<15} {'Tipo':<15} {'Capacidad':<10} {'Estado':<12} {'Precio':<10} {'Razón':>10}")
    print("-" * 87)

    for codigo_hab, datos_hab in habitaciones_baja.items(): # Itera sobre cada key, value del diccionario
        numero = codigo_hab.split("_")[1] # Formato recibido: "hab_101"
        tipo = datos_hab["tipo"]
        capacidad = str(datos_hab["capacidad"])
        estado = datos_hab["estado"]
        precio = str(datos_hab["precio"])
        razon = datos_hab["razon"]

        print(f"{numero:<15} {tipo:<15} {capacidad:<10} {estado:<12} {precio:>10} {razon:>10}")
   
    esperarVolverMenu()

def modificarHabitacion(habitaciones):
    numero_hab = pedir_entero("Ingrese el Nro. de habitación: ")
    cod_hab = formatearCodigoHab(numero_hab)

    if cod_hab in habitaciones:
        nuevo_tipo = input("Ingrese el nuevo tipo (0 para no modificar): ")
        nueva_capacidad = str(pedir_entero("Ingrese la nueva capacidad (0 para no modificar): "))
        nuevo_estado = input("Ingrese el nuevo estado (0 para no modificar): ")
        nuevo_precio = str(pedir_entero("Ingrese el nuevo precio (0 para no modificar): "))
        
        hab_modificada = {
            cod_hab: habitaciones[cod_hab].copy()
        }

        # se actualiza solo si corresponde
        if nuevo_tipo != "0":
            hab_modificada[cod_hab]["tipo"] = nuevo_tipo
        if nueva_capacidad != "0":
            hab_modificada[cod_hab]["capacidad"] = nueva_capacidad
        if nuevo_estado != "0":
            hab_modificada[cod_hab]["estado"] = nuevo_estado
        if nuevo_precio != "0":
            hab_modificada[cod_hab]["precio"] = nuevo_precio

        if manejo_archivos.actualizarHabitacion(hab_modificada, habitaciones):
            print("Se han modificado los datos de la habitación correctamente.")
    else:
        print("Error. No hay habitación con ese Nro.")

    esperarVolverMenu()

def bajaHabitacion(habitaciones, habitaciones_baja):
    numero_hab = pedir_entero("Ingrese el Nro. de habitación: ")
    cod_hab_buscado = formatearCodigoHab(numero_hab)

    if cod_hab_buscado in habitaciones:
        # Se duplica la habitacion y se conserva su codigo
        hab_baja = {
            cod_hab_buscado: habitaciones[cod_hab_buscado].copy()
        }
        
        razon = input("Ingrese la razón de la baja: ")
        hab_baja[cod_hab_buscado]["razon"] = razon

        hab_baja[cod_hab_buscado]["estado"] = "-" # Se establece el estado como nulo, una habitacion dada de baja no tiene estado

        manejo_archivos.agregarHabitacion(hab_baja, habitaciones_baja, baja=True)
        manejo_archivos.eliminarHabitacion(cod_hab_buscado, habitaciones)

        print("La habitación ha sido dada de baja por la siguiente razón:", razon)
    else:
        print("No existe habitación con ese número.")

    esperarVolverMenu()

def reintegrarHabitacion(habitaciones, habitaciones_baja):
    numero_hab = pedir_entero("Ingrese el Nro. de habitación a reintegrar: ")
    cod_hab_buscado = formatearCodigoHab(numero_hab)

    if cod_hab_buscado in habitaciones_baja:
        # Se duplica la habitacion y se conserva su codigo
        hab_alta = {
            cod_hab_buscado: habitaciones_baja[cod_hab_buscado].copy()
        }
        hab_alta[cod_hab_buscado].pop("razon") # Se elimna la razon de la baja
        hab_alta[cod_hab_buscado]["estado"] = "Libre" # Se establece el estado como libre

        manejo_archivos.eliminarHabitacion(cod_hab_buscado, habitaciones_baja, baja=True)
        manejo_archivos.agregarHabitacion(hab_alta, habitaciones)

        print(f"La habitación Nro. {numero_hab} ha sido reintegrada correctamente.")
    else:
        print("No existe una habitación con ese número en la lista de bajas.")

    esperarVolverMenu()

def agregarHabitacion(habitaciones):
    num_hab = str(pedir_entero("Ingrese el numero de habitacion"))
    tipo = input("Ingrese el tipo de habitación: ")
    capacidad = pedir_entero("Ingrese la capacidad: ")
    estado = input("Ingrese el estado: ")
    precio = pedir_entero("Ingrese el precio: ")

    nueva_habitacion = {
        ("hab_"+num_hab): {
            "tipo": tipo,
            "capacidad": capacidad,
            "estado": estado,
            "precio": precio
        }
    }

    manejo_archivos.agregarHabitacion(nueva_habitacion, habitaciones)
    print(f"\nLa habitación {num_hab} se agregó correctamente.")
    
    esperarVolverMenu()