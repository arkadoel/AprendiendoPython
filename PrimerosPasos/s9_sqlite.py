#!/usr/bin/python
from pydoc import doc

__author__ = 'fer'
'''
    Probando a usar bases de datos sqlite
'''

import sqlite3
import sys

class DB:
    con = None
    cur = None
    dbName = ""

    def __init__(self, dbName):
        DB.dbName = dbName
        DB.con = sqlite3.connect(dbName)
        DB.cur = DB.con.cursor()

    def CrearTablas(self):
        if not self.ExisteTabla('albums'):
            self.cur.execute("""CREATE TABLE albums
                      (title text, artist text, release_date text,
                       publisher text, media_type text)
                   """)
            print('Tabla creada')
        else:
            print('Tabla ya existia')

    def InsertarDatos(self):
        #insertar una vez
        self.cur.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")

        # save data to database
        self.con.commit()

        # insertar multiples lineas
        albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
                  ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
                  ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
                  ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
        self.cur.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
        self.con.commit()

    def LeerFilas(self):
        sql = '''
            select * from albums
            '''
        self.cur.execute(sql)

        filas = self.cur.fetchall()

        for fila in filas:
            print(fila)


    def ExisteTabla(self, nombreTabla):
        """
        Mira a ver si existe una tabla
        :param nombreTabla:
        :return: True or False
        """
        resultado = False

        sql='''
            SELECT name FROM sqlite_master
            WHERE type='table'
            ORDER BY name;
            '''
        self.cur.execute(sql)
        fila = self.cur.fetchone()

        if len(fila) > 0:
            #cojamos la columna
            columna = fila[0]
            if columna == nombreTabla:
                resultado = True

        return resultado


def main():

    db = None

    seguir = True

    while seguir:
        print('''


            1.- Crear/abrir base de datos
            2.- Crear tablas
            3.- Insertar datos
            4.- Leer filas
            5.- Existe una tabla albumsS

            9.- Cerrar y salir
            ''')
        opcion = int( input('Opcion: '))

        if opcion == 1:
            db = DB('database.db')
        elif opcion == 2:
            db.CrearTablas()
        elif opcion == 3:
            db.InsertarDatos()
        elif opcion == 4:
            db.LeerFilas()
        elif opcion == 5:
            print(db.ExisteTabla('albumss'))
        elif opcion == 9:
            db.con.close()
            print('DB Cerrada')
            seguir = False



if __name__ == '__main__':
    main()