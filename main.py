from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal
from clientes.datos import clientes
from reservas.datos import reservas
from habitaciones.datos import habitaciones

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin()

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones)
print("Fin programa")