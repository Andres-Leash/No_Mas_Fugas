# Importación de módulo nativo de Python
import csv

# Se definen 2 funciones tanto para egresos como ingresos
def cargar_egresos_familia (ruta):
    # Se define un diccionario para todos los datos traidos desde el .csv
    egresos = {}

    try:
        # Con la funcion with open se abre el archivo y se cierra al terminar de ejecutar
        with open (ruta, "r", encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                ID = fila["id_egreso"]
                egresos[ID] = {
                    "integrante": fila['integrante_familiar'],
                    "tipo_egreso": fila['tipo_egreso'],
                    "fecha": fila['fecha'],
                    "monto": int(fila['monto'])          
                }
        return egresos
    except FileNotFoundError as e:
        print (f"El archivo {ruta} no existe:", e)
    
def cargar_ingresos_familia (ruta):
    # Se define un diccionario para todos los datos traidos desde el .csv
    ingresos = {}
    
    # Mediante try/except se verifica que el archivo existe o no
    # Se le da al usuario un mensaje en caso de error
    try:
        # Con la funcion with open se abre el archivo y se cierra al terminar de ejecutar
        with open (ruta, "r", encoding="UTF-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                ID = fila["id"]
                ingresos[ID] = {
                    "integrante": fila['integrante'],
                    "fecha": fila['fecha'],
                    "monto": int(fila['monto'])          
                }
        return ingresos
    except FileNotFoundError as e:
        print (f"El archivo {ruta} no existe:", e)