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

# Recupera e imprime as propriedades.
print('----------')
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index
colunas = paises.columns
paises_tipo = type(paises)
paises_dtypes = paises.dtypes
paises_idx_dtype = paises.index.dtype

print('numero de linhas:', num_linhas)
print('numero de colunas:', num_colunas)
print('rotulos das linhas:', indices)
print('rotulos das colunas:', colunas)
print('tipo (type):', paises_tipo)
print('dtype das colunas:\n', paises_dtypes)
print('dtype dos rotulos das linhas:', paises_idx_dtype)
