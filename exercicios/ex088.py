# Desafio 088 -> C. um programa que ajude um grupo da mega sena a criar palpites.
#                O programa vai perguntar quantos jogos serão gerados e vai sortear
#                6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# Ex: Quantos jogos sorteia? (input)
#     Sorteando (input jogos)
#     Jogo x(input (um embaixo do outro, com timer, se possivel)

from random import randint
from time import sleep
numsor = -1
jogo = cont = 0
qtd = int(input('Quantos jogos serão sorteados?'))
mega = [[] for i in range(0, qtd)]
print(f'Sorteando {qtd} jogos:')
for pos in range(0, qtd):
    while cont <= 6:
        numsor = randint(0, 60)
        if numsor not in mega[jogo]:
            mega[jogo].append(numsor)
            numsor = -1
            cont += 1
        if len(mega[jogo]) == 6:
            cont = 0
            break
    jogo += 1
for pos, jogo in enumerate(mega):
    print(f' Jogo {pos+1:>2}: {sorted(mega[pos])}')
    sleep(1)

# jeito do professor
print('__FORMA 2__')
cont = 0
tot = 1
lista = []
jogos = []
quant = int(input('Quantos jogos você quer sortear? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
