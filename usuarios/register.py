def ejecutarOpcionRegistrarse(usuarios):
    usuario_valido = False
    while not usuario_valido:
        usuario_nuevo = input("Ingrese un nombre de usuario: ")
        
        usuario_valido = validarRegistro(usuario_nuevo, usuarios)
        
        if usuario_valido:
            # Se pide el ingreso de una contrasena para el nuevo usuario
            contrasena_nueva = input("Ingrese su contraseña: ")
            
            # Se actualiza la tupla de usuarios
            agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios)
            
            # Se le notifica al usuario que el registro fue exitoso
            print("El usuario se ha registrado exitosamente.")
        else:
            print("Ese nombre de usuario ya existe. Elija otro.")


def validarRegistro(usuario_nuevo, usuarios):
    if usuario_nuevo == "":
        return False  # Usuario no puede estar vacío

    for usuario in usuarios:
        if usuario[0] == usuario_nuevo:
            return False  # Usuario ya existe

    return True  # Usuario válido y no existe

def agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, usuarios):
    nueva_tupla = (usuario_nuevo, contrasena_nueva)
    usuarios.append(nueva_tupla)