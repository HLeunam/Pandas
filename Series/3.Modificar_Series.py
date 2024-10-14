# P05: Inserindo, Alterando e Removendo elementos da Series.
import pandas as pd

# Cria a Series "alunos".
alunos = pd.Series({'M02':'Bob',
                    'M05':'Dayse',
                    'M13':'Bill',
                    'M14':'Cris',
                    'M19':'Jimi'
                    })

print('Series original:')
print(alunos)
print('----------------')

# Insere o aluno de matrícula M55, Rakesh.
alunos['M55'] = 'Rakesh'
print('Serie com o M55: Rakesh')
print(alunos)
print('----------------')

# Altera os nomes Bill, Cris e Jimi para Billy, Cristy e Jimmy.
alunos['M13'] = 'Billy'
alunos[['M14', 'M19']] = ['Cristy', 'Jimmy']
print('Serie com nomes alterados:')
print(alunos)

# Remove o aluno de matrícula M02 (Bob).
alunos = alunos.drop('M02')
print('Series sem aluno M02')
print(alunos)