__author__ = 'Arkadoel'
import sys
import sqlite3
from Constantes import const

class db:
    conexion = None

    def __init__(self):
        self.conectar()

    def conectar(self):
        try:

            self.conexion = sqlite3.connect(const.DB_PATH)

            #para evitar errores TypeError: tuple indices must be integers, not str
            self.conexion.row_factory = sqlite3.Row # its key
        except sqlite3.Error as e:

            print("Error %s:" % e.args[0])
            sys.exit(1)

    def ejecutarSQL(self, sql, parametros):
        self.conectar()
        cur = self.conexion.cursor()
        print(sql, parametros)
        n = cur.execute(sql, parametros)
        self.conexion.commit()
        self.cerrarDB()
        return n

    def consultaSQL(self, sql):
        self.conectar()
        cur = self.conexion.cursor()
        print(sql)
        cur.execute(sql)
        filas = cur.fetchall()
        self.cerrarDB()
        return filas

    def consultaUnicaSQL(self, sql):
        self.conectar()
        cur = self.conexion.cursor()
        print(sql)
        cur.execute(sql)
        unico = cur.fetchone()
        self.cerrarDB()
        return unico

    def cerrarDB(self):
        if self.conexion is not None:
            self.conexion.close()
            self.conexion = None


