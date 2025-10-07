from reservas import promedioPrecioReservas, maxPrecioReservas, minYMaxPrecioReservas

def mostrarMenuEstadisticas():
            print("""
----------------------------------------
            Menú Estadisticas
----------------------------------------
1. Promedio de precios de reservas
2. Contar reservas con precio máximo
3. Precio mínimo y máximo
----------------------------------------
0. Volver
----------------------------------------
""")

def mostrarIngresarMenuEstadisticas(reservas):    
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
            promedioPrecioReservas(reservas)
        elif opcion_seleccionada == 2:
            maxPrecioReservas(reservas)
        elif opcion_seleccionada == 3:
            minYMaxPrecioReservas(reservas)
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuEstadisticas()