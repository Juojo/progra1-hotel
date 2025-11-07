from util import generarId
from usuarios.register import validarMail
from usuarios.register import validarRegistro

def test_generarId():
    matriz = [
        [1],
        [2]
    ]
    assert generarId(matriz) == 3 # El nuevo ID deberia ser matriz[ultima_posicion][0] + 1

def test_validarRegistro():
    usuarios_ejemplo = [
        ("Pedro", "contrasena", "mail@gmail.com"),
    ]
    assert validarRegistro("Pedro", usuarios_ejemplo) == False # No se puede registrar el usuario si ya existe uno con el mismo nombre
    assert validarRegistro("", usuarios_ejemplo) == False # No se puede registrar un usuario sin nombre
    assert validarRegistro("Alex", usuarios_ejemplo) == True # Ejemplo valido

def test_validar_mail():
    assert validarMail("juan@gmail.com") == True # El mail es correcto porque termina en @gmail.com
    assert validarMail("juan@yahoo.com.ar") == False # El mail es incorrecto porque no termina en @gmail.com