import numpy as np
import pandas as pd
from numpy.random import randn

#definindo uma seed para gerar os numeros randomicos
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print("Condicionais")
print(df>0)
print("Quando condicionamos o dataframe inteiro, os elementos que não atendem a condicao vem como NaN")
print(df[df>0])

print(df['W']>0)

print("Quando condicionamos por uma coluna, as linhas que não atendem a condicoes desta coluna são omitidas")
print(df[df['W']>0])
print(df[df['Z']<0])
print('acessando uma coluna do dataframe resultante da condicional')
print(df[df['W']>0]['X'])
print(df[df['W']>0][['Y','X']]) 
print("Multiplas condicoes")
print("em multiplas condicoes com series utilizamos o & ao inves do and e o | no lugar do or")
print(df[(df['W']>0) & (df['Y']>1) ])
print(df[(df['W']>0) | (df['Y']>1) ])
print("transformando o indice em uma coluna")
print(df.reset_index())
print("Assim como varios metodos, a mudanca nao ocorre no objeto ao menos que se passe o argumento inplace=True")
newind = 'CA NY WY OR CO'.split()
print(newind)
df['States'] = newind
print(df)
print("Setando uma coluna como indice")
print(df.set_index('States'))