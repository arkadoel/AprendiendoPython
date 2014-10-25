#-------------------------------------------------------------------------------
# Pruebas con errores, excepciones y otros
# Created:     24/10/2014
#-------------------------------------------------------------------------------
import sys

def main():
    a=32
    b=0

    #probando division por cero
    try:
        c = a/b
        print("division: ", str(c))
    except ZeroDivisionError:
        print("Error de division cero")
    except:
        print('Error detectado: ', sys.exc_info()[0])

    print ('segundo error')
    try:
        c = a/b
        print("division: ", str(c))
    except Exception as inst:
        print(type(inst))
        print(inst.args)


if __name__ == '__main__':
    main()
