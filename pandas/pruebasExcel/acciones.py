"""
    Clase donde se definiran las distintas acciones a realizar

"""
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import numpy as np
from pandas import Index
import sqlite3
from pandas.io import sql
import matplotlib.pyplot as plt

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

        #la siguiente linea es usando pypandas para guardar
        #df2[0:3].to_sql(name='tabla', con=cnx)

        #otra forma de hacerlo
        sql.write_frame(df2, name='tabla', con=cnx)

        print('Importados ', len(df2), ' registros')
        cnx.commit()
        cnx.close()

        print('Base de datos creada con exito')

    def df2sqlite(self, dataframe, tbl_name = 'tb'):
        """
        Codigo que permite escribir un dataframe usando sentencias
        de sqlite estandar sin framework ni usando pypandas casi
        :param dataframe:
        :param tbl_name:
        :return:
        """
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

    def prueba_recorrido_dataframe(self):
        """
        Consiste en intentar recorrer y mostrar el contenido de un
        dataframe
        """
        df = self.obtener_dataframe()
        df.reset_index()

        print(df.head(6))

        #ahora vamos a coger la tercera fila
        print('Mostrar datos de la tercera fila\r\n', df.iloc[3])

        print('\r\nDatos de fila tres y columna dos: ', df.iloc[3,2])
        df2 = df['Fecha']
        df2 = df2.combine_first(df['Neto'])

        print(df2.tail(5))
        #writer = pd.ExcelWriter('sale.xlsx')

        #df2.to_excel(writer, 'Salida')