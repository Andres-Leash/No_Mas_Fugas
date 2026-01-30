# Importación de módulos
import funciones_principales
from validaciones import validar_opciones

# Apertura de menú
def abrir_menu (egresos_familia, ingresos_familia):
    print('==Bienvenido a No más Fugas==')
    print('')
    
    # Se establece variable sesión true para que cuando el menú
    # se cierre, sesión queda en False
    sesion = True

    while sesion:
        print('Escoja una de las siguientes opciones [1-4]: \n')
        print('1- Total ingresos')
        print('2- Total egresos')
        print('3- Saldo total')
        print('4- Salir')
        print('-'*30)
        opcion = input('Ingrese su opción: \n')
        print('-'*30)

        # Menu de opciones y llamada a las respectivas funciones de funciones_principales
        match opcion:
            case '1':
                funciones_principales.total_ingresos(ingresos_familia)
            case '2':
                funciones_principales.total_egresos(egresos_familia)
            case '3':
                funciones_principales.saldo_total(ingresos_familia, egresos_familia)
            case '4':
                print ('Gracias por su preferencia')
                sesion = False
            case _:
                validar_opciones(opcion) #Si la opcion no corresponde, va a llamar a esta función
            


      

