from menus import *

# Datos predefinidos

encabezados_clientes = ['Id_clientes', 'Nombre', 'Apellido', 'DNI']
clientes = [
    [1, 'Pedro', 'González', '42123456'],
    [2, 'Sofia', 'Rodríguez', '38765432'],
    [3, 'Miguel', 'Torres', '40987654'],
    [4, 'Valentina', 'Silva', '39456123'],
    [5, 'Diego', 'Morales', '41789012'],
]

encabezados_habitaciones = ['Nro_habitacion', 'Tipo', 'Capacidad', 'Estado']
habitaciones = [
    [1, 'Suite', '2', "Libre"],
    [2, 'Suite', '2', "Ocupada"],
    [3, 'Residencial', '3', "Reservada"],
    [4, 'Presidencial', '5', "Libre"],
    [5, 'Suite', '2', "Libre"],
]

encabezados_reservas = ['Id_reserva', 'Cliente', 'Habitacion', 'Fecha_ingreso', 'Fecha_egreso', 'Estado']
reservas = [
    [1, 1, 3, '04/07/2025', '12/07/2025', True],
    [2, 2, 1, '28/06/2025', '29/06/2025', True],
    [3, 3, 2, '05/07/2025', '19/07/2025', True],
    [4, 5, 4, '02/11/2025', '06/11/2025', True],
    [5, 4, 5, '27/09/2025', '02/10/2025', True],
]

usuarios = [
    ["recepcionista1", "123"],
    ["", ""]
]

# FUNCIONES GENERALES DEL MENU

def mostrarMenuPrincipal():
        print('''
--- Sistema de Reservas de Hotel ---

1. Agregar cliente
2. Modificar cliente
3. Borrar cliente
4. Mostrar clientes
5. Agregar reserva
6. Cancelar reserva
7. Modificar reserva
8. Mostrar todas las reservas
9. Ver estado de habitaciones
10. Modificar estado de habitacion
-------------------------------
0. Salir
''')
        
def imprimirTituloOpcion(titulo):
    print()
    print(f"--- {titulo.upper()} ---")
    print()
        
def mostrarIngresarVolverMenu():
    # Volver al menu principal
    print("\nPresione ENTER para volver al menú principal", end="")
    input()

    mostrarMenuPrincipal()

def limpiarPantalla():
    # \033 = ESC
    print("\033[2J") # Limpia la pantalla
    print("\033[H") # Mueve el cursor al home

def mostrarIngresarMenuPrincipal(clientes, habitaciones, reservas):
    mostrarMenuPrincipal()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            agregarCliente(clientes)
        elif opcion_seleccionada == "2":
            modificarCliente(clientes)
        elif opcion_seleccionada == "3":
            borrarCliente(clientes)
        elif opcion_seleccionada == "4":
            mostrarClientes(clientes)
        elif opcion_seleccionada == "5":
            agregarReserva(reservas)
        elif opcion_seleccionada == "6":
            darBajaReserva(reservas)
        elif opcion_seleccionada == "7":
            modificarReserva(reservas)
        elif opcion_seleccionada == "8":
            mostrarReservas(reservas)
        elif opcion_seleccionada == "9":
            pass
        elif opcion_seleccionada == "10":
            pass
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

# Clientes

def agregarCliente(clientes):
    dni = input("Ingrese el DNI del cliente:")
    existe = False
    # Se busca si existe un cliente con ese DNI
    for i in range(len(clientes)):
        if clientes[i][3] == dni:
            existe = True
    if existe:
        print("Ya existe un cliente registrado con ese DNI.")
    else:
        nuevo_id = clientes[len(clientes)-1][0] + 1
    
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")

    nuevo_cliente = [nuevo_id, nombre, apellido, dni]
    clientes.append(nuevo_cliente)
    print("Se agrego el cliente correctamente.")
    mostrarIngresarVolverMenu()

def borrarCliente(clientes):
    dni = input("Ingrese el DNI del cliente:")
    existe = False
    # Se busca si existe un cliente con ese DNI
    for i in range(len(clientes)):
        if clientes[i][3] == dni:
            existe = True
            indice = i  # Se guarda la posicion del cliente
    if existe:
        clientes.pop(indice)
        print("Se ha borrado el cliente correctamente.")
    else:
        print("Error. No hay un cliente registrado con ese DNI.")
    mostrarIngresarVolverMenu()

def modificarCliente(clientes):
    dni = input("Ingrese el DNI del cliente: ")
    existe = False
    # Se busca si existe un cliente con ese DNI
    for i in range(len(clientes)):
        if clientes[i][3] == dni:
            existe = True
            indice = i

    if existe:
        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
        nuevo_dni = input("Ingrese el nuevo DNI del cliente (0 si no quiere modificarlo): ")

        # Se verifica que el nuevo DNI no esté repetido si no lo quiere cambiar
        if nuevo_dni != "0":  
            repetido = False
            for j in range(len(clientes)):
                if j != indice and clientes[j][3] == nuevo_dni:
                    repetido = True

            if repetido:
                print("Error: ya existe otro cliente con ese DNI.")
                return clientes
            else:
                clientes[indice][3] = nuevo_dni
            
        clientes[indice][1] = nuevo_nombre
        clientes[indice][2] = nuevo_apellido  
        print("Se han modificado los datos del cliente correctamente.")
    else:
        print("Error. No hay un cliente registrado con ese DNI.")

    mostrarIngresarVolverMenu()
    

def mostrarClientes(clientes):
    print(f"{'ID':<10} {'Nombre':<10} {'Apellido':<10} {'DNI'}")
    print("-" * 40)
    for cliente in clientes:
        print(f"{cliente[0]:<10} {cliente[1]:<10} {cliente[2]:<10} {cliente[3]}")
    mostrarIngresarVolverMenu()

# Reservas

def agregarReserva(reservas):
    imprimirTituloOpcion("Agregar reserva")

    ingresarNuevaReserva(reservas)
    print("La reserva se registro correctamente!")

    mostrarIngresarVolverMenu()

def ingresarNuevaReserva(reservas):
    print("Ingrese el ID del cliente que realiza la reserva: ", end="")
    id_cliente = input()
    print("Ingrese la habitacion de la reserva (ID): ", end="")
    id_habitacion = input()
    print("Ingrese la fecha de ingreso: ", end="")
    fecha_ingreso = input()
    print("Ingrese la fecha de egreso: ", end="")
    fecha_egreso = input()

    id_reserva = generarId(reservas)
    estado = True

    reservas.append([id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado])

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

    mostrarIngresarVolverMenu()

def mostrarReservas(reservas):
    print(f"{'ID':<10} {'Cliente':<10} {'Habitacion':<10} {'Ingreso':<10} {'Egreso':<10}")
    print("-" * 40)
    for reserva in reservas:
        print(f"{reserva[0]:<10} {reserva[1]:<10} {reserva[2]:<10} {reserva[3]} {reserva[4]} ")
    mostrarIngresarVolverMenu()

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

    mostrarIngresarVolverMenu()


# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes, habitaciones, reservas)
print("Fin programa")