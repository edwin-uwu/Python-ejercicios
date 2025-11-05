import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1);
y= np.sin(x);
z = np.cos(x);
plt.plot(x,y);
plt.plot(x,z);
plt.show();