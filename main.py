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

usuarios = [
    ["recepcionista1", "123"],
    ["", ""]
]

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal(habitaciones)
print("Fin programa")