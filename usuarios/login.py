from .datos import *

def ejecutarOpcionIniciarSesion():
    # Se ingresa el usuario y la contrasena
    print()
    usuario_ingresado = input("Ingrese nombre de usuario: ")
    contrasena_ingresada = input("Ingrese su contraseña: ")
    
    login_exitoso = validarLogin(usuario_ingresado, contrasena_ingresada)

    if login_exitoso:
        print("\n¡Inicio de sesión exitoso!")
        print("Bienvenido,", usuario_ingresado)
        
        salir_menu_login = True
    else:
        print("El usuario no existe o su contrasena es incorrecta.")
        
    return login_exitoso

def validarLogin(usuario_ingresado, contrasena_ingresada):
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