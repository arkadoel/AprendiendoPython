import cherrypy
'''
Probaremos a enviar un dato, cogerlo y guardarlo en sesion
'''
class StringGenerator:

    @cherrypy.expose
    def index(self):
        return """
                <html>
                <body>

                    <form method="get" action="procesar">
                          <input type="text" value="8" name="nombre" />
                              <button type="submit">Enviar</button>
                    </form>

                </body>
                </html>
                """

    @cherrypy.expose
    def procesar(self, nombre=''):
        #guardamos el nombre en sesion
        cherrypy.session['myNombre'] = nombre

        return 'Hola ' + nombre

    @cherrypy.expose
    def verSesion(self):
        '''
        Mostramos el contenido de lo guardado en sesion
        :return:
        '''
        return 'El contenido de la sesion es: ' + cherrypy.session['myNombre']

if __name__ == '__main__':
    #habilitar las variables de sesion
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }

    cherrypy.quickstart(StringGenerator(), '/', conf)