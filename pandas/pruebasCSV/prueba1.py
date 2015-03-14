__author__ = 'root'
import pandas
from pandas import ExcelWriter
import xlsxwriter


archivo = './train.csv'


if __name__ == '__main__':
    data = pandas.read_csv(archivo)

    #print(data) imprime lo guardado
    #data.Name muestra la columna Name del .csv

    '''
        para filtrar
        print(data[data.Sex == 'male'])
    '''

    hombres = data[data.Sex == 'male']
    mujeres = data[data.Sex == 'female']

    num_hombres = len(hombres)
    num_mujeres = len(mujeres)

    print('Numero de hombres ', num_hombres)
    print('Numero de mujeres ', num_mujeres)

    print(data.columns)
    print(data.xs(0))

    #guardar las mujeres a otro CSV
    #mujeres.to_csv('mujeres.csv', index=False)

    print('\r\nAgrupaciones por rangos de edad:')
    '''
    Agrupemos los grupos de edad de las mujeres
    '''
    menores = mujeres[mujeres.Age < 20]
    los_veinte = mujeres[(mujeres.Age >= 20) & (mujeres.Age < 30)]
    mayores_treinta = mujeres[mujeres.Age >= 30]
    nulos = mujeres[mujeres.Age.isnull()]

    print('\tMenores de 20: ', len(menores))
    print('\tVeinteañeras', len(los_veinte))
    print('\tMayores 30: ', len(mayores_treinta))
    print('\tEdad desconocida: ', len(nulos))

    print('\t\tTotal mujeres: ', len(mujeres))

    '''
    GUARDAR LOS DATOS A UN EXCEL
    '''
    #menores.to_excel('menores.xlsx', sheet_name='menores', engine='xlsxwriter')

    writer = pandas.ExcelWriter('menores.xlsx')
    menores.to_excel(writer,'Menores de 20')
    los_veinte.to_excel(writer, 'Veintena')
    mayores_treinta.to_excel(writer,'Mayores de 30')
    nulos.to_excel(writer, 'Edad desconocida')

    estadistico = writer.book.add_worksheet('Estadistico')

    writer.save()

