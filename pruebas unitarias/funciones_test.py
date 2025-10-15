from util import generarId
from usuarios.login import validarLogin
from usuarios.register import validarMail

def test_generarId():
    matriz = [
    [1, 'Pedro', 'González', '42123456'],
    [2, 'Sofia', 'Rodríguez', '38765432'],
    [3, 'Miguel', 'Torres', '40987654'],
    [4, 'Valentina', 'Silva', '39456123'],
    [5, 'Diego', 'Morales', '41789012'],
    ]
    assert generarId(matriz) == 6

def test_validar_login():
    usuarios_tupla = [
    ("juan", "1234", "juan@gmail.com"),
    ("jose", "5678", "jose@email.com"),
    ]
    assert validarLogin("juan", "1234", usuarios_tupla) == True
    assert validarLogin("lucas", "1234", usuarios_tupla) == False

def test_validar_mail():
    assert validarMail("juan@gmail.com") == True
    assert validarMail("juan@yahoo.com.ar") == False