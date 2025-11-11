from turtle import color
import numpy as np;
import matplotlib.pyplot as plt;

x = np.linspace(0,10,200);
y1 = np.sin(x);
y2 = np.exp(x);
y3 = np.power(x,2);
y4 = np.cos(x);

fig, ax = plt.subplots(2,2,figsize=(16,9));
fig.suptitle('Graficas de datos');
ax[0,0].plot(x,y1,color='red');
ax[0,0].set_title('Sen(x)',color='blue');
ax[0,1].scatter(x,y2);
ax[0,1].grid();
ax[1,0].plot(x,y3);
ax[1,0].set_xlabel('Eje X')
ax[1,0].set_ylabel('Eje Y')
ax[1,1].plot(x,y4);
ax[1,1].set_title('Cos(x)');

plt.show();