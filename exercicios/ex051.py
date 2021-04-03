# Desafio 051 -> Desenvolva um programa que leia o primeiro termo e a razão de um Progressão aritmética.
#                   No final, mostre os 10 primeiros termos dessa prgressão

#acho que nao entendi o que pediu no enunciado mas fiz uma PA que inclusive deixa medir o segundo termo

num1 = int(input('Digite o valor do primeiro termo: '))
num2 = int(input('Digite o valor do segundo termo: '))
num3 = int(input('Digite o valor da constante: '))
for pa in range(num1, num2, num3):
    print('{}'.format(pa), end=' -> ')
print('P.A completa.')

# confome o desafio feito

ter1 = int(input('Digite o valor do termo: '))
raz = int(input('Digite o valor da razão: '))
dec = ter1 + (10 - 1) * raz
for unid in range(ter1, dec + raz, raz):
    print('{}'.format(unid), end=' -> ')
print('P.A completa.')