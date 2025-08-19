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

# Funciones login/registro

def validarLogin(usuario_ingresado, contrasena_ingresada, usuarios):
    login_exitoso = False # Por defecto se toma como que el login no es exitoso
    
    # Busca el usuario en la lista
    i = 0
    usuario_encontrado = False
    contrasena_correcta = False
    
    while usuario_encontrado == False and i<len(usuarios):
        if usuarios[i][0] == usuario_ingresado:
            usuario_encontrado = True
            if usuarios[i][1] == contrasena_ingresada:
                #contrasena_correcta = True
                login_exitoso = True # login_exitso pasa a ser True para el return de la funcion
        i+=1
            
    return login_exitoso

def validarRegistro(usuario_nuevo, usuarios_nombre):
    usuario_valido = False # Por defecto se toma como que el usuario no es valido
    
    # Se busca que el usuario ingresado no exista en la lista de usuarios_nombre
    i = 0
    usuario_ya_existe = False
    usuario_encontrado = False
    while not usuario_encontrado and i<len(usuarios_nombre):
        if usuarios_nombre[i] == usuario_nuevo:
            usuario_ya_existe = True
        i+=1

    if usuario_ya_existe == False:
        usuario_valido = True # Se cambia el usuario_valido a True para el return de la funcion
        
    # El usuario no puede estar vacio
    if usuario_nuevo == "":
        usuario_valido = False
        
    return usuario_valido

def agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios):
    usuarios.append([usuario_nuevo, contrasena_nueva])
    
def mostrarMenuLogin():
    print("------ Menú ------")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("------------------")
    print("0. Salir")
    print()
    
def ejecutarOpcionIniciarSesion(usuarios):
    # Se ingresa el usuario y la contrasena
    print()
    usuario_ingresado = input("Ingrese nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")
    
    login_exitoso = validarLogin(usuario_ingresado, contrasena_ingresada, usuarios)

    if login_exitoso:
        print("\n¡Inicio de sesión exitoso!")
        print("Bienvenido,", usuario_ingresado)
        
        salir_menu_login = True
    else:
        print("El usuario no existe o su contrasena es incorrecta.")
        
    return login_exitoso
        
def ejecutarOpcionRegistrarse(usuarios):
    usuario_valido = False
    while not usuario_valido:
        usuario_nuevo = input("Ingrese un nombre de usuario: ")
        
        usuario_valido = validarRegistro(usuario_nuevo, usuarios)
        
        if usuario_valido:
            # Se pide el ingreso de una contrasena para el nuevo usuario
            contrasena_nueva = input("Ingrese su contraseña: ")
            
            # Se actualiza las lista de usuarios y la de contrasenas
            agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios)
            
            # Se le notifica al usuario que el registro fue exitoso
            print("\nEl usuario se ha registrado exitosamente.\n")
        else:
            print("Ese nombre de usuario ya existe. Elija otro.")

def mostrarIngresarMenuLogin(usuarios):
    # Devuelve True si el login fue exitoso
    # Devuelve False si el usuario decidio salir
    
    login_exitoso = False
    
    salir_menu_login = False # Variable para controlar el ciclo principal
    
    while salir_menu_login == False and login_exitoso == False:
        mostrarMenuLogin()
        opcion = input("Elija una opción: ")

        if opcion == "1": # (Iniciar sesion)
            login_exitoso = ejecutarOpcionIniciarSesion(usuarios)
        elif opcion == "2": # (Registrarse)
            ejecutarOpcionRegistrarse(usuarios)
        elif opcion == "0": # (Salir)
            salir_menu_login = True # Sale del ciclo del menu por opcion seleccionada
        else:
            print("\nOpción no válida. Por favor intente nuevamente.\n")
    
    print()
    return login_exitoso

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

def mostrarIngresarMenuPrincipal(clientes):
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
            pass
        elif opcion_seleccionada == "6":
            pass
        elif opcion_seleccionada == "7":
            pass
        elif opcion_seleccionada == "8":
            pass
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
    pass

def darBajaReserva(reservas):
    pass

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes)
print("Fin programa")