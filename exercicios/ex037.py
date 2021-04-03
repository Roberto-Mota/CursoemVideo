# Desafio 037 -> Escreva um programa que leia um número inteiro qualquer e peça para
#                o usuário escolher qual será a base de conversão.

#                1 para binário
#                2 para octal
#                3 para hexadecimal
from time import sleep
num = int(input('Digite um número \033[1minteiro\033[m: '))
bina = bin(num)
octa = oct(num)
hexa = hex(num)
sleep(0.5)
print('Existem três possibilidades de conversão:')
sleep(0.5)
print('Digite \033[1;32m1\033[m para Binário')
sleep(0.5)
print('Digite \033[1;32m2\033[m para Octal')
sleep(0.5)
print('Digite \033[1;32m3\033[m para Hexadecimal')
sleep(0.5)
base = int(input('Qual será a base de conversão? '))
if base == 1:
    print('O número {} em Binário é: {}'.format(num, bina[2:]))
if base == 2:
    print('O número {} em Octal é: {}'.format(num, octa[2:]))
if base == 3:
    print('O número {} em Hexadecimal é: {}'.format(num, hexa[2:]))
else:
    print('Você digitou um valor inválido para a conversão, tente novamente.')
