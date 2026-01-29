from menu import abrir_menu
from control_CSV import cargar_ingresos_familia as ingreso
from control_CSV import cargar_egresos_familia as egreso

print("__name__ =", __name__)
print ('cargo main')
def main ():
    print ('cargo main')
    egresos_familia = egreso ("archivo_prueba/prueba_egresos.csv")
    print ('cargo egresos familia')
    ingresos_familia = ingreso ("archivo_prueba/prueba_ingresos.csv")
    print ('cargo ingresos familia')
    
    print ('abriendo menu')
    abrir_menu (egresos_familia, ingresos_familia)
    print ('menu cerrado')
    
if __name__ == "__main__":
    main()
