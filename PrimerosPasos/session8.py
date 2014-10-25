#-------------------------------------------------------------------------------
# Probemos ahora con los ficheros
# Created:     24/10/2014
#-------------------------------------------------------------------------------
import os

def EscribirFichero(ruta, texto):
    #abrir fichero modo simple para escribirlo
    f =open(ruta, 'w')
    f.write(texto)
    f.close()

def LeerFichero(ruta):
    f = open(ruta, 'r')
    textoEntero = f.read()
    f.close()
    return textoEntero

def LeerFicheroWith(ruta):
    with open(ruta,'r') as f:
        texto = f.read()
        f.close()
    return texto

def EliminarSiExiste(ruta):
    if os.path.isfile(ruta):
        os.remove(ruta)
        return True
    else:
        return False

def main():

    seguir = True

    while seguir:
        os.system('clear')
        print('Elija lo que quiere hacer:')
        print('\t1.- Escribir fichero')
        print('\t2.- Leer fichero')
        print('\t3.- Leer con with')
        print('\t4.- Eliminar un fichero')
        print('')
        print('\t9.- Salir')
        opcion = int(input('Opcion>'))

        if type(opcion).__name__ == 'int':
            if opcion == 1:
                EscribirFichero("fichero.txt","hola")
            if opcion == 2:
                print(LeerFichero('fichero.txt'))
            if opcion == 3:
                print(LeerFicheroWith('fichero.txt'))
            if opcion == 4:
                eliminado = EliminarSiExiste( input('ruta del fichero a eliminar: '))
                if eliminado == True:
                    print('Hecho')
                else:
                    print('Fallo al eliminar')
            if opcion == 9:
                seguir = False

if __name__ == '__main__':
    main()
