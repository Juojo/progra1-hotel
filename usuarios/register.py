import re

def ejecutarOpcionRegistrarse(usuarios):
    usuario_valido = False
    while not usuario_valido:
        usuario_nuevo = input("Ingrese un nombre de usuario: ")
        
        usuario_valido = validarRegistro(usuario_nuevo, usuarios)
        
        if usuario_valido:
            # Se pide el ingreso de una contraseña para el nuevo usuario y se valida
            while True:
                contrasena_nueva = input("Ingrese su contraseña (mínimo 8 caracteres, 1 mayúscula, 1 minúscula, 1 número y 1 carácter especial): ")
                if validarContrasena(contrasena_nueva):
                    break
                else:
                    print("Contraseña inválida. Debe tener al menos 8 caracteres, incluir mayúscula, minúscula, número y carácter especial.")

            while True:
                mail_nuevo = input("Ingrese su correo electrónico (gmail): ")
                if validarMail(mail_nuevo):
                    break
                else:
                    print("Correo inválido. Debe ser un gmail. Intente nuevamente.")

            # Se actualiza la tupla de usuarios
            agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, mail_nuevo, usuarios)
            
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

def validarMail(mail):
    patron = r'.+@gmail\.com$'
    if re.match(patron, mail):
        return True
    else:
        return False


def validarContrasena(contrasena):
   
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return True if re.match(patron, contrasena) else False


def agregarUsuarioNuevo(usuario_nuevo, contrasena_nueva, mail_nuevo, usuarios):
    nueva_tupla = (usuario_nuevo, contrasena_nueva, mail_nuevo)
    usuarios.append(nueva_tupla)