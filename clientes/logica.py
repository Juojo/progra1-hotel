from util import *

def agregarCliente(clientes):
    dni = input("Ingrese el DNI del cliente:")
    existe = False
    i = 0
    # Se busca si existe un cliente con ese DNI
    while i < len(clientes) and not existe:
        if dni == clientes[i][3]:
            existe = True
        i = i + 1
    if existe:
        print("Ya existe un cliente registrado con ese DNI.")
    else:
        nuevo_id = clientes[len(clientes)-1][0] + 1
    
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")

    nuevo_cliente = [nuevo_id, nombre, apellido, dni]
    clientes.append(nuevo_cliente)
    print("Se agrego el cliente correctamente.")
    esperarVolverMenu()

def borrarCliente(clientes):
    dni = input("Ingrese el DNI del cliente:")
    existe = False
    i = 0
    indice = -1
    # Se busca si existe un cliente con ese DNI
    while i < len(clientes) and not existe:
        if dni == clientes[i][3]:
            existe = True
            indice = i  # Se guarda la posicion del cliente
        i = i + 1
    if existe:
        clientes.pop(indice)
        print("Se ha borrado el cliente correctamente.")
    else:
        print("Error. No hay un cliente registrado con ese DNI.")
    esperarVolverMenu()

def modificarCliente(clientes):
    dni = input("Ingrese el DNI del cliente: ")

      # Creamos una lista con todos los DNIs de los clientes
    dnis = [c[3] for c in clientes]

    # Verificamos si el DNI ingresado existe
    if dni in dnis:
      
        indice = dnis.index(dni) # Obtenemos el indice del cliente con .index

        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
        nuevo_dni = input("Ingrese el nuevo DNI del cliente (0 si no quiere modificarlo): ")

        # Se verifica que el nuevo DNI no este repetido si se quiere cambiar
        if nuevo_dni != "0":
            if nuevo_dni in dnis and dnis.index(nuevo_dni) != indice:
                print("Error: ya existe otro cliente con ese DNI.")
                return clientes
            else:
                clientes[indice][3] = nuevo_dni 

        # Actualizamos nombre y apellido
        clientes[indice][1] = nuevo_nombre
        clientes[indice][2] = nuevo_apellido  
        print("Se han modificado los datos del cliente correctamente.")
    else:
        print("Error. No hay un cliente registrado con ese DNI.")

    esperarVolverMenu()
    

def mostrarClientes(clientes):
    print("-" * 68)
    print(f"{'ID':<10} {'Nombre':<20} {'Apellido':<20} {'DNI':>15}")
    print("-" * 68)
    for cliente in clientes:
        print(f"{cliente[0]:<10} {cliente[1]:<20} {cliente[2]:<20} {cliente[3]:>15}")
    esperarVolverMenu()