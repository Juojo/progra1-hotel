from reservas import *

def mostrarMenuReservas():
    print("""
----------------------------------------
               Menú Reservas
----------------------------------------
1. Agregar Reserva
2. Modificar Reserva
3. Cancelar Reserva
4. Mostrar Reservas
5. Aplicar descuento
----------------------------------------
0. Volver
----------------------------------------
""")
        
def mostrarIngresarMenuReservas(archivo_reservas, archivo_habitaciones, archivo_clientes):    
    mostrarMenuReservas()

    opcion_seleccionada = -1 # Se inicializa la variable

    while opcion_seleccionada != 0:
        while True:
            try:
                opcion_seleccionada = int(input("Elija una opción: "))
                break
            except ValueError:
                print("Error: Solo se permite el ingreso de numeros enteros")
                mostrarMenuReservas()
            except Exception as e:
                print("Error no contemplado:", type(e).__name__)
                mostrarMenuReservas()
        
        if opcion_seleccionada == 1:
            agregar_reserva(archivo_reservas, archivo_habitaciones, archivo_clientes)
        elif opcion_seleccionada == 2:
            modificar_reserva(archivo_reservas)
        elif opcion_seleccionada == 3:
            dar_baja_reserva(archivo_reservas)
        elif opcion_seleccionada == 4:
            mostrar_reservas(archivo_reservas)
        elif opcion_seleccionada == 5:
            aplicar_descuento(archivo_reservas)
        else:
            if opcion_seleccionada != 0:
                print()
                print("Opción no válida.")
                print()

        if opcion_seleccionada != 0:
            mostrarMenuReservas() # Muestra el print del menu luego de salir de la opcion seleccionada