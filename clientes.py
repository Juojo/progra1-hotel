from util import *

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