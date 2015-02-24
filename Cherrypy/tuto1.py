import cherrypy
'''
Para arrancar el servidor simplemente ejecutar
python3 ./tuto1.py
'''

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hola mundo"

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld()) 
