# Aula 17 -> Variáveis Compostas (Listas) Nessa aula, vamos aprender o que são LISTAS
# e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar
# vários valores em uma mesma estrutura, acessíveis por chaves individuais.
lanche = ['Cachorro Quente', 'Pizza', 'Suco', 'Sorvete']
print(dir(lanche))
# Formas de eliminar algo da lista:
del lanche[3]
lanche.pop(3) #geralmente pra remover o último index da lista
lanche.remove('Sorvete')
lanche.insert(2, 'Goiaba') #Insere Goiaba no index 2
# Existe a possibilidade de criar listas através de ranges
valores = list(range(4, 11))
# Vai criar uma lista com os valores de 4 até 10, com os index de 0 até 6
valores.sort(reverse=True) #organiza em ordem ao contrário