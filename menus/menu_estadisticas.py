from estadisticas import promedioPrecioReservas, contPrecioMaxReservas, minYMaxPrecioReservas

def mostrarMenuEstadisticas():
            print("""
----------------------------------------
            Menú Estadisticas
----------------------------------------
1. Promedio de precios de reservas
2. Precio mínimo y máximo de reserva
3. Contar reservas con precio máximo
----------------------------------------
0. Volver
----------------------------------------
""")

def mostrarIngresarMenuEstadisticas(archivo_reservas):    
    mostrarMenuEstadisticas()

    opcion_seleccionada = -1

    while opcion_seleccionada != 0:
        while True:
            try:
                opcion_seleccionada = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuEstadisticas()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuEstadisticas()   
        
        if opcion_seleccionada == 1:
            promedioPrecioReservas(archivo_reservas)
        elif opcion_seleccionada == 2:
            minYMaxPrecioReservas(archivo_reservas)
        elif opcion_seleccionada == 3:
            contPrecioMaxReservas(archivo_reservas)
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuEstadisticas()