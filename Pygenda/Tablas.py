"""
    Gestion de las tablas
"""
import sys
import sqlite3
from constantes import const

class tbpersona:
    conexion = None

    def __init__(self):
        try:

            self.conexion = sqlite3.connect(const.DB_PATH)

            #para evitar errores TypeError: tuple indices must be integers, not str
            self.conexion.row_factory = sqlite3.Row # its key
        except sqlite3.Error as e:

            print("Error %s:" % e.args[0])
            sys.exit(1)

    def nombresPersonas(self):
        """
        Listar los nombres completos de las personas
        :return: tupla de string con los nombres
        """
        sql = const.sql.SELECT.replace(';', '') + ' order by Nombre;'
        cur = self.conexion.cursor()
        cur.execute(const.sql.SELECT)
        filas = cur.fetchall()
        nombres = {0:""}
        nombres.clear()

        for fila in filas:
            nombres.update({int(fila['id']):fila['Nombre'] + ' ' + fila['Apellidos']})

        return nombres

    def personaByID(self, id):
        cur = self.conexion.cursor()
        cur.execute(const.sql.SELECT_BY_ID, str(id))
        persona = cur.fetchone()

        return persona

    def guardar(self, persona):
        """
        :param persona: tipo diccionario
        """
        cur = self.conexion.cursor()
        print(persona)

        if persona['id'] == -1:
            #insertar
            print('Insertando nuevo')
            cur.execute(const.sql.INSERT, (
                        persona['Nombre'],
                        persona['Apellidos'],
                        persona['Fijo'],
                        persona['ExtFijo'],
                        persona['Movil'],
                        persona['ExtMovil'],
                        persona['Email'],
                        persona['Departamento']))
            self.conexion.commit()
        else:
            #guardar
            print('guardando en ID: ' + str(persona['id']))
            cur.execute(const.sql.UPDATE, (
                        persona['Nombre'],
                        persona['Apellidos'],
                        persona['Fijo'],
                        persona['ExtFijo'],
                        persona['Movil'],
                        persona['ExtMovil'],
                        persona['Email'],
                        persona['Departamento'],
                        persona['id']))
            self.conexion.commit()

    def eliminar(self, id):
        cur = self.conexion.cursor()
        cur.execute(const.sql.DELETE, str(id))
        self.conexion.commit()







