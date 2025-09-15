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

    opcion_seleccionada = "" # Se inicializa la variable

    while opcion_seleccionada != "0":
        opcion_seleccionada = input("Seleccione una opción: ")   
        
        if opcion_seleccionada == "1":
            promedioPrecioReservas(reservas)
        elif opcion_seleccionada == "2":
            maxPrecioReservas(reservas)
        elif opcion_seleccionada == "3":
            minYMaxPrecioReservas(reservas)
        else:
            if opcion_seleccionada != "0":
                print()
                print("Opción no válida.")
                print()

        mostrarMenuEstadisticas()