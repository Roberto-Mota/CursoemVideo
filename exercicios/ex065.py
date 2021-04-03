# Desafio 065 -> Crie um program que leia varios numeros int pelo teclado. No final da execução, mostre
#                a média entre todos os valores e qual foi o maior e o menor valores lidos. o programa
#                deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from typing import List

num_maxmin: list[int] = []
cont = 's'
pig = 0
media = 0
nums = 0
while cont == 's':
    numi = int(input('Digite um número inteiro: '))
    nums += numi
    pig += 1
    num_maxmin.insert(pig, numi)
    if pig % 5 == 0:
        cont = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
        while cont not in 'sn':
            cont = input('Digito inválido. por favor tente novamente.\nDeseja continuar? [S/N]').lower().strip()[0]
media = nums / pig
print('A média dos {} números que você digitou é {:.2f}, sendo que o maior número foi {} e o menor {}'. format(pig, media, max(num_maxmin), min(num_maxmin)))