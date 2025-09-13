from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal
from clientes.datos import clientes
from reservas.datos import reservas, generarPrecioTotalReservasDefault
from habitaciones.datos import habitaciones

# Programa Principal

generarPrecioTotalReservasDefault(habitaciones)
login_exitoso = mostrarIngresarMenuLogin()

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones)
print("Fin programa")