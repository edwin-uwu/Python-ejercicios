import numpy as np;
import matplotlib.pyplot as plt;

x = np.linspace(0,10,200);
y1 = np.sin(x);
y2 = np.exp(x);
y3 = np.power(x,2);
y4 = np.cos(x);

fig, ax = plt.subplots(2,2,figsize=(16,9));
ax[0,0].plot(x,y1);
ax[0,1].plot(x,y2);
ax[1,0].plot(x,y3);
ax[1,1].plot(x,y4);

plt.show();