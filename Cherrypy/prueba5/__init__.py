

__author__ = 'arkadoel'

import cherrypy
import os, os.path
import string


class webapp(object):

    @cherrypy.expose
    def index(self):
        return  file('./index.html')

if __name__ == '__main__':
    w = webapp()
    cherrypy.quickstart(w)
