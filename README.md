# progra1-hotel

## 14. Sistema de gestión hotelera

Este sistema permite administrar eficientemente un hotel, fa-
cilitando el control de habitaciones, la gestión de clientes y la 
organización de reservas. Está orientado a establecimientos de 
alojamiento  que  desean  automatizar  el  proceso  de  registro, 
asignación y seguimiento de estadías. Las entidades sugeridas 
son: Clientes, que contienen los datos personales de los hués-
pedes; Habitaciones, que representan cada unidad disponible 
en  el  hotel  con  sus  características  (número,  tipo,  capacidad, 
estado); y Reservas, que vinculan a un cliente con una habita-
ción  en  un  período  determinado. La  entidad  de  unión  es  Re-
servas, ya que relaciona habitación, cliente y fechas de ingreso y egreso. 
El sistema debe implementar operaciones CRUD sobre todas las entidades, permitiendo re-
gistrar nuevos clientes, gestionar habitaciones (crear, modificar estado, dar de baja) y admi-
nistrar reservas (asignar, modificar, cancelar). Las búsquedas deben permitir, por ejemplo, 
consultar todas las reservas realizadas por un cliente específico, o verificar la disponibilidad 
de una habitación en una fecha dada, utilizando recursividad para explorar la grilla de ocu-
pación.  Se  utilizarán  matrices  para  representar  la  ocupación  diaria  de  habitaciones  (por 
ejemplo, una matriz con habitaciones en filas y fechas en columnas), y listas y diccionarios 
para organizar la información general. Las estadísticas básicas incluirán: porcentaje de ocu-
pación por habitación, promedio de duración de reservas, y cantidad total de reservas rea-
lizadas en un período. El sistema deberá validar correctamente los datos ingresados (como 
solapamiento  de  fechas  o  habitaciones  ya  ocupadas),  guardar  y  recuperar  información mediante archivos, utilizar Git para el control de versiones y contener pruebas unitarias que 
aseguren la integridad de su funcionamiento.

# Observaciones
* Expresiones regulares: utilizar 2 mas
* Funciones Lambda: emplear uso de map
* Conjuntos: emplear uso

## Recursividad
* minimo 3 usos de recursividad
* recorrer una matriz y mostrarla
* Recursion en estadistica, armar algo nuevo
* Ejemplo 12, devolver valor total de todas las reservas

Archivo temp para modificar reservas
