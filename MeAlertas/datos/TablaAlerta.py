__author__ = 'Arkadoel'
import sqlite3
import sys
from Constantes import const
import datos

class Alerta:
    '''
    Clase objeto correspondiente a una alerta de la DB
    '''
    def __init__(self):
        self.id = -1
        self.hora= ''
        self.mensaje= ''
        self.estaNotificada = False
        self.iniciarDiasSemana()
        self.script = ''

    def iniciar(self, _hora, _mensaje):
        self.estaNotificada = False
        self.hora = _hora
        self.mensaje = _mensaje
        self.iniciarDiasSemana()

    def iniciarDiasSemana(self):
        self.lunes = False
        self.martes = False
        self.miercoles = False
        self.jueves = False
        self.viernes = False
        self.sabado = False
        self.domingo = False

class tbAlertas:
    '''
    Clase encargada de las operaciones sobre la tabla
    Alertas de la base de datos
    '''

    __INSERT__ = '''
                insert into Alertas
                (hora, mensaje, notificada, lunes, martes, miercoles, jueves, viernes, sabado, domingo, script)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                '''
    __DELETE__ = 'delete from Alertas where id = ?;'
    __UPDATE__ = '''
                update Alertas set
                hora = ?, mensaje=?, notificada=?,
                lunes=?, martes=?, miercoles=?,
                jueves=?,
                viernes=?,
                sabado=?,
                domingo=?,
                script=?
                where id = ?;
                '''
    __SELECT__ = 'select * from Alertas'

    def __init__(self):
        self.gestorDB = datos.db()

    def agregar(self, alerta):

        existe = self.getAlertaById(alerta.id)

        if existe is None:
            sql = self.__INSERT__
            self.gestorDB.ejecutarSQL(sql, (
                alerta.hora,
                alerta.mensaje,
                alerta.estaNotificada,
                alerta.lunes,
                alerta.martes,
                alerta.miercoles,
                alerta.jueves,
                alerta.viernes,
                alerta.sabado,
                alerta.domingo,
                alerta.script
            ))
        else:
            sql = self.__UPDATE__
            self.gestorDB.ejecutarSQL(sql, (
                alerta.hora,
                alerta.mensaje,
                alerta.estaNotificada,
                alerta.lunes,
                alerta.martes,
                alerta.miercoles,
                alerta.jueves,
                alerta.viernes,
                alerta.sabado,
                alerta.domingo,
                alerta.script,
                alerta.id
            ))

    def eliminar(self, id):
        sql = self.__DELETE__.replace('?', str(id))
        self.gestorDB.ejecutarSQL(sql, ())

    def getAlertaById(self, id):
        alerta = Alerta()
        sql = self.__SELECT__ + " where id = " + str(id) + ";"
        fila = self.gestorDB.consultaUnicaSQL(sql)

        if fila is None:
            return None
        else:
            alerta.id = fila['id']
            alerta.hora = fila['hora']
            alerta.mensaje = fila['mensaje']
            alerta.estaNotificada = fila['notificada']
            alerta.lunes = fila['lunes']
            alerta.martes = fila['martes']
            alerta.miercoles = fila['miercoles']
            alerta.jueves = fila['jueves']
            alerta.viernes = fila['viernes']
            alerta.sabado = fila['sabado']
            alerta.domingo = fila['domingo']
            alerta.script = fila['script']
            return alerta

    def listarHorasAlertas(self):
        sql = self.__SELECT__
        filas = self.gestorDB.consultaSQL(sql)

        resultado = {0:("","")}
        resultado.clear()

        for fila in filas:
            resultado.update({int(fila['id']):(fila['hora'], fila['mensaje'], fila['script'])})

        return resultado

    def listarHorasAlertasHoy(self):
        diaSemana = const.diaSemana()
        sql = self.__SELECT__+ " where " + diaSemana + "= 1;"
        filas = self.gestorDB.consultaSQL(sql)

        resultado = {0:("","")}
        resultado.clear()

        for fila in filas:
            resultado.update({int(fila['id']):(fila['hora'], fila['mensaje'], fila['script'])})

        return resultado

