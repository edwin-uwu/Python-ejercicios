import numpy as np

a = np.array([[1,7,3,4],[2,12,4,1],[2,9,7,8]]);
print(a);
#Multiplos 2
print(a[a%2==0]);
#Pares y mayores a 4
print(a[(a%2==0)&(a > 4)]);
#Números multiplos de 2 o multiplos de 3
print(a[(a%2==0)|(a%3==0)]);

#Array
f1 = [1,2,3,4];
b = np.array([f1,[3*k for k in f1 ],[(3*k)**2 for k in f1]]);
print(b)
#pares
print('Numeros impares cantidad: ',b[a%2!=0].size);
#