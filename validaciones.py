# Función para decirle al usuario qué fué lo que escribió mal en las opciones 

def validar_opciones (opcion):
    if opcion.isalpha():
        print('Escogió una letra, solo use números enteros dentro de las opciones indicadas')
        print('-'*30)
    elif not opcion.isdigit():
        print('Escogió un decimal, solo use números enteros dentro de las opciones indicadas')
        print('-'*30)
    else:
        print ('Escoja una opcion en el rango solicitado')
        print('-'*30)