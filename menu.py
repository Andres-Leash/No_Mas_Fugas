import funciones_principales
from validaciones import validar_opciones


def abrir_menu (egresos_familia, ingresos_familia):
    print('==Bienvenido al sistema de gestion de ingresos del hogar==')
    print('')
    
    sesion = True

    while sesion:
        print('Escoja una de las siguientes opciones [1-4]: \n')
        print('-'*30)
        print('1- Total ingresos')
        print('2- Total egresos')
        print('3- Saldo total')
        print('4- Promedio de egresos')
        print('5- Salir')
        print('-'*30)
        print('')
        opcion = input()
        print('')
        print('-'*30)

        match opcion:
            case '1':
                funciones_principales.total_ingresos(ingresos_familia)
            case '2':
                funciones_principales.total_egresos(egresos_familia)
            case '3':
                funciones_principales.saldo_total(ingresos_familia, egresos_familia)
            case '4':
                funciones_principales.promedio_egresos(egresos_familia)
            case '5':
                print ('Gracias por su preferencia')
            case _:
                validar_opciones(opcion)
            


      

