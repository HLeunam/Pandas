#P21: Quais os países que também têm verde, amarelo, azul
#     e branco entre as cores de sua bandeira nacional?
import pandas as pd

#--------------------------------------------------------------
# (1) - Importa a bse de dados
#--------------------------------------------------------------
flags = pd.read_csv(r'C:\Users\henri\OneDrive\Pessoal\Anotações\GitHub\Pandas\Bases\flags.csv')
#--------------------------------------------------------------
# (2) - Alguns métodos para obter informações básicas
#--------------------------------------------------------------
# Imprime as primeiras linhas
print(flags.head())
print('------------------------------------')
print(flags.tail())
print('------------------------------------')

#--------------------------------------------------------------
# (3) - Quem tem verde, amarelo, azul e branco na bandeira?
#--------------------------------------------------------------

# Separa as cores
verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']
soma = verde + amarelo + azul + branco

# Gera vetor booleano com True para quem tem as 4 cores.
tem_todas = (soma==4)

# Imprime os nomes dos países com as quatro cores.
print('paises com verde, amarelo, azul e branco:')
print(flags[tem_todas]['name'])