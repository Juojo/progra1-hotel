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