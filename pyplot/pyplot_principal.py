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
#x = np.random.random([50]);
#y = np.random.random([50]);
#print(x);
#print(y);
#Scatter plot grafica por puntos
#plt.scatter(x,y)

#Bar plot gráfica de barras
#opciones=['si','no'];
#resultados=[40,50];
#plt.bar(opciones,resultados);

#Histogramas
#plt.hist(x,15);

#Box plot
#plt.boxplot(x);

#pie plot
#plt.pie(resultados,labels=opciones);

print('--------------------')
#Tamaños, colores, estilos de linea y marcadores

y = np.array([1,4.3,17,16.8,30,25,50,45,100]);
x = np.array([1,2,3,4,5,6,7,8,9]);


#Largo y Ancho
plt.figure(figsize=(12,6));
plt.grid();
#plt.plot(x,y,'o:b') Azul
plt.plot(x,y,'o--',c='purple',mfc='red',mec='green',ms='10');
plt.show();