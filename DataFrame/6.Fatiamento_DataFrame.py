#P11 Hello World!
import pandas as pd

# Cria DataFrame.
dados = {
        'nome': ['Argentina', 'Brasil', 'Franca', 'Italia','Reino Unido'],
        'continente': ['America', 'America', 'Europa', 'Europa', 'Europa'],
        'extensao': [2780, 8511, 644, 301, 244],
        'corVerde': [0, 1, 0, 1, 0]
        }

# Definir siglas para utilizar como índice.
siglas = ['AR','BR', 'FR', 'IT', 'UK']

# Criar DataFrame.
paises = pd.DataFrame(dados, index=siglas)
print(paises)

#Método de fatiamento.
paises['extensao']
paises.corVerde
paises.loc['BR']
paises.iloc[2]

# Fatiamento de  3 primeiras linhas e  duas primeiras colunas
print(paises.iloc[:3, :2]) # Primeiro linha e depois colunas.

# Fatiamento de paises que contenham a cor Verde.
print(paises.loc[['BR','IT'],'corVerde'])

# Fatiamento.
print(paises.iloc[-2:,1:3])