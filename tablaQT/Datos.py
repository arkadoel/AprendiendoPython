""" Clases para generar datos
    que poner en la tabla

"""
class Persona:
    def __init__(self, nombre='', apellido='', edad=0):
        self.nombre = nombre
        self.apellidos = apellido
        self.edad = edad

class Modelo:

    def __init__(self):
        self.lista_personas = list()
        self.columnas = ['Nombre', 'Apellidos', 'Edad']

        peter = Persona(nombre='Peter', apellido='Chen', edad=20)
        george = Persona(nombre='George', apellido='Lucas', edad=50)

        self.lista_personas.append(peter)
        self.lista_personas.append(george)

