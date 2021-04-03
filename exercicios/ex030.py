# Desafio 030 -> Crie um programa que leia um numero inteiro e diga se ele é par ou impar

import math
num = int(input('Digite um número inteiro: '))
numd = num % 2
print ('{} é par'.format(num) if numd == 0 else '{} é ímpar'.format(num))
#    print('{} é par'.format(num))
#else:
#    print('{} é ímpar'.format(num))

