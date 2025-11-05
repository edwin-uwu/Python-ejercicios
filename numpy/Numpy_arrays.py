import numpy as np


A = np.array([[1,2],[3,4]]);

print(A);

A = np.empty([3,2]);
print(A);

A = np.zeros([3,2]);
print(A);

A = np.identity(5);
print(A);

A = np.arange(1,101,0.5);
print(A);

A = np.linspace(1,101,5);
print(A);

A = np.random.rand(3,2);
print(A);

print(A.ndim);
print(A.shape);
print(A.size);
print(A.dtype);

B = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(B);

print(B[2,2]);
print(B[1,2]);
print(B[0,1]);

B[2,0] = 777;
print(B);
#Número 1,2,4,5
print(B[:2,:2]);
#Número 2,3,5,6
print(B[:2,1:3]);
#Número  5
print(B[1:2,1:2]);

#Arreglo de 100 elementos de 10 x 10
C = np.arange(100).reshape(10,10);
#Array de 100 elementos
print(C);
#Mostrar número 5
print(C[0,5]);
#Mostrar fila completa que empiece con 3
print(C[3,:10]);
#Mostrar columna completa que comienze con 2
print(C[:10,2]);
#Monstrar ultima columna
print(C[:10,9]);
#Mostrar bloque 2x2 numeros 0,1,10,11
print(C[:2,:2]);
#Muestra el bloque de 3x3 de la esquina inferior derecha. (Números 77, 78, 79, 87, 88, 89, 97, 98, 99).
print(C[7:10,7:10])
#Muestra los números 44, 45, 54, 55.
print(C[4:6,4:6])
#Muestra todas las filas pares (fila 0, 2, 4...).
print(C[::2,:])
print(C[::2,::2])

print(C[2:7,2:7]);

C = np.arange(1,101,0.5)
print(C)