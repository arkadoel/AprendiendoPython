'''
Created on 20/10/2014

@author: fer
'''

if __name__ == '__main__':
    print('hola')
    
    x=32 #entero
    print x
    
    # variable mensaje
    mensaje = "hola mundo"
    print mensaje

    #booleano
    my_bool=True
    print my_bool

    #exponentes
    calculo = 10**2
    print calculo

    print ("La variable calculo es de tipo: %s" % type(calculo))
    print ("Clase %s" % type(calculo).__name__)

    ''' Conversion de tipos '''
    entero = int(3.999)
    print entero

    real = float(3)
    print real

    cadena = str(32)
    print type(cadena)
    pass