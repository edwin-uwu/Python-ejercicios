import pandas as pd

df1 = pd.read_excel('figurasanime.xlsx');
#print(df1);

#df2 = pd.read_csv('archivo.csv',sep='\s+');
#print(df2.head()) #Primeras 5 filas
#print(df2.tail())# Ultimas 5 filas
#print(df1.shape())#Muestra filas y columnas cantidad 

#print(df1.head(2))
#print(df1.sample(12))
#print(df1.describe())
#print(df1.info())
#Accediendo datos de dataframe

df3 = pd.read_excel('figurasanime.xlsx');
df3.set_index('nombre',inplace=True);
#print(df3.head());

print(df3['anime'].head(10)); # obtener columnas
print(df3.iloc[7]);#Obtener datos por filas

#Rangos y filtrado de datos

print(df3.iloc[37:]);
print("\n",df3[(df3['distance'] > 6) & (df3['climb']> 5)])
