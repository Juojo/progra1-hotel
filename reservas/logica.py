from util import *
from datetime import date
from functools import reduce
import json

def calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso):
    extraerDia = lambda fecha_string: int(fecha_string[:2])
    extraerMes = lambda fecha_string: int(fecha_string[3:5])
    extraerAnio = lambda fecha_string: int(fecha_string[-4:])

    date_fecha_ingreso = date(extraerAnio(fecha_ingreso), extraerMes(fecha_ingreso), extraerDia(fecha_ingreso))
    date_fecha_egreso = date(extraerAnio(fecha_egreso), extraerMes(fecha_egreso), extraerDia(fecha_egreso))
    delta = date_fecha_egreso - date_fecha_ingreso

    # Lambda para calcular el total
    calcular = lambda precio, dias: precio * dias
    return calcular(precio_habitacion, delta.days)

def agregarReserva(reservas, habitaciones, clientes):
    imprimirTituloOpcion("Agregar reserva")

    ingresarNuevaReserva(reservas, habitaciones, clientes)
    print("La reserva se registro correctamente!")

    esperarVolverMenu()

def ingresarNuevaReserva(reservas, habitaciones, clientes):
    print("Ingrese el ID del cliente que realiza la reserva: ", end="")
    id_cliente = pedir_entero("")
    print("Ingrese la habitacion de la reserva (ID): ", end="")
    id_habitacion = pedir_entero("")
    print("--- Ingrese la fecha de ingreso ---")
    fecha_ingreso = pedir_fecha()
    print("--- Ingrese la fecha de egreso ---")
    fecha_egreso = pedir_fecha()

    id_reserva = generarId(reservas)
    estado = True

    # Buscar el precio de la habitación
    precio_habitacion = buscarPrecioHabitacion(id_habitacion, habitaciones)

    # Calcular precio total
    precio_total = calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso)

    # Se guarda la reserva
    reservas.append([id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total])

    # Busca el nombre del cliente
    cliente = list(filter(lambda c: c[0] == id_cliente, clientes))[0] # Devuelve la primera posicion de la lista
    print(f"Reserva registrada para {cliente[1]} {cliente[2]} con un costo total de ${precio_total}")


def buscarPrecioHabitacion(id_habitacion, habitaciones):
    # habitacion = list(filter(lambda h: h[0] == id_habitacion, lista_habitaciones))[0] # Devuelve la primera posicion de la lista
    # precio_habitacion = habitacion[4]

    cod_hab = "hab_"+str(id_habitacion)
    if cod_hab in habitaciones:
        return habitaciones[cod_hab]["precio"]
    else:
        return 0

def modificarReserva(reservas):
    Id_reserva = pedir_entero("Ingrese el ID de la reserva: ")

    # Se crea una lista con todos los IDs de reservas
    ids = [reserva[0] for reserva in reservas]

    # Se busca si hay una reserva con ese ID
    if Id_reserva in ids:
        
        indice = ids.index(Id_reserva)  # Obtenemos el indice de la reserva con .index

        nuevo_cliente = input("Ingrese el nuevo cliente de la reserva: ")
        print("Ingrese la nueva fecha de ingreso: ", end="")
        nueva_fecha_ingreso = pedir_fecha()
        print("Ingrese la nueva fecha de egreso: ", end="")
        nueva_fecha_egreso = pedir_fecha()
        nueva_habitacion = pedir_entero("Ingrese la nueva habitacion del cliente (0 si no quiere modificarla): ")

        # Se verifica que la nueva habitacion no esté ocupada o si no se quiere cambiar
        if nueva_habitacion != 0:
            # Creamos una lista con las habitaciones ocupadas
            ocupadas = [r[2] for r in reservas if r[5] and r != reservas[indice]]

            if nueva_habitacion in ocupadas:
                print("Error: La habitacion ya esta ocupada.")
                return reservas
            else:
                reservas[indice][2] = nueva_habitacion

        reservas[indice][1] = nuevo_cliente
        reservas[indice][3] = nueva_fecha_ingreso
        reservas[indice][4] = nueva_fecha_egreso  
        print("Se han modificado los datos de la reserva correctamente.")
    else:
        print("Error. No hay una reserva con ese ID.")

    esperarVolverMenu()

