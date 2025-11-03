from util import *
from functools import reduce

def contPrecioMaxReservas(reservas):
    imprimirTituloOpcion("Contar reservas con precio máximo")
    
    precios = [reserva[6] for reserva in reservas] 

    resultados_precios_maximos = {
        "precio_max": max(precios),
        "cantidad": sum(1 for reserva in reservas if reserva[6] == max(precios))
    }
    
    print(f"Precio máximo: {resultados_precios_maximos['precio_max']}")
    print(f"Cantidad de reservas con ese precio: {resultados_precios_maximos['cantidad']}")
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

def minYMaxPrecioReservas(reservas):
    imprimirTituloOpcion("Precio mínimo y máximo")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        esperarVolverMenu()
        return

    minimo = minPrecioReserva(reservas)
    maximo = maxPrecioReserva(reservas)

    print(f"Precio mínimo de reserva: {minimo}")
    print(f"Precio máximo de reserva: {maximo}")
    esperarVolverMenu()

def promedioPrecioReservas(reservas):
    imprimirTituloOpcion("Promedio de precios de reservas")

    precios = [reserva[6] for reserva in reservas]
    total = reduce(lambda total_acumulado, precio: total_acumulado + precio, precios)
    promedio = total / len(precios)
    
    print(f"Promedio de precios de las reservas: {promedio:.2f}")
    esperarVolverMenu()
