from mako.runtime import Context
import io

__author__ = 'arkadoel'

import os
import os.path
from mako.template import Template
import cherrypy


class webapp(object):

    @cherrypy.expose
    def index(self):
        return open('./index.html')

    @cherrypy.expose(alias="/accion")
    def accion(self, nombre="", password=""):
        print(nombre, password)
        cherrypy.session['mi_nombre'] = nombre

        template = Template(filename="./segundo.html")
        return template.render(nombre=nombre)


if __name__ == '__main__':
    w = webapp()


    conf = {
     '/': {
         'tools.sessions.on': True,
         'tools.staticdir.root': os.path.abspath(os.getcwd())
     },
     '/static': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': './public'
     }
}
    cherrypy.quickstart(w, '/', conf)

