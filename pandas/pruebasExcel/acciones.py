""" Clase donde se definiran las distintas acciones a realizar

"""
import pandas as pd
import numpy as np
from pandas import Index
import sqlite3
from pandas.io import sql

import pandas.io
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Acciones:

    def __init__(self, ruta=''):
        self.RUTA_XLS = ruta

    def intentar_leer_archivo(self):
        archivo = pd.ExcelFile(self.RUTA_XLS)
        #leemos la primera hoja del excel
        df = archivo.parse(0)

        #leer las 5 primeras filas
        #print(df.head(5))
        #ver los tipos de datos identificados
        #print(df.dtypes)
        #ver los nombres de las columnas contenidas
        print(df.columns)

        print(df.describe())

    def obtener_dataframe(self):
        print('Obteniendo el dataframe ...')
        archivo = pd.ExcelFile(self.RUTA_XLS, dtype={'Fecha': str})
        df = archivo.parse(0)
        return df

    def volcar_datos_a_db(self):
        """
        Vuelca los datos del archivo excel a una base de datos
        :return:
        """
        #base = declarative_base()
        self.rutaDB = "/media/DATOS/PROYECTOS/2015/datos.db"
        engine_str = 'sqlite:///' + self.rutaDB
        #engine = create_engine()

        #base.metadata.create_all(engine)
        #conn = engine.connect()


        df = self.obtener_dataframe()
        df.reindex()
        #indice = Index(list(range(0, len(df))), name='indice')
        #df.reindex(index=indice,columns=df)
        df2 = df.reset_index()


        df2['Fecha'] = df2['Fecha'].apply(lambda x: str(x))
        df2['Apertura'] = df2['Apertura'].apply(lambda x: str(x))
        df2['Cierre'] = df2['Cierre'].apply(lambda x: str(x))
        print(df2.dtypes)
        #self.df2sqlite(df2, tbl_name='tabla')


        # Create your connection.
        cnx = sqlite3.connect(self.rutaDB)
        cur = cnx.cursor()
        cur.execute("drop table if exists tabla")
        cnx.commit()
        #df2[0:3].to_sql(name='tabla', con=cnx)

        sql.write_frame(df2, name='tabla', con=cnx)
        print('Importados ', len(df2), ' registros')
        cnx.commit()
        cnx.close()

        print('Base de datos creada con exito')

    def df2sqlite(self, dataframe, tbl_name = 'tb'):


        conn=sqlite3.connect(self.rutaDB)
        cur = conn.cursor()

        wildcards = ','.join(['?'] * len(dataframe.columns))
        data = [tuple(x) for x in dataframe.values]

        cur.execute("drop table if exists %s" % tbl_name)

        col_str = '"' + '","'.join(dataframe.columns) + '"'
        cur.execute("create table %s (%s)" % (tbl_name, col_str))
        print("insert into %s values(%s)" % (tbl_name, wildcards), data)
        cur.executemany("insert into %s values(%s)" % (tbl_name, wildcards), data)

        conn.commit()
        conn.close()