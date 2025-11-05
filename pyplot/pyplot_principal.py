from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(0,10,0.1);
#y= np.sin(x);
#z = np.cos(x);
##plt.plot(x,y,label='sin(x)');
##plt.plot(x,z,label='cos(x)');
#Personalización de gráficos
print('--------------------')
#plt.grid();#Regillas en el gráfico
#plt.title('Mi primer gráfico');#Título
#plt.legend();#Mostrar leyenda
#plt.xlabel('Eje X');#Título eje x
#plt.ylabel('Eje Y');#Título eje y
#plt.xlim(0,4);#Límites eje x

#plt.show();
#Tipo de gráficas
x = np.random.random([50]);
y = np.random.random([50]);
print(x);
print(y);
#Scatter plot grafica por puntos
#plt.scatter(x,y)

#Bar plot gráfica de barras
opciones=['si','no'];
resultados=[40,50];
#plt.bar(opciones,resultados);

#Histogramas
#plt.hist(x,15);

#Box plot
#plt.boxplot(x);

#pie plot
plt.pie(resultados,labels=opciones);
plt.show();