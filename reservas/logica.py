from util import *
from datetime import date

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
    id_cliente = pedir_entero()
    print("Ingrese la habitacion de la reserva (ID): ", end="")
    id_habitacion = pedir_entero()
    print("Ingrese la fecha de ingreso (dd/mm/yyyy): ", end="")
    fecha_ingreso = input()
    print("Ingrese la fecha de egreso (dd/mm/yyyy): ", end="")
    fecha_egreso = input()

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
    habitacion = list(filter(lambda h: h[0] == id_habitacion, habitaciones))[0] # Devuelve la primera posicion de la lista
    precio_habitacion = habitacion[4]

    return precio_habitacion

def modificarReserva(reservas):
    Id_reserva = pedir_entero("Ingrese el ID de la reserva: ")

     # Se crea una lista con todos los IDs de reservas
    ids = [reserva[0] for reserva in reservas]

    # Se busca si hay una reserva con ese ID
    if Id_reserva in ids:
        
        indice = ids.index(Id_reserva)  # Obtenemos el indice de la reserva con .index

        nuevo_cliente = input("Ingrese el nuevo cliente de la reserva: ")
        nueva_fecha_ingreso = input("Ingrese la nueva fecha de ingreso: ")
        nueva_fecha_egreso = input("Ingrese la nueva fecha de egreso: ")
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
    id_reserva = input()

    encontrado = False
    i = 0
    while i<len(reservas) and encontrado == False:
        if reservas[i][0] == id_reserva:
            encontrado = True
            reservas[i][5] = False
        i+=1

    print("La reserva se dio de baja correctamente!")

    esperarVolverMenu()