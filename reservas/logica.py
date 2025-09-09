from util import *

def calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso):
    # Sacamos solo el día
    dia_ingreso = int(fecha_ingreso[:2])
    dia_egreso = int(fecha_egreso[:2])
    dias = dia_egreso - dia_ingreso

    # Lambda para calcular el total
    calcular = lambda precio, dias: precio * dias
    return calcular(precio_habitacion, dias)

def agregarReserva(reservas, habitaciones, clientes):
    imprimirTituloOpcion("Agregar reserva")

    ingresarNuevaReserva(reservas, habitaciones, clientes)
    print("La reserva se registro correctamente!")

    esperarVolverMenu()

def ingresarNuevaReserva(reservas, habitaciones, clientes):
    print("Ingrese el ID del cliente que realiza la reserva: ", end="")
    id_cliente = int(input())
    print("Ingrese la habitacion de la reserva (ID): ", end="")
    id_habitacion = int(input())
    print("Ingrese la fecha de ingreso (dd/mm/yyyy): ", end="")
    fecha_ingreso = input()
    print("Ingrese la fecha de egreso (dd/mm/yyyy): ", end="")
    fecha_egreso = input()

    id_reserva = generarId(reservas)
    estado = True

    # Buscar el precio de la habitación
    habitacion = list(filter(lambda h: h[0] == id_habitacion, habitaciones))[0] # Devuelve la primera posicion de la lista
    precio_habitacion = habitacion[4]

    # Calcular precio total
    precio_total = calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso)

    # Se guarda la reserva
    reservas.append([id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total])

    # Busca el nombre del cliente
    cliente = list(filter(lambda c: c[0] == id_cliente, clientes))[0] # Devuelve la primera posicion de la lista
    print(f"Reserva registrada para {cliente[1]} {cliente[2]} con un costo total de ${precio_total}")


def generarId(matriz):
    nuevoId = 1

    if len(matriz) != 0:
        ultimoId = matriz[len(matriz)-1][0]
        nuevoId = ultimoId + 1

    return nuevoId

def modificarReserva(reservas):
    Id_reserva = int(input("Ingrese el ID de la reserva: "))
    existe = False
    # Se busca si existe una reserva con ese ID
    for i in range(len(reservas)):
        if reservas[i][0] == Id_reserva:
            existe = True
            indice = i

    if existe:
        nuevo_cliente = input("Ingrese el nuevo cliente de la reserva: ")
        nueva_fecha_ingreso = input("Ingrese la nueva fecha de ingreso: ")
        nueva_fecha_egreso = input("Ingrese la nueva fecha de egreso: ")
        nueva_habitacion = int(input("Ingrese la nueva habitacion del cliente (0 si no quiere modificarla): "))
        # Se verifica que la nueva habitacion no este ocupada o si no se quiere cambiar
        if nueva_habitacion != 0:  
            repetido = False
            for j in range(len(reservas)):
                if j != indice and reservas[j][2] == nueva_habitacion and reservas[j][5] == True:
                    repetido = True

            if repetido:
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
    print(f"{'ID':<10} {'Cliente':<10} {'Habitacion':<10} {'Ingreso':<10} {'Egreso':<10} {'Precio Total'}")
    print("-" * 40)
    for reserva in reservas:
        print(f"{reserva[0]:<10} {reserva[1]:<10} {reserva[2]:<10} {reserva[3]:<10} {reserva[4]:<10} {reserva[6]}")
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