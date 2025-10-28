import json, sys

ruta_habitaciones = "./informacion_almacenada/habitaciones.json"
ruta_habitaciones_baja = "./informacion_almacenada/habitaciones_baja.json"

def leerArchivoJson(ruta_archivo):
    if ruta_archivo == "h": ruta_archivo = ruta_habitaciones
    if ruta_archivo == "hb": ruta_archivo = ruta_habitaciones_baja

    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8", newline="\n")
        
        datos = {}
        try:
            datos = json.load(archivo)
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
            

        return datos
    except FileNotFoundError as e:
        print("No se encontro el archivo:", e)
      
    except Exception as e:
        print("Ocurrio un error con la lectura del archivo:", e)
        
def agregarHabitacion(nueva_habitacion, habitaciones, baja=False):
    ruta = ruta_habitaciones_baja if baja else ruta_habitaciones

    habitaciones.update(nueva_habitacion)
    sobreescribirJson(habitaciones, ruta, "Error al guardar la nueva habitacion")

def eliminarHabitacion(cod_habitacion, habitaciones, baja=False):
    ruta = ruta_habitaciones_baja if baja else ruta_habitaciones

    habitaciones.pop(cod_habitacion)
    sobreescribirJson(habitaciones, ruta, "Error al borrar la habitacion")

def actualizarHabitacion(hab_modificada, habitaciones):
    habitaciones.update(hab_modificada)
    sobreescribirJson(habitaciones, ruta_habitaciones, "Error al actualizar la habitacion")

def sobreescribirJson(diccionario, ruta, mensaje_error):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(diccionario, archivo, ensure_ascii=False, indent=4)
            archivo.write("\n")
        return True
    except Exception as e:
        print(f"\n{mensaje_error}:", e)
        return False

# def agregarUsuarioNuevo(usuario_nuevo, usuarios):
#     ultimo_id = list(usuarios.keys())[-1]
#     nuevo_id = generarNuevoId(ultimo_id)

#     usuario_empaquetado = {
#         nuevo_id: usuario_nuevo
#     }

#     # Almacena en memoria el nuevo usuario
#     usuarios.update(usuario_empaquetado)
    
#     # Almacena en el json el nuevo usuario
#     try:
#         with open(ruta_usuarios, "w", encoding="utf-8") as archivo: # Abre el archivo en append mode (Escribe al final del arhivo)
#             json.dump(usuarios, archivo, indent=4)
#             archivo.write("\n")
#         return True
#     except Exception as e:
#         print("\nError al guardar la nueva pregunta:", e)
#         return False
    
    
# def generarNuevoId(ultimo_id):
#     numero = int(ultimo_id.split("_")[1])
#     nuevo_id = f"usr_{numero + 1}"
#     return nuevo_id