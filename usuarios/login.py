def ejecutarOpcionIniciarSesion(usuarios):
    # Se ingresa el usuario y la contrasena
    print()
    usuario_ingresado = input("Ingrese nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")
    
    login_exitoso = validarLogin(usuario_ingresado, contrasena_ingresada, usuarios)

    if login_exitoso:
        print("¡Inicio de sesión exitoso!")
        print("Bienvenido,", usuario_ingresado)
    else:
        print("El usuario no existe o su contrasena es incorrecta.")
        
    return login_exitoso

def validarLogin(usuario_ingresado, contrasena_ingresada, usuarios):
    for nombre, contrasena, mail in usuarios:
        if nombre == usuario_ingresado and contrasena == contrasena_ingresada:
            return True  # Login exitoso
    return False  # No se encontró o contraseña incorrecta