# Importación de módulos
from menu import abrir_menu
from control_CSV import cargar_ingresos_familia as ingreso
from control_CSV import cargar_egresos_familia as egreso


def main ():
    
    # Carga de archivos
    egresos_familia = egreso ("archivo_prueba/prueba_egresos.csv")
    ingresos_familia = ingreso ("archivo_prueba/prueba_ingresos.csv")
    #Se llama la función abrir_menú desde módulo menu
    abrir_menu (egresos_familia, ingresos_familia)
   
#El software se va a ejecutar solo si está en main    
if __name__ == "__main__":
    main()