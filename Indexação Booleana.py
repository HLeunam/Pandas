# P0: Indexação booleana.
import pandas as pd

# Cria as series "notas" e "alunos".
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
alunos = pd.Series({'M02':'Bob',
                    'M05':'Dayse',
                    'M13':'Bill',
                    'M14':'Cris',
                    'M19':'Jimi'})

# Obtém os índices dos alunos aprovados.
idx_aprovados = notas[notas >= 7].index

# Imprime os alunos aprovados.
print('Relacao de alunos aprovados:')
print('----------------------------')
print(alunos[idx_aprovados])