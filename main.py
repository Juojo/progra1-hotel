from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal
from clientes.datos import clientes
from reservas.datos import reservas, generarPrecioTotalReservasDefault

import manejo_archivos

habitaciones = manejo_archivos.leerArchivoJson("h") # "h" es el prefijo definido para la ruta del archivo habitaciones.json

if __name__ == "__main__":
    generarPrecioTotalReservasDefault(habitaciones)
    login_exitoso = mostrarIngresarMenuLogin()

    if login_exitoso:
        mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones)
    print("Fin programa")