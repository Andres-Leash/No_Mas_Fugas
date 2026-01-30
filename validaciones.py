# Función para decirle al usuario qué fué lo que escribió mal en las opciones 

def validar_opciones (opcion):
    if opcion.isdecimal():
        print('Escogió un decimal, solo use números enteros dentro de las opciones indicadas')
    elif opcion.isalpha():
        print('Escogió una letra, solo use números enteros dentro de las opciones indicadas')
    else:
        print ('Escoja una opcion en el rango solicitado')