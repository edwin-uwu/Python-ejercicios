from math import pi
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
#Array una dimención
c = np.array([7,2,9,10]);
print(c);
#Array bidimencional
d = np.array([[1,2,3,4],[5,6,7,8]]);
print(d)
#Eliminar  0,1
print('Array ')
print(np.delete(d,1));
#Elimnar fila
print('Fila eliminada')
print(np.delete(d,1,axis=0));
print('Columna eliminada');
print(np.delete(d,1,axis=1));

#Añadir 
print('\n Añadir ')
print(np.append(d,[6,7]));

print(np.append(d,[[16],[17]],axis=1));

#Cambiar forma de array
print('\nCambiarForma Array')
ar = np.linspace(1,36,36);
print(ar);
print('Cambio de arreglo:\n',ar.reshape(6,6));
#Operaciones básicas
print('Operaciones con arrays');
a = np.array([2,3,6]);
b = np.array([4,7,9]);
m = [1,2,3];
n = [3,4,5];
print('Concatenación m + n\n',m+n);
print('Suma de elemnto a + b con operador\n',a+b);
print('Suma de elemento a + b con función\n',np.add(a,b));
print('Resta de elemnto a - b con operador\n',a-b)
print('Resta de elemnto a - b con función\n',np.subtract(a,b));
print('Multiplicación de elemnto a * b con operador\n',a*b);
print('Multiplicación de elemnto a * b con función\n',np.multiply(a,b));
print('División de elemnto a / b con operador\n',a/b);
print('División de elemnto a / b con función\n',np.divide(a,b));

m = np.array([1,2,3,4]);
print('Cubo de cada elemnto\n',np.power(m,3));
print('Logaritmo natural\n',np.log(m));

print('Cubo de cada uno ' , np.power(n,3));
print('Cuadrado de cada uno ', np.power(n,2));
print('Raiz cuadrada de cada uno',np.sqrt(n));
#Unidades trigonométricas
print('seno de cada uno',np.sin(n));
print('coseno de cada uno ',np.cos(n));
print('tangente de cada uno ',np.tan(n));
#Operaciones estadísticas con arrays
print('\n------------------------')
r = np.random.random([5]);
print(r)
print('Media: ',np.mean(r));
print('Mediana: ',np.median(r));
print('Normal: ', np.std(r));
print('Maximo: ',np.max(r));
print('Minimo: ',np.min(r));
#Álgebra lineal con arrays
print('\n--------------');
a = np.array([1,2,3]);
b = np.array([5,4,2]);
c = np.array([2,5,6]);
print('Producto punto: ',np.dot(a,b));
print('Producto cruz: ',np.cross(a,b));
m = np.array([a,b,c]);
print(m);

print('Calcular inversa: ',np.linalg.inv(m));
print('Calcular autovalores: ',np.linalg.eigvals(m))
print('Calcular traza: ',np.trace(m));
print('Cambiar filas por columnas: ',np.transpose(m));
#Sistema de ecuaciones lineales
print('\nSistema de ecuaciones lineales\nx+2y=3\n5x+4y=4');
a = np.array([[1,2],[5,4]]);
b = np.array([3,4]);
print(np.linalg.solve(a,b));