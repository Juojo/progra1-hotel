from menus.menu_principal import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal
from reservas.datos import reservas, generarPrecioTotalReservasDefault

def main():
    archivo_clientes = "clientes/datos_clientes.txt"
    ruta_habitaciones = "./informacion_almacenada/habitaciones.json"
    ruta_habitaciones_baja = "./informacion_almacenada/habitaciones_baja.json"

    generarPrecioTotalReservasDefault(ruta_habitaciones)
    login_exitoso = mostrarIngresarMenuLogin()

    if login_exitoso:
        mostrarIngresarMenuPrincipal(archivo_clientes, reservas, ruta_habitaciones, ruta_habitaciones_baja)
    print("Fin programa")

if __name__ == "__main__":
    main()