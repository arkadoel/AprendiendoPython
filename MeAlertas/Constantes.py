__author__ = 'Arkadoel'
from _datetime import  datetime
import threading

class const:
    APP_VERSION = '0.1.0'
    DB_PATH = "./mealertas.db"
    SONIDO = './media/Alarm02.wav'
    ICONO = './media/LOGO.png'
    ICONO_NUEVO = './media/new.png'
    ICONO_GUARDAR = './media/save.png'
    ICONO_ELIMINAR = './media/delete.png'
    ICONO_LISTA = './media/bullets-black.png'
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

    