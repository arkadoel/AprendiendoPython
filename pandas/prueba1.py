__author__ = 'root'
import pandas
import openpyxl


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

    print('\r\nAgrupaciones')
    '''
    Agrupemos los grupos de edad de las mujeres
    '''
    menores = mujeres[mujeres.Age < 20]
    los_veinte = mujeres[(mujeres.Age >= 20) & (mujeres.Age < 30)]
    mayores_treinta = mujeres[mujeres.Age >= 30]
    nulos = mujeres[mujeres.Age.isnull()]

    print('\tMenores: ', len(menores))
    print('\tEn los veinte', len(los_veinte))
    print('\tMayores 30: ', len(mayores_treinta))
    print('\tEdad desconocida: ', len(nulos))

    print('\t\tTotal mujeres: ', len(mujeres))

    #menores.to_excel('menores.xlsx', index=False)
