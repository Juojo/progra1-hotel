from menus import *

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin()

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones)
print("Fin programa")