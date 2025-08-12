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

# Listas paralelas de usuarios
usuarios_nombre = ["usuario1", "usuario2"]
usuarios_contrasena = ["1234", "5678"]

# Funciones login/registro

def validarLogin(usuario_ingresado, contrasena_ingresada, usuarios_nombre, usuarios_contrasena):
    login_exitoso = False # Por defecto se toma como que el login no es exitoso
    
    # Busca el usuario en la lista
    i = 0
    usuario_encontrado = False
    contrasena_correcta = False
    
    while usuario_encontrado == False and i<len(usuarios_nombre):
        if usuarios_nombre[i] == usuario_ingresado:
            usuario_encontrado = True
            if usuarios_contrasena[i] == contrasena_ingresada:
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

def agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios_nombre, usuarios_contrasena):
    usuarios_nombre.append(usuario_nuevo)
    usuarios_contrasena.append(contrasena_nueva)
    
def mostrarMenuLogin():
    print("------ Menú ------")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("------------------")
    print("0. Salir")
    print()
    
def ejecutarOpcionIniciarSesion(usuarios_nombre, usuarios_contrasena):
    # Se ingresa el usuario y la contrasena
    print()
    usuario_ingresado = input("Ingrese nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")
    
    login_exitoso = validarLogin(usuario_ingresado, contrasena_ingresada, usuarios_nombre, usuarios_contrasena)

    if login_exitoso:
        print("\n¡Inicio de sesión exitoso!")
        print("Bienvenido,", usuario_ingresado)
        
        salir_menu_login = True
    else:
        print("El usuario no existe o su contrasena es incorrecta.")
        
    return login_exitoso
        
def ejecutarOpcionRegistrarse(usuarios_nombre, usuarios_contrasena):
    usuario_valido = False
    while not usuario_valido:
        usuario_nuevo = input("Ingrese un nombre de usuario: ")
        
        usuario_valido = validarRegistro(usuario_nuevo, usuarios_nombre)
        
        if usuario_valido:
            # Se pide el ingreso de una contrasena para el nuevo usuario
            contrasena_nueva = input("Ingrese su contraseña: ")
            
            # Se actualiza las lista de usuarios y la de contrasenas
            agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios_nombre, usuarios_contrasena)
            
            # Se le notifica al usuario que el registro fue exitoso
            print("\nEl usuario se ha registrado exitosamente.\n")
        else:
            print("Ese nombre de usuario ya existe. Elija otro.")

def mostrarIngresarMenuLogin(usuarios_nombre, usuarios_contrasena):
    # Devuelve True si el login fue exitoso
    # Devuelve False si el usuario decidio salir
    
    login_exitoso = False
    
    salir_menu_login = False # Variable para controlar el ciclo principal
    
    while salir_menu_login == False and login_exitoso == False:
        mostrarMenuLogin()
        opcion = input("Elija una opción: ")

        if opcion == "1": # (Iniciar sesion)
            login_exitoso = ejecutarOpcionIniciarSesion(usuarios_nombre, usuarios_contrasena)
        elif opcion == "2": # (Registrarse)
            ejecutarOpcionRegistrarse(usuarios_nombre, usuarios_contrasena)
        elif opcion == "0": # (Salir)
            salir_menu_login = True # Sale del ciclo del menu por opcion seleccionada
        else:
            print("\nOpción no válida. Por favor intente nuevamente.\n")
    
    print()
    return login_exitoso

# Clientes

def agregarCliente():
    pass

# Reservas

def agregarReserva():
    pass

def modificarReserva(id_reserva):
    pass

def darBajaReserva(id_reserva):
    pass

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios_nombre, usuarios_contrasena)

if login_exitoso:
    print("Inicio programa")

print("Fin programa")