import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):

        return """
            <html>
            <body>
                <h1>Hola</h1>
            </body>
            </html>
            """

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())