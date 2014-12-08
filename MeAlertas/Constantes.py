__author__ = 'Arkadoel'
from _datetime import  datetime

class const:
    __APP_VERSION__ = '0.0.1'
    __DB_PATH__ = "./mealertas.db"


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

    