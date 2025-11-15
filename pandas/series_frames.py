import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fromas de crear series
Estudiantes ={'Felipe':18,'Diana':19}
print(pd.Series(Estudiantes, index=['Felipe','Diana','Alejandro']));

#Escalar
x = pd.Series(8,index=['a','p','c']);
print(x);

a= np.array([[1,2],[4,6]]);
print(a)
aa = pd.DataFrame(a,index=['a','b'],columns=['col1','col2']);
print(aa)