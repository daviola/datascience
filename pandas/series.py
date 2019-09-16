import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
print("series sem definir o index")
print(pd.Series(data = my_data))
print("series com o index")
print(pd.Series(data = my_data, index=labels))
#pode ser declarado assim tambem
pd.Series(my_data, labels)
print("Agora passamos um dicionario para criar uma serie")
print(pd.Series(d))
print("uma serie pode armazenar varios tipos de dados alem de números, assim como letras, strings , referencias de funcoes entre outros")
print(pd.Series(data=labels))

ser1 = pd.Series([1,2,3,4],['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)
print(ser2['USA'])

ser3 = pd.Series(data=labels)
print(ser3)
print(ser3[0])

print("Nos podemos fazer operacoes com series, neste caso somamos ser1 e ser2")
print(ser1+ser2)
print("A operacao é realizada baseada nos indices, portanto se um indice não é encontrado nas duas series ele retorna um valor NaN")