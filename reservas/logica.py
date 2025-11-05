from util import *
from datetime import date
from functools import reduce
import json
import os

def dividir_linea_reservas(linea):
    if linea.strip() == "": # Si la línea está vacía o tiene saltos se ignora
        return None
    
    partes = linea.strip().split(";")
    if len(partes) == 7:
        id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = partes
        return id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total
    else:
        return None
    
def calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso):
    extraerDia = lambda fecha_string: int(fecha_string[:2])
    extraerMes = lambda fecha_string: int(fecha_string[3:5])
    extraerAnio = lambda fecha_string: int(fecha_string[-4:])

    date_fecha_ingreso = date(extraerAnio(fecha_ingreso), extraerMes(fecha_ingreso), extraerDia(fecha_ingreso))
    date_fecha_egreso = date(extraerAnio(fecha_egreso), extraerMes(fecha_egreso), extraerDia(fecha_egreso))
    delta = date_fecha_egreso - date_fecha_ingreso

    # Lambda para calcular el total
    calcular = lambda precio, dias: precio * dias
    return calcular(precio_habitacion, delta.days)

def buscarPrecioHabitacion(id_habitacion, habitaciones):
    # habitacion = list(filter(lambda h: h[0] == id_habitacion, lista_habitaciones))[0] # Devuelve la primera posicion de la lista
    # precio_habitacion = habitacion[4]

    cod_hab = "hab_"+str(id_habitacion)
    if cod_hab in habitaciones:
        return habitaciones[cod_hab]["precio"]
    else:
        return 0
    
'''
ARCHIVOS
'''

def mostrar_reservas(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        print(f"{'ID':<10} {'Cliente':<10} {'Habitacion':<10} {'Ingreso':<10} {'Egreso':<10} {'Precio Total':>15}")
        for linea in arch:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos
                print(f"{id_reserva:<10} {id_cliente:<10} {id_habitacion:<10} {fecha_ingreso:<10} {fecha_egreso:<10} {precio_total:>15}")
            else:
                if linea.strip() != "":
                    print("Linea con formato incorrecta.")
    except OSError as e:
        print("Error. No se pudo abrir el archivo.",e)
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo.")
    esperarVolverMenu()

def agregar_reserva(archivo_reservas, archivo_habitaciones, archivo_clientes):
    try:
        arch = open(archivo_reservas, "r", encoding="UTF-8")
        linea = arch.readline()
        while linea:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos
            linea = arch.readline()
    except FileNotFoundError:
        pass
    finally:
        try:
            arch.close()
        except:
            pass

    id_reserva = generar_id_archivo(archivo_reservas)
    print("Ingrese el ID del cliente que realiza la reserva: ", end="")
    id_cliente = pedir_entero("")
    print("Ingrese la habitacion de la reserva (ID): ", end="")
    id_habitacion = pedir_entero("")
    print("--- Ingrese la fecha de ingreso ---")
    fecha_ingreso = pedir_fecha()
    print("--- Ingrese la fecha de egreso ---")
    fecha_egreso = pedir_fecha()
    estado = True

     # Buscar el precio de la habitación
    precio_habitacion = buscarPrecioHabitacion(id_habitacion, archivo_habitaciones)

    # Calcular precio total
    precio_total = calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso)

    try:
        arch = open(archivo_reservas, "a", encoding="UTF-8")
        arch.write(f"{id_reserva};{id_cliente};{id_habitacion};{fecha_ingreso};{fecha_egreso};{estado};{precio_total}\n")
        print("Se agregó la reserva correctamente.")
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

    # Buscamos en el archivo de los clientes
    try:
        with open(archivo_clientes, "r", encoding="UTF-8") as archivo_clientes:
            clientes = archivo_clientes.readlines()
            # Busca el cliente
            cliente_encontrado = None
            for cliente in clientes:
                datos_cliente = cliente.strip().split(";")
                if len(datos_cliente) == 4 and datos_cliente[0] == str(id_cliente):
                    cliente_encontrado = datos_cliente
                    break
            if cliente_encontrado:
                print(f"Reserva registrada para {cliente_encontrado[1]} {cliente_encontrado[2]} con un costo total de ${precio_total}")
            else:
                print("Cliente no encontrado.")
    except FileNotFoundError:
        print(f"El archivo {archivo_clientes} no se encuentra disponible.")

    esperarVolverMenu()

