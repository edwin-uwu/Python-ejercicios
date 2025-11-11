import numpy as np
import matplotlib.pyplot as plt

#Configuración de rango de los ejes
y = np.array([1,4.3,17,16.8,30,25,50,45,10]);
x = np.array([1,2,3,4,5,6,7,8,9]);

plt.figure(figsize=(12,6));
plt.grid();
plt.plot(x,y,'o:',mfc='c',mec='r',ms=10);
plt.xticks([1,3,5,7,9],[2000,2002,2004,2006,2008],rotation='vertical');
plt.show();