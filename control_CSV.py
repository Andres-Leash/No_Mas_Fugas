import csv


def cargar_egresos_familia (ruta):
    egresos = {}

    try:
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
    ingresos = {}

    try:
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