def mostrarReservas(reservas):
    print("-" * 70)
    print(f"{'ID':<10} {'Cliente':<10} {'Habitacion':<10} {'Ingreso':<10} {'Egreso':<10} {'Precio Total':>15}")
    print("-" * 70)

    validarPrint = lambda valor: valor if valor != None else "No encontrado"

    for reserva in reservas:
        print(f"{validarPrint(reserva[0]):<10} {validarPrint(reserva[1]):<10} {validarPrint(reserva[2]):<10} {validarPrint(reserva[3]):<10} {validarPrint(reserva[4]):<10} {validarPrint(reserva[6]):>15}")
    esperarVolverMenu()

def darBajaReserva(reservas):
    imprimirTituloOpcion("dar de baja una reserva")
    
    print("Ingrese la ID de la reserva que quiere dar de baja: ", end="")
    id_reserva = pedir_entero("")

    reserva_encontrada = None
    for reserva in reservas:
        if reserva[0] == id_reserva:
            reserva_encontrada = reserva
    
    if reserva_encontrada is not None:
        reserva_encontrada[5] = False
        print("La reserva se dio de baja correctamente!")
    else:
        print("No se encontró una reserva con ese ID.")

    esperarVolverMenu()

def maxPrecioReservas(reservas):
    imprimirTituloOpcion("Contar reservas con precio máximo")
    
    precios = [reserva[6] for reserva in reservas] 

    resultados_precios_maximos = {
        "precio_max": max(precios),
        "cantidad": sum(1 for reserva in reservas if reserva[6] == max(precios))
    }
    
    print(f"Precio máximo: {resultados_precios_maximos['precio_max']}")
    print(f"Cantidad de reservas con ese precio: {resultados_precios_maximos['cantidad']}")
    esperarVolverMenu()

def minYMaxPrecioReservas(reservas):
    imprimirTituloOpcion("Precio mínimo y máximo")

    precios = [reserva[6] for reserva in reservas]

    resultado_precios = {
        "precio_min": min(precios),
        "precio_max": max(precios)
    }
    
    print(f"Precio mínimo de reserva: {resultado_precios['precio_min']}")
    print(f"Precio máximo de reserva: {resultado_precios['precio_max']}")
    esperarVolverMenu()

def promedioPrecioReservas(reservas):
    imprimirTituloOpcion("Promedio de precios de reservas")

    precios = [reserva[6] for reserva in reservas]
    total = reduce(lambda total_acumulado, precio: total_acumulado + precio, precios)
    promedio = total / len(precios)
    
    print(f"Promedio de precios de las reservas: {promedio:.2f}")
    esperarVolverMenu()

archivo = "reservas/datos_reservas.txt"

def dividir_linea_reservas(linea):
    if linea.strip() == "": # Si la línea está vacía o tiene saltos se ignora
        return None
    
    partes = linea.strip().split(";")
    if len(partes) == 7:
        id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = partes
        return id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total
    else:
        return None
    
def mostrar_reservas(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        print(f"{'ID':<10} {'Cliente':<10} {'Habitacion':<10} {'Ingreso':<10} {'Egreso':<10} {'Precio Total':>15}")
        for linea in arch:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos
                print(f"{id_reserva:<10} {id_cliente:<10} {id_habitacion:<10} {fecha_ingreso:<10} {fecha_egreso:<10} {precio_total:>15}")
            else:
                if linea.strip() != "":
                    print("Linea con formato incorrecta.")
    except OSError as e:
        print("Error. No se pudo abrir el archivo.",e)
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo.")
    esperarVolverMenu()