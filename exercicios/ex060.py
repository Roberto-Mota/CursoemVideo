# Desafio 060 -> Faça um programa que leia um numero qualquer e mostre o seu fatorial.
#                Ex: 5! = 5x4x3x2x1=120
#                desafio extra: tentar fazer com for tbm
import math
num = int(input('Digite um número inteiro que deseja saber o fatorial: '))
numfatorado = math.factorial(num)
numm = 0
numb = num
pig = num
while pig != 1:
    numm = (num*(pig-1))
    num = numm
    pig -= 1
print('o fatorial de {} ({}!) é igual a {}.'.format(numb, numb, numm))

# Jeito do professor
#num2 = int(input('Digite um número inteiro que deseja saber o fatorial: '))
#c = num2
#f = 1
#print('Calculando {}! = '.format(num2), end='')
#while c > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
#print(f)

# desafio com for:
f = 0
num3 = int(input('Digite um número inteiro que deseja saber o fatorial: '))
print('Calculando {}! = '.format(num3), end='')
for each in range((num3-1), 0, -1):
    f = num3*each
    print('{}'.format(each), end='')
    print(' x ' if each > 1 else ' = ', end='')
    num3 = f
print(f)