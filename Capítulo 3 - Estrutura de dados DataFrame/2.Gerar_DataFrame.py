#P11 Hello World!
import pandas as pd

# Cria DataFrame.
dados = {
        'nome': ['Argentina', 'Brasil', 'Franca', 'Itália','Reino Unido'],
        'continente': ['America', 'America', 'Europa', 'Europa', 'Europa'],
        'extensao': [2780, 8511, 644, 301, 244],
        'corVerde': [0, 1, 0, 1, 0]
        }

# Definir siglas para utilizar como índice.
siglas = ['AR','BR', 'FR', 'IT', 'UK']

# Criar DataFrame.
paises = pd.DataFrame(dados, index=siglas)

# Imprime o DataFrame.
print(paises)