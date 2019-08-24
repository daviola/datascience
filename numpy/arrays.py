import numpy as np

#lista normal
my_list = [1,2,3]
print("Lista Normal")
print(my_list)

#array criado a partir da lista
print("Array")
print(np.array(my_list))

#lista de listas 
print("Lista de Listas")
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

#matriz a partir da lista de listas
print("Matriz")
print(np.array(my_matrix))

print("arange 0 a 10")
print(np.arange(0,10))

print("arange 0 a 11 de 2 em dois")
print(np.arange(0,11,2))

print("Gera array de zeros")
print(np.zeros(3))

print("gera matriz de zeros")
print(np.zeros((5,5)))

print("array de 1s")
print(np.ones(3))

print("matriz de 1s")
print(np.ones((3,3)))

print("retorna numeros espacados igualmente")
print(np.linspace(0,10,3))
print(np.linspace(0,10,50))

print("matriz identidade")
print(np.eye(4))



#random

print("rand")
print(np.random.rand(2))
print(np.random.rand(5,5))

print("randn")
print(np.random.randn(2))
print(np.random.randn(5,5))

print("randint")
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))


#Array Attributes and Methods
print("Atributos e metodos de array")
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr)
print(ranarr)
print("reshape")
print(arr.reshape(5,5))
print("array randomico")
print(ranarr)
print("max")
print(ranarr.max())
print("argmax")
print(ranarr.argmax())
print("min")
print(ranarr.min())
print("argmin")
print(ranarr.argmin())

print("shape")
print(arr.shape)
print(arr.reshape(1,25))
print(arr.reshape(1,25).shape)
print(arr.reshape(25,1))
print(arr.reshape(25,1).shape)
print(arr.dtype)








