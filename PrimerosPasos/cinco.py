#2014-oct-24 mas pruebas con clases
#probando a programar con pyScripter

class coche:

    #constructor
    def __init__(self, nombre):
        '''
            definiendo una variable de la clase a
            partir de un parametro
        '''
        self.nombre = nombre

    #destructores como en C
    def __del__(self):
        nombreClase = self.__class__.__name__
        print ("clase ", nombreClase, " destruida")

class coche2:
    propiedad =0
    propi2='hola'

    def __init__(self):
        propi2='54'

    def setPropiedad(self, valor):
        coche2.propiedad = valor

    def getPropiedad(self):
        return str(coche2.propiedad)

def main():
    print('hola mundor')
    renault= coche("michoche")
    print( renault.nombre)
    renault.__del__()

    segundo = coche2()
    segundo.setPropiedad(543)
    print("Propiedad vale ",segundo.getPropiedad())


if __name__ == '__main__':
    main()

