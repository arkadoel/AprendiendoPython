import cherrypy
'''
Agregamos la posibilidad de ejecutar una accion,
como si de struts se tratase

http://...../accion?nombre=Fer
'''

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hola mundo"

    @cherrypy.expose
    def accion(self, nombre=''):
        '''
        Como ponemos un parametro, podremos pasar parametros
        desde la url
        '''
        return 'Hola ' + nombre

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld()) 