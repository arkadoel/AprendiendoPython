from acciones import Acciones
from Escrituras import EscribirExcel

from _datetime import datetime
__author__ = 'arkadoel'
__date__ = '2015-jun-16'


RUTA_EXCEL = '/media/DATOS/PROYECTOS/2015/excelGrande.xlsx'

def getHora():
    horas = datetime.now().hour
    minutos = datetime.now().minute
    segundos = datetime.now().second
    milisegundos = datetime.now().microsecond

    resultado = ''

    if horas <10:
        resultado += '0' + str(horas)
    else:
        resultado += str(horas)

    resultado += ':'

    if minutos <10:
        resultado += '0' + str(minutos)
    else:
        resultado += str(minutos)

    resultado += ':'
    if segundos <10:
        resultado += '0' + str(segundos)
    else:
        resultado += str(segundos)
        resultado += ':'

    if milisegundos <10:
        resultado += '0' + str(milisegundos)
    else:
        resultado += str(milisegundos)

    return resultado

def ver_menu():
    seguir = True

    while(seguir):
        print('Del siguiente menu, seleccione la opcion deseada:')
        print('\t1.- Intentar leer datos')
        print('\t2.- Importar datos a base de datos')
        print('\t3.- Mostrar datos de un dataframe')
        print('\t4.- Escribir un xlsx con pypandas')
        print('\r\n\t32.-Salir')

        opcion = input('\r\n\tOpcion: ')

        if opcion == '1':
            print("Inicio: " + getHora())
            Acciones(ruta = RUTA_EXCEL).intentar_leer_archivo()
            print("Fin: " + getHora())
        elif opcion == '2':
            print("Inicio: " + getHora())
            Acciones(ruta= RUTA_EXCEL).volcar_datos_a_db()
            print("Inicio: " + getHora())
        elif opcion == '3':
            Acciones(ruta = RUTA_EXCEL).prueba_recorrido_dataframe()
        elif opcion == '4':
            escribir = EscribirExcel(entrada=RUTA_EXCEL, salida="./salida.xlsx")
            escribir.crear_un_libro_pandas_Excel_Writer()
            escribir.crear_libro_xlwt()
            escribir.crear_libro_openpyxl()
            escribir.modificar_con_openpyxl()
        elif opcion == '32':
            seguir = False

if __name__ == '__main__':
    ver_menu()
