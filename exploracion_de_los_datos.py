from traceback import print_tb
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv(r'weatherAUS.csv')

def menu():
        print('\t\tExploración de datos\n')
        opciones = ('1) Tamaño del Data Set\n'
                '2) Tipos de datos de cada columna\n'
                '3) Tratamiento de valores nulos\n'
                '4) Tecnicas de tratamiento de nulos\n'
                '5) Estadisticas Columnas\n'
                '6) Exit\n'
                'Opción: ')
        opcion = input(opciones)
        return int(opcion)
    
def opcion_1(dataFrame):
    tamaño = dataFrame.shape;
    print('\t\tTamaño del Data Set')
    print('Filas: ' + str(df.shape[0]))
    print('Columnas: ' + str(df.shape[1]))

def opcion_2(dataFrame):
    tipos = dataFrame.dtypes;
    print('\t\tTipos de datos de las columnas')
    print(tipos)
    
def opcion_3(dataFrame):
    total_nulos = 0
    for feature in dataFrame.columns:
        total_nulos += dataFrame[feature].isna().sum()
        print('Total de valores nulos de', feature, '=', dataFrame[feature].isna().sum())
        
    print('Total de datos con valores nulos: ' + str(total_nulos))

def listar_columnas(dataFrame, imprimir):
    contador = 0
    columns = []
    print("\t\tColumnas")
    for column in dataFrame.columns:
        contador += 1
        columns.append(str(column))
        if imprimir: 
            print(str(contador) + ")" + str(column))
    
    return columns

def describe_columna(dataFrame, column):
    tipo_column = dataFrame[column].dtypes
    print('Mínimo:',dataFrame[column].min())
    print('Máximo:',dataFrame[column].max())
    if(tipo_column == 'float64'):
        print('Promedio:',dataFrame[column].mean())
        print('STD:',dataFrame[column].std())
        print(dataFrame[column].quantile([.25, .5, .75]))

def opcion_5(dataFrame):
    columnas = listar_columnas(dataFrame, True)
    opcion = input('Opción: ')
    describe_columna(dataFrame, columnas[int(opcion) - 1])
    
while True:          
    choice = menu()
    if choice == 1:
        opcion_1(df)
    elif choice == 2:
        opcion_2(df)
    elif choice == 3:
        opcion_3(df)
    elif choice == 5:
        opcion_5(df)
    elif choice == 6:
        break
    input('Presiona Enter Para Continuar...\t')