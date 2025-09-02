from .datos import *

def ejecutarOpcionRegistrarse():
    usuario_valido = False
    while not usuario_valido:
        usuario_nuevo = input("Ingrese un nombre de usuario: ")
        
        usuario_valido = validarRegistro(usuario_nuevo, usuarios)
        
        if usuario_valido:
            # Se pide el ingreso de una contrasena para el nuevo usuario
            contrasena_nueva = input("Ingrese su contraseña: ")
            
            # Se actualiza las lista de usuarios y la de contrasenas
            agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva)
            
            # Se le notifica al usuario que el registro fue exitoso
            print("\nEl usuario se ha registrado exitosamente.\n")
        else:
            print("Ese nombre de usuario ya existe. Elija otro.")


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

def agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva):
    usuarios.append([usuario_nuevo, contrasena_nueva])
