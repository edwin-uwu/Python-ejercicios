import numpy as np
import matplotlib.pyplot as plt
#Análisis de Temperaturas Mensuales

dias = np.arange(1,31);
temperaturas = 25+5* np.random.randn(30);

promedio = np.mean(temperaturas);
max = np.max(temperaturas);
min = np.min(temperaturas);
tMax = dias[np.argmax(temperaturas)];
tMin = dias[np.argmin(temperaturas)];

print('Temperatura promedio del Mes: ', promedio);
print('Temp Max : ',max,'\nTemp: min', min);
print('Día temperatura maxima: ', tMax);
print('Día temperatura minima: ', tMin);

plt.figure(figsize=(10, 5))
plt.plot(dias, temperaturas, label='Temperatura diaria')
plt.axhline(promedio, color='red', linestyle='--', label='Promedio')
plt.scatter(tMax, max, color='red', zorder=5, label='Día más caluroso')
plt.scatter(tMin, min, color='blue', zorder=5, label='Día más frío')
plt.title('Temperaturas Máximas Diarias (30 días)')
plt.xlabel('Día del mes')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()