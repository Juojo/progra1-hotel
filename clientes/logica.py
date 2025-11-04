from util import *
import os

# def cargar_matriz_en_archivo(clientes, archivo):
#     try:
#         lineas = [f"{id};{nombre};{apellido};{dni}\n" for id, nombre, apellido, dni in clientes]
#         arch = open(archivo, "wt",encoding="UTF-8")
#         arch.writelines(lineas)
#     except OSError as mensaje:
#         print("No se puede grabar el archivo:", mensaje)
#     finally:
#         try:
#             arch.close()
#         except NameError:
#             pass

def mostrar_clientes(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        print(f"{'ID':<10} {'Nombre':<20} {'Apellido':<20} {'DNI':>15}")
        for linea in arch:
            datos = dividir_linea_clientes(linea)
            if datos:
                id, nombre, apellido, dni = datos
                print(f"{id:<10} {nombre:<20} {apellido:<20} {dni:>15}")
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

def agregar_cliente(archivo):    
    nuevo_dni = str(pedir_entero("Ingrese el DNI del cliente: "))
    cliente_existente = False

    try:
        arch = open(archivo, "r", encoding="UTF-8")
        linea = arch.readline()
        while linea:
            datos = dividir_linea_clientes(linea)
            if datos:
                id, nombre, apellido, dni = datos
                if dni == nuevo_dni:
                    cliente_existente = True
                    break
            linea = arch.readline()
    except FileNotFoundError:
        pass
    finally:
        try:
            arch.close()
        except:
            pass

    if cliente_existente:
        print("Ya existe un cliente con ese DNI.")
        esperarVolverMenu()
        return
    else:
        nuevo_id = generar_id_archivo(archivo)
        nuevo_nombre = input("Ingrese el nombre del cliente: ")
        nuevo_apellido = input("Ingrese el apellido del cliente: ")

    try:
        arch = open(archivo, "a", encoding="UTF-8")
        arch.write(f"{nuevo_id};{nuevo_nombre};{nuevo_apellido};{nuevo_dni}\n")
        print("Se agregó el cliente correctamente.")
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
    esperarVolverMenu()

def dividir_linea_clientes(linea):
    if linea.strip() == "": # Si la línea está vacía o tiene saltos se ignora
        return None
    
    partes = linea.strip().split(";")
    if len(partes) == 4:
        id, nombre, apellido, dni = partes
        return id, nombre, apellido, dni
    else:
        return None

def baja_cliente(archivo):    
    dni_baja = str(pedir_entero("Ingrese el DNI del cliente:"))
    temp = "temp.txt"
    cliente_a_borrar = False
    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = dividir_linea_clientes(linea)
            if datos:
                id, nombre, apellido, dni = datos
                if dni != dni_baja:
                    aux.write(linea)
                else:
                    cliente_a_borrar = True

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

    if cliente_a_borrar:
        try:
            os.remove(archivo)       # elimina el original
            os.rename(temp, archivo) # renombra el temporal
            print(f"El cliente con DNI N° {dni_baja} se ha eliminado correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  # eliminamos el temporal si no se usó
        print(f"No se encontró el cliente con DNI N° {dni_baja}.")

def modificar_cliente(archivo):
    dni_modificar = str(pedir_entero("Ingrese el DNI del cliente:"))
    temp = "temp.txt"
    cliente_a_modificar = False

    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = dividir_linea_clientes(linea)
            if datos:
                id, nombre, apellido, dni = datos
                if dni == dni_modificar:
                    cliente_a_modificar = True
                    print(f"Cliente encontrado: {nombre} - {apellido} - {dni}")
                    nuevo_nombre = input("Ingrese el nuevo nombre del cliente (ENTER para mantener): ")
                    if nuevo_nombre == "":
                        nuevo_nombre = nombre

                    nuevo_apellido = input("Ingrese el nuevo apellido del cliente (ENTER para mantener): ")
                    if nuevo_apellido == "":
                        nuevo_apellido = apellido
                    
                    nuevo_dni = pedir_entero("Ingrese el nuevo DNI del cliente (0 para mantener): ")
                    if nuevo_dni == 0:
                        nuevo_dni = dni

                    nueva_linea = f"{id};{nuevo_nombre};{nuevo_apellido};{nuevo_dni}\n"
                    aux.write(nueva_linea)
                    print(f"El cliente con el DNI N° {nuevo_dni} se ha modificado.")
                else:
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
            print("Error en el cierre del archivo:")

    if cliente_a_modificar:
        try:
            os.remove(archivo)
            os.rename(temp, archivo)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró el cliente con el DNI N° {dni_modificar}.")