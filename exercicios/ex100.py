# Desafio 100 -> Crie um programa que tenha uma lista chamada números e duas funções chamadas
#                   sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vai colocá-los
#                   dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
#                   sorteados pela função anterior.
from random import randint
numl = []
numlp = []


def sorteia():
    numl = []
    for n in range(0, 5):
        numl.append(randint(1, 30))
    print(f'A lista sorteada é: {numl}')
    return numl


def somapar():
    ntot = 0
    for n in numl:
        if n % 2 == 0:
            numlp.append(n)
    for n in numlp:
        if n == numlp[-1]:
            print(f'{n} =', end=' ')
        else:
            print(f'{n} +', end=' ')
        ntot += n
    print(ntot)


numl = sorteia()
somapar()
