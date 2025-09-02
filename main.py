from menus import mostrarIngresarMenuLogin, mostrarIngresarMenuPrincipal

# Datos predefinidos

encabezados_habitaciones = ['Nro_habitacion', 'Tipo', 'Capacidad', 'Estado']
habitaciones = [
    [1, 'Suite', '2', "Libre"],
    [2, 'Suite', '2', "Ocupada"],
    [3, 'Residencial', '3', "Reservada"],
    [4, 'Presidencial', '5', "Libre"],
    [5, 'Suite', '2', "Libre"],
]

encabezados_reservas = ['Id_reserva', 'Cliente', 'Habitacion', 'Fecha_ingreso', 'Fecha_egreso', 'Estado']
reservas = [
    [1, 1, 3, '04/07/2025', '12/07/2025', True],
    [2, 2, 1, '28/06/2025', '29/06/2025', True],
    [3, 3, 2, '05/07/2025', '19/07/2025', True],
    [4, 5, 4, '02/11/2025', '06/11/2025', True],
    [5, 4, 5, '27/09/2025', '02/10/2025', True],
]

usuarios = [
    ["recepcionista1", "123"],
    ["", ""]
]

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal(habitaciones, reservas)
print("Fin programa")