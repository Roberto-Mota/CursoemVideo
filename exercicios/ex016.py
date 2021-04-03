# Desafio 016 -> Crie um programa que leia um número qualquer pelo teclado e mostre
#               na tela a sua porção inteira
# Ex: Digite um numero: 8.145
#     O numero 8.145 tem a parte inteira 8
from math import trunc
numq = float(input('Digite um número qualquer: '))
numqi = trunc(numq)
print('A parte inteira de {} valor é {}'.format(numq,numqi))

# forma mais eficiente, com menos variável

numq2 = float(input('Digite outro valor: '))
print('A parte inteira de {} valor é {}'.format(numq2,trunc(numq2)))

# forma mais eficiente, sem importar módulo, só usar o int

numq3 = float(input('Digite um valor float: '))
print('A parte inteira de {} é {}.'.format(numq3,int(numq3)))