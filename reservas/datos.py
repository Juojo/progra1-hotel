from .logica import calcularPrecio, buscarPrecioHabitacion

encabezados_reservas = ['Id_reserva', 'Cliente', 'Habitacion', 'Fecha_ingreso', 'Fecha_egreso', 'Estado', 'Precio_total']
reservas = [
    [1, 1, 202, '04/07/2025', '12/07/2025', True, None],
    [2, 2, 202, '13/07/2025', '14/07/2025', True, None],
    # [2, 2, 101, '28/06/2025', '29/06/2025', True, None],
    # [3, 3, 404, '05/07/2025', '19/07/2025', True, None],
    # [4, 5, 202, '02/11/2025', '06/11/2025', True, None],
    # [5, 4, 202, '27/09/2025', '02/10/2025', True, None],
]

# Esta funcion se ejecuta por unica vez cuando se corre el programa.
def generarPrecioTotalReservasDefault(habitaciones):
    for reserva in reservas:
        reserva[6] = calcularPrecio(buscarPrecioHabitacion(reserva[2], habitaciones), reserva[3], reserva[4])