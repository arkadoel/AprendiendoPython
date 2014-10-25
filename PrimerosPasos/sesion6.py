#-------------------------------------------------------------------------------
# Probemos con la herencia a ver que tal
# Created:     24/10/2014

#-------------------------------------------------------------------------------

class rueda:
    color=""
    diametro=""

    def __init__(self):
        rueda.color="rojo"
        rueda.diametro="17 pulgadas"

class carroceria:
    composicion = ""
    colorCarroceria=""

    def __init__(self):
        carroceria.colorCarroceria="verde"
        carroceria.composicion="Aluminio"

class coche(rueda, carroceria):
    def __init__(self):
        self.nombre ="Renault megane"
        rueda.__init__(self)
        carroceria.__init__(self)

    def setColor(self,valor):
        rueda.color = valor

    '''
        NO PERMITIDA
        def setColor(self, valor, tipo):
        rueda.color = valor + tipo
    '''

def main():

    miCoche = coche()
    print("Datos de mi coche ")
    print("\tColor: ", miCoche.color)
    print("\tComposicion carroceria: ", miCoche.composicion)
    print("\tDiametro de las ruedas: ", miCoche.diametro)

    miCoche.setColor("ambar")
    print("color: ", miCoche.color)

    '''Como las variables son dinamicas el tipo puede variar
    de cadena a entero en el mismo metodo, por tanto no es posible
    tener varios metodos con el mismo nombre, aunque cambie el
    numero de argumentos
    '''
    miCoche.setColor(329)
    print("color: ", type(miCoche.color))

    miCoche.setColor("h","52")
    print("color: ", type(miCoche.color))

if __name__ == '__main__':
    main()
