__author__ = 'Arkadoel'
__date__ = '6 dic 2014'
'''
Aplicacion que permite poner recordatorios semanales a ciertas alertas
en determinados dias de la semana. Mas o menos.

Que es lo que se quiere aprender con este desarrollo:
    - Threads in python
    - Investigar si es necesario hacer un DirectORM para python.
    - Mas controles QT
'''

from PyQt4 import QtGui
from Ventana1 import vPrincipal
from Constantes import const
import sys
from datos.TablaAlerta import tbAlertas, Alerta
import datetime
import Reloj2
import IconoSistema

if __name__ == '__main__':
    '''
    app = QtGui.QApplication(sys.argv)
    v = vPrincipal()
    v.show()

    sys.exit(app.exec_())
    '''


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

    IconoSistema.iconoSistema()

    print('Iniciado')
    tabla = tbAlertas()
    tareas = tabla.listarHorasAlertasHoy()
    hilo = Reloj2.MirarHora(kwargs=tareas,args='0', daemon=False)

    hilo.start()
    hilo.join()









