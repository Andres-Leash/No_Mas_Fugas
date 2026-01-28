from menu import abrir_menu
from control_CSV import cargar_ingresos_familia as ingreso
from control_CSV import cargar_egresos_familia as egreso



def main ():
    egresos_familia = egreso ("archivo_prueba/prueba_egresos.csv")
    ingresos_familia = ingreso ("archivo_prueba/prueba_ingresos.csv")

    abrir_menu(egresos_familia, ingresos_familia)
    
if __name__ == "__main__":
    main
