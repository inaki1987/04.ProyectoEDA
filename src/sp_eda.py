
import pandas as pd


def eda_prelim(df):
    
    display(df.sample(5))
    print('----------')
    print('DIMENSIONES')
    print(f'El conjunto de datos presenta {df.shape[0]} filas y {df.shape[1]} columnas')
    print('----------')
    print('INFORMACION DE COLUMNAS')
    display(df.info())
    print('----------')
    print('DUPLICADOS')
    print(f'Tenemos {df.duplicated().sum()} duplicados')
    print('----------')
    print('ELEMENTOS NULOS')
    display(df.isnull().sum()/df.shape[0]*100)
    print('----------')
    print('FRECUENCIA CATEGORÍAS')
    for col in df.select_dtypes(include='object').columns:
        print (df[col].value_counts())
        print('-----------')