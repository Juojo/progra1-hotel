from .datos import *
from util import *

def agregarCliente():
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

def borrarCliente():
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

def modificarCliente():
    dni = input("Ingrese el DNI del cliente: ")
    existe = False
    i = 0
    indice = -1
    # Se busca si existe un cliente con ese DNI
    while i < len(clientes) and not existe:
        if dni == clientes[i][3]:
            existe = True
            indice = i
        i = i + 1
        

    if existe:
        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
        nuevo_dni = input("Ingrese el nuevo DNI del cliente (0 si no quiere modificarlo): ")

        # Se verifica que el nuevo DNI no esté repetido si no lo quiere cambiar
        if nuevo_dni != "0":  
            repetido = False
            j = 0
            while j < len(clientes):
                if j != indice and clientes[j][3] == nuevo_dni:
                    repetido = True
                j = j + 1

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

    esperarVolverMenu()
    

def mostrarClientes():
    print(f"{'ID':<10} {'Nombre':<10} {'Apellido':<10} {'DNI'}")
    print("-" * 40)
    for cliente in clientes:
        print(f"{cliente[0]:<10} {cliente[1]:<10} {cliente[2]:<10} {cliente[3]}")
    esperarVolverMenu()