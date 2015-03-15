'''
Lo importante para esta prueba es aprender a:
    -generar
    -Leer
    -Modificar
Archivos CSV
'''

import pandas as pd
import os

ARCHIVO = 'salida.csv'

def generar(path=None):
    '''
    Genera un archivo CSV con las columnas y los datos
    puestos anteriormente
    :param path:
    :return:
    '''
    columnas = ('Nombre', 'Apellidos', 'Edad', 'Sexo', 'Casado')
    datos =[
        ('Fer', 'Minguela', 29, 'hombre', False),
        ('Paco', 'Cifuentes', 32, 'hombre', True),
        ('Ana', 'Katerina', 34, 'mujer', False)
    ]

    df = pd.DataFrame(data=datos, columns=columnas)


    '''
    Para ver lo que contiene print(df)
    para ver los tipos de datos ... df.dtypes
    '''
    df.to_csv(path, index=False)
    print('Archivo generado')

def leer_archivo(archivo=None):
    '''
    Vamos a leer el archivo levemente
    :param archivo:
    :return:
    '''
    if os.path.isfile(archivo):
        datos = pd.read_csv(archivo)

        print(datos)
    else:
        print('Genere el archivo primero')

def modificar(archivo=None):
    '''
    Modificamos distintos aspectos del archivo
    :param archivo:
    :return:
    '''
    if os.path.isfile(archivo):
        datos = pd.read_csv(archivo)

        #nueva columna
        datos['columna'] = 32.3

        #intentar agregar una linea
        fila = ('Pedro', 'Martinez', 21, 'hombre', False, 2)
        datos.loc[len(datos)] = fila
        print(datos)

        print('\r\nAhora eliminamos el segundo elemento')
        datos = datos[datos.index != 2]
        #datos = datos.reset_index()
        print(datos)

        columnas = ['Nombre', 'Apellidos', 'Edad', 'Sexo', 'Casado']
        datos.to_csv(archivo, index=False, header=columnas)
    else:
        print('Genere el archivo primero')

if __name__ == '__main__':
    salir = False

    while salir == False:
        print('''
        Elija una de las siguientes opciones:
            1.- Generar
            2.- Leer archivo
            3.- Modificarlo

            9.- Salir
        ''')
        opcion = input('Opcion: ')

        if opcion == '1':
            generar(ARCHIVO)
        elif opcion == '2':
            leer_archivo(ARCHIVO)
        elif opcion == '3':
            modificar(ARCHIVO)
        elif opcion == '9':
            salir = True
        else:
            print('Escoja una opcion correcta')