def dar_baja_reserva(archivo_reservas):  
    print("Ingrese la ID de la reserva que quiere dar de baja: ", end="")
    id_reserva_a_borrar = pedir_entero("")
    temp = "temp.txt"
    reserva_a_borrar = False

    try:
        arch = open(archivo_reservas, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos
                if str(id_reserva) != str(id_reserva_a_borrar):
                    aux.write(linea)
                else:
                    reserva_a_borrar = True

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if reserva_a_borrar:
        try:
            os.remove(archivo_reservas)       # elimina el original
            os.rename(temp, archivo_reservas) # renombra el temporal
            print(f"La reserva se dio de baja correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  # eliminamos el temporal si no se usó
        print(f"No se encontró una reserva con ese ID")

    esperarVolverMenu()

def modificar_reserva(archivo_reservas, archivo_habitaciones):
    id_modificar = str(pedir_entero("Ingrese el ID de la reserva: "))
    temp = "temp.txt"
    reserva_modificada = False
    '''reservas_existentes = []  # Se crea una lista para verificar las habitaciones ocupadas en las reservas

    # Se cargan todas las reservas en la lista antes de modificar
    try:
        with open(archivo_reservas, "rt", encoding="UTF-8") as arch:
            for linea in arch:
                datos = dividir_linea_reservas(linea)
                if datos:
                    reservas_existentes.append(datos)
    except FileNotFoundError:
        print("El archivo de reservas no existe.")
        return
    except OSError as error:
        print("Error al acceder al archivo:", error)
        return'''

    # Se abre de nuevo para leer y escribir un temporal
    try:
        arch = open(archivo_reservas, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos

                if id_reserva == id_modificar:
                    reserva_modificada = True

                    nuevo_cliente = input("Ingrese el nuevo ID de cliente (ENTER para mantener): ")
                    if nuevo_cliente.strip() == "":
                        nuevo_cliente = id_cliente

                    print("Ingrese la nueva fecha de ingreso: ", end="")
                    nueva_fecha_ingreso = pedir_fecha()
                    if nueva_fecha_ingreso == "":
                        nueva_fecha_ingreso = fecha_ingreso

                    print("Ingrese la nueva fecha de egreso: ", end="")
                    nueva_fecha_egreso = pedir_fecha()
                    if nueva_fecha_egreso == "":
                        nueva_fecha_egreso = fecha_egreso

                    nueva_habitacion = pedir_entero("Ingrese la nueva habitación (0 para mantener): ")
                    if nueva_habitacion == 0:
                        nueva_habitacion = id_habitacion
                    '''else:
                        # Se verifica si la habitación ya está ocupada
                        ocupadas = [r[2] for r in reservas_existentes if r[5] and r[0] != id_reserva]
                        if str(nueva_habitacion) in ocupadas:
                            print("Error: La habitación ya está ocupada.")
                            aux.write(linea)  # Se deja la original sin modificar
                            continue'''
                    
                    estado = True

                    # Buscar el precio de la habitación
                    precio_habitacion = buscarPrecioHabitacion(nueva_habitacion, archivo_habitaciones)

                    # Calcular precio total
                    precio_total = calcularPrecio(precio_habitacion, fecha_ingreso, fecha_egreso)

                    nueva_linea = f"{id_reserva};{nuevo_cliente};{nueva_habitacion};{nueva_fecha_ingreso};{nueva_fecha_egreso};{estado};{precio_total}\n"
                    aux.write(nueva_linea)
                    print("La reserva ha sido modificada correctamente.")
                else:
                    aux.write(linea)
            else:
                if linea.strip() != "":
                    print("Línea con formato incorrecto en el archivo.")
                    aux.write(linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo.")

    if reserva_modificada:
        try:
            os.remove(archivo_reservas)
            os.rename(temp, archivo_reservas)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró la reserva con el ID N° {id_modificar}.")

    esperarVolverMenu()

def aplicar_descuento(archivo_reservas):
    try:
        desc = int(input("Ingrese el descuento a aplicar (0-100): "))
        if desc < 0 or desc > 100:
            print("Error: el descuento debe estar entre 0 y 100.")
            return
    except ValueError:
        print("Error: debe ingresar un número entero.")
        return

    id_reserva_desc = str(pedir_entero("Ingrese el ID de la reserva: "))
    temp = "temp.txt"
    descuento_aplicado = False

    try:
        arch = open(archivo_reservas, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = dividir_linea_reservas(linea)
            if datos:
                id_reserva, id_cliente, id_habitacion, fecha_ingreso, fecha_egreso, estado, precio_total = datos

                if id_reserva == id_reserva_desc:
                    precio_actual = float(precio_total) # se pasa a float
                    precio = [precio_actual] # se pasa a lista
                    nuevo_precio = list(map(lambda x: x * (1 - desc / 100), precio))
                    nuevo_precio_total = str(nuevo_precio[0])
                    descuento_aplicado = True              

                    nueva_linea = f"{id_reserva};{id_cliente};{id_habitacion};{fecha_ingreso};{fecha_egreso};{estado};{nuevo_precio_total}\n"
                    aux.write(nueva_linea)
                    print(f"Descuento aplicado correctamente. Nuevo precio: ${nuevo_precio[0]:.2f}")
                else:
                    aux.write(linea)
            else:
                if linea.strip() != "":
                    print("Línea con formato incorrecto en el archivo.")
                    aux.write(linea)

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo.")

    if descuento_aplicado:
        try:
            os.remove(archivo_reservas)
            os.rename(temp, archivo_reservas)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró la reserva con el ID N° {id_reserva_desc}.")

    esperarVolverMenu()