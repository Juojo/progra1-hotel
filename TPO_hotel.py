from menus import *

# Datos predefinidos

encabezados_clientes = ['Id_clientes', 'Nombre', 'Apellido', 'DNI']
clientes = [
    [1, 'Pedro', 'González', '42123456'],
    [2, 'Sofia', 'Rodríguez', '38765432'],
    [3, 'Miguel', 'Torres', '40987654'],
    [4, 'Valentina', 'Silva', '39456123'],
    [5, 'Diego', 'Morales', '41789012'],
]

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

# FUNCIONES GENERALES DEL MENU

def mostrarMenuPrincipal():
        print('''
--- Sistema de Reservas de Hotel ---

1. Agregar cliente
2. Modificar cliente
3. Borrar cliente
4. Mostrar clientes
5. Agregar reserva
6. Cancelar reserva
7. Modificar reserva
8. Mostrar todas las reservas
9. Ver estado de habitaciones
10. Modificar estado de habitacion
-------------------------------
0. Salir
''')

def mostrarIngresarMenuPrincipal(clientes, habitaciones, reservas):
    mostrarMenuPrincipal()
    
    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")
        
        if opcion_seleccionada == "1":
            agregarCliente(clientes)
        elif opcion_seleccionada == "2":
            modificarCliente(clientes)
        elif opcion_seleccionada == "3":
            borrarCliente(clientes)
        elif opcion_seleccionada == "4":
            mostrarClientes(clientes)
        elif opcion_seleccionada == "5":
            agregarReserva(reservas)
        elif opcion_seleccionada == "6":
            darBajaReserva(reservas)
        elif opcion_seleccionada == "7":
            modificarReserva(reservas)
        elif opcion_seleccionada == "8":
            mostrarReservas(reservas)
        elif opcion_seleccionada == "9":
            pass
        elif opcion_seleccionada == "10":
            pass
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

# Programa Principal

login_exitoso = mostrarIngresarMenuLogin(usuarios)

if login_exitoso:
    mostrarIngresarMenuPrincipal(clientes, habitaciones, reservas)
print("Fin programa")