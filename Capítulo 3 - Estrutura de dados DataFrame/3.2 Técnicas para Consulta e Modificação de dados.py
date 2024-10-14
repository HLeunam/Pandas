# Técnicas para consulta e modificação de dados.

#P13: Busca em DataFrames.
import pandas as pd

# Cria o DataFrame.
dados = {
        'nome': ['Argentina','Brasil','Franca','Italia'],
        'continente': ['America','America','Europa','Europa'],
        'extensao': [2780, 85111, 644, 301],
        'corVerde': [0,1,0,1]
        }

siglas = ['AR','BR','FR', 'IT']

paises = pd.DataFrame(dados, index=siglas)
print(paises)

# Testa se um dado rótulo de linha existe.
tem_BR = 'BR' in paises.index
tem_US = 'US' in paises.index
print("Existe rotulo 'BR'? ->", tem_BR)
print("Existe rotulo 'US'? ->", tem_US)
print('------------------------------')

# Testa se um dado rótulo de coluna existe.
tem_corVerde = 'corVerde' in paises.columns
tem_corAzul = 'corAzul' in paises.columns
print("Existe o rotulo 'corVerde?' -> ", tem_corVerde)
print("Existe o rotulo 'corAzul?' -> ", tem_corAzul)
