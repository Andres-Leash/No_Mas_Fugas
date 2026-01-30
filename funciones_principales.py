import validaciones
from datetime import datetime



def obtener_integrantes_y_meses(egresos_familia):
    #Se definieron variables para preguntas personalizadas al usuario
    integrantes = set() #variable se convertira a tupla despues
    rango_meses = set() #se mantendrá como conjunto
    for dato in egresos_familia.values(): #itera los valores del diccionario
        #añade a integrantes la itenracion de integrante
        integrantes.add(dato['integrante'])

        fecha = datetime.strptime(dato['fecha'], '%Y-%m-%d')
        meses = fecha.month
        rango_meses.add(meses)
    rango_meses = sorted(rango_meses) #Lo ordena alfabeticamente
    integrantes = tuple(sorted(integrantes)) #Lo ordena y transforma a tupla
    return integrantes, rango_meses

def obtener_integrantes_y_meses(ingresos_familia):
    #Se definieron variables para preguntas personalizadas al usuario
    integrantes = set() #variable se convertira a tupla despues
    rango_meses = set() #se mantendrá como conjunto
    for dato in ingresos_familia.values(): #itera los valores del diccionario
        integrantes.add(dato['integrante'])


        rango_meses.add(dato['fecha'])
    rango_meses = sorted(rango_meses) #Lo ordena alfabeticamente
    integrantes = tuple(sorted(integrantes)) #Lo ordena y transforma a tupla
    return integrantes, rango_meses

def total_ingresos (ingresos_familia):
    
    #Menu de opciones            
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
            #Se obtiene solo los integrantes de la funcion con indice 0
            integrantes = obtener_integrantes_y_meses(ingresos_familia)[0]
            print('Integrantes familiares disponibles: ')
            for i, integrante in enumerate(integrantes, start=1):
                print(f'{i}. {integrante}')
            print('')
            opcion = input ('Escoja el nombre del integrante: ')
            print('')
            print('-'*30)
            while True:  
                if opcion in integrantes:
                    total = 0
                    for dato in ingresos_familia.values():
                        if dato['integrante'] == opcion:
                            total += dato['monto']
                    print (f'El total de egresos de {opcion} fue de ${total}')
                    print ('-'*30)
                    break
                else:
                    print ("La opcion no esta dentro de la lista")
                    print ('Intente nuevamente')
                    print ('-'*30)
        case '2':
            Total = 0
            for dato in ingresos_familia.values():
                Total += dato['monto']
            print (f'El total de ingresos es de ${Total}')
            print ('-'*30)
        case '3':
            print ('Gracias por su preferencia')
        case _:
            validaciones.validar_opciones(opcion)