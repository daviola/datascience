import numpy as np
#Creating sample array
arr = np.arange(0,11)
print(arr)

#Get a value at an index
print("acessar elemento de um array se faz da mesma forma que uma lista")
print(arr[8])
print(arr[1:5])
print("Broadcasting:\nDiferente das listas, o array tem a capacidade de fazer broadcast de um valor para varios elementos do array.")
#atribui o valor 100 para os elemento de indice 1 a 4
arr[1:5]=100
print(arr)
# resetamos o array
arr = np.arange(0,11)
print(arr)
print("Slice de array\n Observe que os elementos não são copiados para a outra variável, são apenas referenciados, ou seja, as alterações feitas no slice se refletem no array original")
slice_of_arr = arr[0:6]
print(slice_of_arr)
#broadcast de numero 99 para os elementos do slice
slice_of_arr[:]=99
print(slice_of_arr)
print(arr)
#para copiar o array, tem que se fazer de maneira explicita conforme abaixo
arr_copy = arr.copy()

print("indexando matrizes")
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)
print("acessa primeira linha")
print(arr_2d[0])
# Format is arr_2d[row][col] or arr_2d[row,col]
# Getting individual element value
print("acessa elemento individual")
print(arr_2d[1][0])
print(arr_2d[1,0])
print("slice de matriz")
print(arr_2d[:2,1:])
print("acessa ultima linha de duas formas:")
print(arr_2d[2])
print(arr_2d[2,:])

print("acesso de linhas individuais")
#geramos uma matriz
arr2d = np.zeros((10,10))
#pega quantas linhas tem o array
arr_length = arr2d.shape[1]
#atribui valores para cada uma das linhas
for i in range(arr_length):
    arr2d[i] = i
print("array completo")    
print(arr2d)
print("linhas 2 4 6 8 ")
print(arr2d[[2,4,6,8]])
print("linhas 6 4 2 7 ")
print(arr2d[[6,4,2,7]])

print("selecao condicional")
arr = np.arange(1,11)
print(arr)
print(arr > 4)
bool_arr = arr>4
print("mostra maiores que 4")
print(arr[bool_arr])
print("mostra maiores que 2")
print(arr[arr > 2])