__author__ = 'Arkadoel'
import threading
import time

class ProcesoReloj:
    '''
    Clase que tiene como objetivo controlar la ejecucion de un reloj
    que compruebe cada cierto tiempo cuando ha de ejecutarse una accion
    '''

    def __init__(self):
        self.daemon = threading.Thread(target=self.proceso, name='DemonioReloj')
        self.daemon.setDaemon(True)

    def iniciar(self):
        self.daemon.start()

    def parar(self):
        self.daemon._stop()

    def proceso(self, alerta=None):
        '''
        metodo a poner en un nuevo hilo
        :return:
        '''
        print(threading.currentThread().getName())
        time.sleep(7)
        print('Proceso terminado')
