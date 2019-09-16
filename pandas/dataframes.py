import numpy as np
import pandas as pd
from numpy.random import randn

#definindo uma seed para gerar os numeros randomicos
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print("imprimindo o dataframe")
print(df)
print("imprimindo uma coluna(retorna uma serie)")
print(df['W'])
#outra forma de acessar uma coluna
print(df.W)
print(type(df))
print(type(df['W']))
print("acessando mais de uma coluna(retorna um dataframe)")
print(df[['W','Z']])
print(type(df[['W','Z']]))
print("Adicionando uma coluna nova")
df['new'] = df['W'] + df['Y']
print(df)
print("Removendo uma coluna")
print(df.drop('new',axis=1))
print("o metodo drop retorna o dataframe sem a coluna, porem não altera o objeto por si só")
print(df)
print("Para remover dentro do proprio objeto, precisamos adicionar o argumento inplace")
df.drop('new',axis=1, inplace=True)
print(df)
print("Removendo um alinha, mudamos o argumento axis.")
print(df.drop('E',axis=0))
print("como o dataframe se deriva do numpy, tambem possui o metodo shape")
print(df.shape)
print("acessando linhas no dataframe")
print(df.loc['A'])
print("acessando linhas no dataframe por indice numerico")
print(df.iloc[0])
print("Acessando elemento apontando linha e coluna")
print(df.loc['B','Y'])
print("Acessando multiplos elementos apontando linhas e colunas")
print(df.loc[['A','B'], ['W', 'Y']])

