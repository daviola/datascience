import numpy as np
# Array de 10 zeros
print(np.zeros(10))
#array de 10 1s
print(np.ones(10))
#array de 10 5s
print(np.ones(10)*5)
#array de inteiros de 10 a 50
print(np.arange(10,51))
#array de numeros pares de 10 a 50
print(np.arange(10,51,2))
#matriz 3x3 com valores de 0 a 8
print(np.arange(9).reshape(3,3))
#matriz identidade 3x3
print(np.eye(3))
#numero randomico entre 0 e 1
print(np.random.rand(1))
#gera array de 25 numeros randomicos
print(np.random.randn(25))
#cria um array de 20 numeros espacados igualmente entre 0 e 1
print(np.linspace(0,1,20))
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
#reproduzir o array acima
mat = np.arange(1,26).reshape(5,5)
print(mat)
#tirar o slice abaixo do array gerado anteriormente
# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
print(mat[2:,1:])
#tirar o numero 20 do array
print(mat[3,4])
#tirar o slice abaixo do array:
# array([[ 2],
#        [ 7],
#        [12]])
print(mat[:3,1:2])
#tirar o slice abaixo:
# array([21, 22, 23, 24, 25])
print(mat[4,:])
#tirar o slice abaixo:
# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
print(mat[3:5,:])
#soma valores do array:
print(mat.sum())
#desvio padrao dos valores no array
print(mat.std())
#soma todas as colunas
print(mat.sum(axis=0))