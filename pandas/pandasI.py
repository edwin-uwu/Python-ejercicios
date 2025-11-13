import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Series de datos
Estudiantes = pd.Series([16,12,17],index=['Pepito','María','Ana']);
print(Estudiantes);
print(Estudiantes['Pepito'])
print(Estudiantes[2])
print(Estudiantes.index)
print(Estudiantes.values)
print(Estudiantes.shape)