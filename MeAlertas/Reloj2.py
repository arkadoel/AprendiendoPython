__author__ = 'Arkadoel'
import threading
import time
from Constantes import const
import sys, os

try:
    import winsound
except:
    print('Sistema no windows, no se encuentra la libreria winSound')


class MirarHora(threading.Thread):

    __ESPERA__ = 5 # segundos de espera entre iteracciones

    def __init__(self, target=None, group=None, name=None, verbose=None, args=None, kwargs=None, daemon=None):
        '''
        Inicializacion del hilo, por si queremos pasarle datos
        :param target:
        :param group:
        :param name:
        :param verbose:
        :param args:
        :param kwargs:
        :return:
        '''
        threading.Thread.__init__(self, group=group, target=target,name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        print('Argumentos pasados al demonio: ', self.kwargs)
        seguir = True
        #obtener lista de tareas para hoy
        self.listaTareas = self.kwargs


        while seguir:
            if self.listaTareas.__len__() == 0:
                seguir = False
            else:
                horaActual = const.getHora()

                for key, value in self.listaTareas.items():
                    if horaActual == value[0]:
                        print('toca sonar', value[0])
                        self.hacerProcesos(value[1])
                    else:
                        print('.', end=' ')

                #hereda el error de no limpiar el buffer del lenguaje C --> LOL
                sys.stdout.flush()

                time.sleep(self.__ESPERA__)

        print('Finalizado el daemon reloj')


    def hacerProcesos(self, texto=None):
        '''
        Lanza los eventos que haya que hacer en ese momento
        :return:
        '''

        const.SYSTRAY.showMessage(texto)

        if os.name == 'nt': #windows
            winsound.PlaySound(const.SONIDO, winsound.SND_FILENAME)
        elif os.name== 'posix': #linux
            comando = 'aplay ' + const.SONIDO
            os.system(comando)




