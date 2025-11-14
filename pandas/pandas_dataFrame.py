import pandas as pd 
import numpy as np
import matplotlib.pyplot as ptl

#Estudiantes = pd.Series([16,12,17],index=['Pepito','María','Ana']);
Estudiantes = pd.DataFrame({'edades':[16,12,17],'escolaridad':['S','S','U']},
                           index=['Pepito','María','Ana']);
print(Estudiantes);

print(Estudiantes.dtypes);
print(Estudiantes.index);
print(Estudiantes.axes);
print(Estudiantes.columns);
print(Estudiantes.values);