import validaciones
import math

def total_ingresos (egresos_familia):
    print ('Escoja una de las siguientes opciones [1-3]: \n')
    print('-'*30)
    print('1- Ingresos por integrante')
    print('2- Ingresos totales')
    print('3- Salir')
    print('-'*30)
    print('')
    opcion = input()
    print('')
    print('-'*30)

    match opcion:
        case '1':
            integrantes = set()
            for dato in egresos_familia.values():
                integrantes.add(dato['integrante'])
            
        case '2':
            continue
        case '3':
            print ('Gracias por su preferencia')
        case _:
            validaciones.validar_opciones(opcion)