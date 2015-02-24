__author__ = 'Arkadoel'
import threading
import time
from Constantes import const
import sys, os, subprocess
from datos.TablaAlerta import tbAlertas

try:
    import winsound
except:
    print('Sistema no windows, no se encuentra la libreria winSound')


class MirarHora(threading.Thread):

    ESPERA = 10     #segundos de espera entre iteracciones
    PASADAS = 1     #recarga el listado de tareas cada X pasadas de reloj

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
        self.alertaActual = None
        return

    def run(self):
        print('Argumentos pasados al demonio: ', self.kwargs)
        seguir = True
        #obtener lista de tareas para hoy
        self.listaTareas = self.kwargs
        i=0

        while seguir:
            if i>self.PASADAS:
                self.listaTareas = tbAlertas().listarHorasAlertasHoy()
                self.alertaActual = None


            horaActual = const.getHora()

            for key, value in self.listaTareas.items():
                if horaActual == value[0]:
                    print('toca sonar', value[0])
                    if self.alertaActual is not None:
                        if self.alertaActual != key:
                            #la alerta no ha sido notificada, la hacemos sonar
                            self.hacerProcesos(hora=value[0], texto=value[1], comando=value[2])
                        else:
                            print('La alerta ya fue notificada, no sonara')
                    else:
                        self.hacerProcesos(hora=value[0], texto=value[1], comando=value[2])
                        self.alertaActual = key
                else:
                    print('.', end=' ')

            #hereda el error de no limpiar el buffer del lenguaje C --> LOL
            sys.stdout.flush()

            time.sleep(self.ESPERA)

            i +=1
        #finWhile

        print('Finalizado el daemon reloj')


    def hacerProcesos(self, hora=None, texto=None, comando=None):
        '''
        Lanza los eventos que haya que hacer en ese momento
        :return:
        '''

        const.SYSTRAY.showMessage(hora, texto)

        if comando is not None:
            strEjecuta = comando
            print(strEjecuta)
            subprocess.call(strEjecuta, shell=True)

        #repetimos tres veces el sonido
        for i in range(0, 3):

            if os.name == 'nt':
                #windows
                winsound.PlaySound(const.SONIDO, winsound.SND_FILENAME)
            elif os.name== 'posix':
                #linux
                comando = 'aplay ' + const.SONIDO
                os.system(comando)



