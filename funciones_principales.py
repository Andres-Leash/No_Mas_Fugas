
# Importación de módulos de datatime y propios como validaciones

from datetime import datetime
import validaciones

# Se definen 2 funciones para separar datos a partir del diccionario y estandarizarlos
# Ambas funciones son uno para Egresos y el otro para Ingresos
# También se define una función para recursividad en totales de egresos e ingresos
# Finalmente se definen las funciones operacionales: ingresos, egresos y saldo


def obtener_variables_egresos(egresos_familia):
    # Se definieron variables para preguntas personalizadas al usuario
    integrantes = set()  # variable se convertira a tupla despues
    rango_meses = set()  # se mantendrá como conjunto
    tipo_egreso = set()  # se mantendrá como conjunto
    for dato in egresos_familia.values():  # itera los valores del diccionario
        # añade a integrantes la itenracion de integrante
        integrantes.add(dato["integrante"])

        # añade a rango meses la iteracion de fechas
        fecha = datetime.strptime(dato["fecha"], "%Y-%m-%d")
        meses = fecha.month
        rango_meses.add(meses)

        # añade a tipo egreso la iteracion correspondiente
        tipo_egreso.add(dato["tipo_egreso"])
    rango_meses = sorted(rango_meses)  # Lo ordena alfabeticamente
    integrantes = tuple(sorted(integrantes))  # Lo ordena y transforma a tupla
    tipo_egreso = sorted(tipo_egreso)  # Lo ordena alfabeticamente
    return integrantes, rango_meses, tipo_egreso


def obtener_variables_ingresos(ingresos_familia):
    # Se definieron variables para preguntas personalizadas al usuario
    integrantes = set()  # variable se convertira a tupla despues
    rango_meses = set()  # se mantendrá como conjunto
    for dato in ingresos_familia.values():  # itera los valores del diccionario
        integrantes.add(dato["integrante"])

        fecha = datetime.strptime(dato["fecha"], "%Y-%m-%d")
        meses = fecha.month
        rango_meses.add(meses)
    rango_meses = sorted(rango_meses)  # Lo ordena alfabeticamente
    integrantes = tuple(sorted(integrantes))  # Lo ordena y transforma a tupla
    return integrantes, rango_meses

def recursividad_ingresos_egresos(montos, indice=0):
    # Cuando el índice llege al mismo valor que monto, va a terminar la función recursiva
    if indice == len(montos):
        return 0
    else:
        # Va a regresar el monto del indice y va a sumar el siguiente valor
        return montos[indice]['monto'] + recursividad_ingresos_egresos(montos, indice + 1)
    

def total_ingresos(ingresos_familia):

    # Menu de opciones
    print("Escoja una de las siguientes opciones [1-3]: \n")
    print("1- Ingresos por integrante")
    print("2- Ingresos totales")
    print("3- Salir")
    print("-" * 30)
    opcion = input('Ingrese su opción: \n')
    print("-" * 30)

    match opcion:
        case "1":
            # Se obtiene solo los integrantes de la funcion con indice 0
            integrantes = obtener_variables_ingresos(ingresos_familia)[0]

            while True:
                print("Integrantes familiares disponibles: ")
                # itera en toda la lista de integrantes familiares
                for integrante in integrantes:
                    print(f"- {integrante}")
                opcion = input("Escoja el nombre del integrante o 'salir' para volver al menu: ")
                print("-" * 30)
                if opcion in integrantes:
                    # Se ejecuta solo si lo escrito por el usuario
                    # esta dentro de la lista de integrantes
                    total = 0
                    for dato in ingresos_familia.values(): #Itera sobre la lista
                        if dato["integrante"] == opcion:
                            total += dato["monto"]
                    print(f"El total de ingresos de {opcion} fue de ${total}")
                    print("-" * 30)
                    break
                elif opcion == "salir":
                    break
                else:
                    print("La opcion no esta dentro de la lista")
                    print("Intente nuevamente")
                    print("-" * 30)
        case "2":
            # Se calcula el total de ingresos familiares del csv con la función recursiva
            ingresos = list(ingresos_familia.values())
            total = recursividad_ingresos_egresos(ingresos)
            
            print(f"El total de ingresos fue de ${total}")
            print("-" * 30)
        case "3":
            print("Saliendo de la funcion")
        case _:
            # Esto es en caso de que escriba algo que no corresponda
            validaciones.validar_opciones(opcion)


