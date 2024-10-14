# Entendendo Algoritmos: Um guia para programadores e outros curiosos.

# Pesquisa Binária.

# Definição da lista de valores.
minha_lista = [1, 3, 5, 7, 9]

# Função para pesquisa binária.
def pesquisa_binaria(lista, item):
    baixo = 0 # Posição antes do meio da lista.
    alto = len(lista) - 1 # Posição depois do meio da lista.

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

print (pesquisa_binaria(minha_lista, 3))

# Exercício 1: Suponha que você tenha uma lista com 128 nomes e esteja fazendo um pesquisa binária. Qual seria o número
# máximo de etapas que você levaria para encontrar o nome desejado?

# 7 etapas.
# 8 etapas.

def pesquisa_binaria(tamanho, etapas):
    tamanho = 128
    etapas = 128/2 + minha_pesquisa (Não Onco)
    return
