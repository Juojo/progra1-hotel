from util import *
from functools import reduce
from reservas.logica import dividir_linea_reservas

def contPrecioMaxReservas(archivo_reservas):
    imprimirTituloOpcion("Contar reservas con precio máximo")

    try:
        with open(archivo_reservas, "rt", encoding="UTF-8") as arch:
            reservas = [dividir_linea_reservas(linea) for linea in arch if dividir_linea_reservas(linea)]
    except FileNotFoundError:
        print("El archivo no existe.")
        esperarVolverMenu()
        return

    if not reservas:
        print("No hay reservas registradas.")
        esperarVolverMenu()
        return

    precios = [float(reserva[6]) for reserva in reservas]
    precio_max = max(precios)
    cantidad_max = sum(1 for p in precios if p == precio_max)

    print(f"Precio máximo: ${precio_max:.2f}")
    print(f"Cantidad de reservas con ese precio: {cantidad_max}")
    esperarVolverMenu()

def minPrecioReserva(reservas, i=0):
    if i == len(reservas) - 1:
        return reservas[i][6] # Caso base
    # Llamadas recursivas
    else:
        minimo_siguiente = minPrecioReserva(reservas, i + 1)
        if reservas[i][6] <= minimo_siguiente:
            return reservas[i][6]
        else:
            return minimo_siguiente

def maxPrecioReserva(reservas, i=0):
    if i == len(reservas) - 1:
        return reservas[i][6]  # Caso base
    # Llamadas recursivas
    else:
        max_siguiente = maxPrecioReserva(reservas, i + 1)
        if reservas[i][6] >= max_siguiente:
            return reservas[i][6]
        else:
            return max_siguiente

def minYMaxPrecioReservas(archivo_reservas):
    imprimirTituloOpcion("Precio mínimo y máximo")

    try:
        with open(archivo_reservas, "rt", encoding="UTF-8") as arch:
            reservas = [dividir_linea_reservas(linea) for linea in arch if dividir_linea_reservas(linea)]
    except FileNotFoundError:
        print("El archivo no existe.")
        esperarVolverMenu()
        return

    if not reservas:
        print("No hay reservas registradas.")
        esperarVolverMenu()
        return

    minimo = minPrecioReserva(reservas)
    maximo = maxPrecioReserva(reservas)

    print(f"Precio mínimo de reserva: ${float(minimo):.2f}")
    print(f"Precio máximo de reserva: ${float(maximo):.2f}")
    esperarVolverMenu()

def promedioPrecioReservas(archivo_reservas):
    imprimirTituloOpcion("Promedio de precios de reservas")

    try:
        with open(archivo_reservas, "rt", encoding="UTF-8") as arch:
            reservas = [dividir_linea_reservas(linea) for linea in arch if dividir_linea_reservas(linea)]
    except FileNotFoundError:
        print("El archivo no existe.")
        esperarVolverMenu()
        return

    if not reservas:
        print("No hay reservas registradas.")
        esperarVolverMenu()
        return

    precios = [float(reserva[6]) for reserva in reservas]
    total = reduce(lambda total_acumulado, precio: total_acumulado + precio, precios)
    promedio = total / len(precios)

    print(f"Promedio de precios de las reservas: ${promedio:.2f}")
    esperarVolverMenu()