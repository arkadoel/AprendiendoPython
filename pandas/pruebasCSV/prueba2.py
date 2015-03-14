'''
Lo importante para esta prueba es aprender a:
    -generar
    -Leer
    -Modificar
Archivos CSV
'''

import pandas

def generar(path=None):
    pass

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
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '9':
            salir = True
        else:
            print('Escoja una opcion correcta')