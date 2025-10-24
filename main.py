from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal
from clientes.datos import clientes
from reservas.datos import reservas, generarPrecioTotalReservasDefault

import manejo_archivos

def main():
    habitaciones = manejo_archivos.leerArchivoJson("h") # "h" es el prefijo definido para la ruta del archivo habitaciones.json
    habitaciones_baja = manejo_archivos.leerArchivoJson("hb")

    generarPrecioTotalReservasDefault(habitaciones)
    login_exitoso = mostrarIngresarMenuLogin()

    if login_exitoso:
        mostrarIngresarMenuPrincipal(clientes, reservas, habitaciones, habitaciones_baja)
    print("Fin programa")

if __name__ == "__main__":
    main()