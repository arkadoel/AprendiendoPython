from mako.runtime import Context
import io

__author__ = 'arkadoel'

import os
import os.path
from mako.template import Template
from mako.lookup import TemplateLookup
import cherrypy

PATH = os.path.abspath(os.getcwd())

class webapp(object):

    @cherrypy.expose
    def index(self):
        direccion = PATH + "/index.html"
        return Template(filename=direccion).render()

    @cherrypy.expose(alias='/login')
    def login(self, nombre, password):
        if nombre == 'fer' and password == 'dos':
            return Template(filename=PATH + '/static/principal.html').render()
        else:
            return Template(filename=PATH + '/static/Error.html').render()


if __name__ == '__main__':
    w = webapp()
    conf = {
         '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './static'
         }
    }
    cherrypy.quickstart(w, '/', conf)
