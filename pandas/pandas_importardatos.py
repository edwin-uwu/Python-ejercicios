import pandas as pd

df1 = pd.read_excel('figurasanime.xlsx');
print(df1);

df2 = pd.read_csv('archivo.csv',sep='\s+');
print(df2.head()) #Primeras 5 filas
print(df2.tail())# Ultimas 5 filas
print(df1.shape())#Muestra filas y columnas cantidad 