#!/usr/bin/env python3
import sys

if sys.version.__contains__('2.'):
    print('Python 2.x, no se puede ejecutar, se necesita python3')
elif sys.version.__contains__('3.'):
    print('Python 3.x, correcto')
    from PyQt4 import QtGui
    from Constantes import const
    from datos.TablaAlerta import tbAlertas
    #from Ventana1 import vPrincipal

    import Reloj2
    import IconoSistema

__author__ = 'Arkadoel'
__date__ = '6 dic 2014'
__license__ = 'GPLv2'

'''
Aplicacion que permite poner recordatorios semanales a ciertas alertas
en determinados dias de la semana. Mas o menos.

Que es lo que se quiere aprender con este desarrollo:
    - Threads in python
    - Investigar si es necesario hacer un DirectORM para python.
    - Mas controles QT
'''

@staticmethod
def Salir():
    sys.exit(0)

if __name__ == '__main__':
    if sys.version.__contains__('3.'):

        app = QtGui.QApplication(sys.argv)
        print('Iniciado ' + const.getHora())
        tabla = tbAlertas()
        tareas = tabla.listarHorasAlertasHoy()

        IconoSistema.IconoSistema(app)
        hilo = Reloj2.MirarHora(kwargs=tareas, args='0', daemon=True)

        hilo.start()

        app.exec_()


    '''
    tabla = tbAlertas()
    alerta = Alerta()
    alerta.iniciar(const.getHora(), 'Prue')

    tabla.agregar(alerta)

    tareas = tabla.listarHorasAlertas()

    salida =tabla.getAlertaById(112)
    if salida is not None:
        print(salida.hora)
    else:
        print('salida none')

    l = const.diaSemana()
    print('ii' + l)


    for key, value in tareas.items():
        tabla.eliminar(key)

    '''