__author__ = 'Arkadoel'
from _datetime import  datetime
import threading

class const:
    APP_VERSION = '0.0.1'
    DB_PATH = "./mealertas.db"
    SONIDO = './media/Alarm02.wav'
    ICONO = './media/LOGO.png'
    SYSTRAY = None
    v_PRINCIPAL=None


    @staticmethod
    def getHora():
        horas = datetime.now().hour
        minutos = datetime.now().minute
        #segundos = datetime.now().second
        resultado = ''

        if horas <10:
            resultado += '0' + str(horas)
        else:
            resultado += str(horas)

        resultado += ':'

        if minutos <10:
            resultado += '0' + str(minutos)
        else:
            resultado += str(minutos)

        '''
        resultado += ':'

        if segundos <10:
            resultado += '0' + str(segundos)
        else:
            resultado += str(segundos)
        '''
        return resultado

    def diaSemana() -> str:
        '''
            Devuelve el dia de la semana en el que estamos
            :rtype : basestring
            :return: String
            '''
        dias = ['Lunes',
                'Martes',
                'Miercoles',
                'Jueves',
                'Viernes',
                'Sabado',
                'Domingo']
        return dias[datetime.today().weekday()]

    