def total_egresos(egresos_familia):

    # Menu de opciones
    print("Escoja una de las siguientes opciones [1-3]: \n")
    print("1- Egresos por tipo de egreso")
    print("2- Egresos totales")
    print("3- Salir")
    print("-" * 30)
    opcion = input('Ingrese su opción: \n')
    print("-" * 30)

    match opcion:
        case "1":
            # Se obtiene solo los integrantes de la funcion con indice 0
            tipo_egreso = obtener_variables_egresos(egresos_familia)[2]

            
            while True:
                # Se obtiene el listado de tipo de egresos disponibles
                print("Tipo de egresos disponibles: ")
                for tipo in tipo_egreso:
                    print(f"- {tipo}")
                opcion = input("Escoja el tipo de egreso o 'salir' para volver al menu: ")
                print("-" * 30)
                # Se usa un condicional si la opcion está dentro de la lista de tipo de egreso
                if opcion in tipo_egreso:
                    total = 0
                    for dato in egresos_familia.values():
                        if dato["tipo_egreso"] == opcion:
                            total += dato["monto"]
                    print(f"El total de egresos de {opcion} fue de ${total}")
                    print("-" * 30)
                    break
                elif opcion == "salir":
                    break
                else:
                    print("La opcion no esta dentro de la lista")
                    print("Intente nuevamente")
                    print("-" * 30)
        case "2":
            # Se calcula el total de egresos familiares del csv con la función recursiva
            egresos = list(egresos_familia.values())
            total = recursividad_ingresos_egresos(egresos)

            print(f"El total de egresos fue de ${total}")
            print("-" * 30)
        case "3":
            print("Saliendo de la funcion")
        case _:
            validaciones.validar_opciones(opcion)


def saldo_total(ingresos_familia, egresos_familia):
    # Menu de opciones
    print("Escoja una de las siguientes opciones [1-3]: \n")
    print("1- Saldo por mes")
    print("2- Saldo total")
    print("3- Salir")
    print("-" * 30)
    opcion = input('Ingrese su opción: \n')
    print("-" * 30)

    match opcion:
        case "1":
            # Se obtiene un set de meses tanto del diccionario egresos como de ingresos
            meses_egresos = obtener_variables_egresos(egresos_familia)[1]
            meses_ingresos = obtener_variables_ingresos(ingresos_familia)[1]
            # Se combinan ambos sets, para que solo queden los que están en común
            meses_comunes = set(meses_egresos) & set(meses_ingresos)
            # Se realiza un listado de los meses del año para reemplazarlo por los valores numerales
            meses_anio = {
                1: "Enero",
                2: "Febrero",
                3: "Marzo",
                4: "Abril",
                5: "Mayo",
                6: "Junio",
                7: "Julio",
                8: "Agosto",
                9: "Septiembre",
                10: "Octubre",
                11: "Noviembre",
                12: "Diciembre",
            }
            # Finalmente se hace el diccionar clave, valor, donde valor es el mes en palabras
            meses_disponibles = {
                mes: meses_anio[mes] for mes in meses_anio if mes in meses_comunes
            }

            # Ahora entra a la funcion operacional de saldo por meses
            while True:
                # Se obtiene el listado de meses disponibles para el usuario
                print("Meses para consultar:")
                for mes, nombre in meses_disponibles.items():
                    print(f"{mes}. {nombre}")
                # Se le pregunta al usuario el mes a consultar
                opcion = input("Escoja el mes (numero) o salir para volver al menu:").strip().lower()
                print("-" * 30)
                # Si es 'salir', va a regresar al menú principal
                if opcion == 'salir':
                    print("Saliendo de saldos")
                    print("-" * 30)
                    break
                # Se realiza condicional para verificar que el input es entero
                elif opcion.isdigit():
                    # Se transforma a formato entero
                    opcion = int(opcion)
                    # Se verifica que la opción está dentro de la lista de meses              
                    if opcion in meses_disponibles:
                        total_ingresos = 0
                        total_egresos = 0
                        for dato in ingresos_familia.values():
                            # Cuando se iteran en las fechas, hay que transformarlo primero en el formato
                            # fecha para realizar la comparación
                            fecha = datetime.strptime(dato["fecha"], "%Y-%m-%d")
                            # Aquí se compara para realizar la suma
                            if fecha.month == int(opcion):
                                total_ingresos += dato["monto"]
                        for dato2 in egresos_familia.values():
                            fecha2 = datetime.strptime(dato2["fecha"], "%Y-%m-%d")
                            if fecha2.month == int(opcion):
                                total_egresos += dato2["monto"]
                        saldo_mes = total_ingresos - total_egresos # Suma saldo total
                        print(f'El total de saldo en el mes de {meses_disponibles[int(opcion)]} fue de ${saldo_mes}')
                        print('-'*30)
                        break
                    else: # En el caso de que sea entero, pero no está en la lista
                        print("La opcion no esta dentro de la lista")
                        print("Intente nuevamente")
                        print("-" * 30)
                else:
                    print ('Ingrese una opción válida, intente nuevamente')
                    print("-" * 30)
                  

        case "2":
            # Operación para obtener saldo entre ingresos y egresos
            egresos = 0
            ingresos = 0
            for dato in egresos_familia.values():
                egresos += dato["monto"]
            for dato2 in ingresos_familia.values():
                ingresos += dato2["monto"]
            saldo_total = ingresos - egresos
            print(f"El saldo total fue de ${saldo_total}")
            print("-" * 30)
        case "3":
            print("Gracias por su preferencia")
        case _:
            validaciones.validar_opciones(opcion)

