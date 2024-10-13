# P02: Propriedades básicas das Series.
import pandas as pd

# Cria a Series "alunos":
alunos = pd.Series({'M02':'BOB',
                    'M05':'Dayse',
                    'M13':'Bill',
                    'M14':'Cris',
                    'M19':'Jimi'
                    })

# Atribui nomes p/ os vetores de dados e rótulos.
alunos.name = "alunos"
alunos.index.name = "Matriculas"

# Recupera e imprime as propriedades.
print(alunos)
print('-----------')
tamanho = alunos.size
dados = alunos.values
rotulos = alunos.index
alunos_tipo = type(alunos)
alunos_dtype = alunos.dtype
alunos_idx_dtype = alunos.index.dtype

print('Numero de elementos: ', tamanho)
print('Vetor de dados: ', dados)
print('Vetor de rotulos: ', rotulos)
print('tipo (type): ', alunos_tipo)
print('dtype da Series: ', alunos_dtype)
print('dtype do vetor de rotulos: ', alunos_idx_dtype)


# Obter o aluno através do index.
alunos[0] # Obtém o primeiro aluno.
alunos[-1] # Obtém o último aluno.
alunos['M14'] # Obtém aluno pelo número da matricula.

# Fatiamento por intervalos.
alunos[i:j]

# Exemplos de fatiamento.
alunos[0:2] # Primeiro e terceiro elementos.
alunos[2:4] # Terceiro e quinto elementos.
alunos [:2] # Dois últimos elementos da série.
alunos[2:] # Três primeiros elementos da série.
alunos[-2:] # Dois últimos elementos.
alunos[[2,0,4]]
