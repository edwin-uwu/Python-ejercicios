import pandas as pd
import numpy as np

s1 = pd.Series([1,np.nan,3,np.nan,5]);
print(s1);
df4 = pd.DataFrame({'A':[1,2,np.nan,4],'B':[3,2,5,5],'C':[np.nan,7,np.nan,2]},index=['Ene','Feb','Mar','Abr']);
print(df4);

print('Monstrar nulos\n')
print(s1.isnull());
print(df4.isnull());
print('No mostrar nulos')
s1_sin_nulos = s1.dropna();
print(s1_sin_nulos);
df4_sin_nulos_filas = df4.dropna();
df4_sin_nulos_columnas = df4.dropna(axis=1);
print('Normal\n',df4_sin_nulos_filas);
print('Columnas\n',df4_sin_nulos_columnas);
