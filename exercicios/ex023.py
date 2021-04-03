# Desafio 023 -> Faça um programa que leia um número de 0 a 9999 e mostre
#                   na tela cada um dos digitos separados
#                  Ex: Digite um número: 2154
#                  unidade: 4
#                  dezena: 5
#                  centena: 1
#                  milhar: 2
#                  Tentar fazer em string e int

#   Versão em str

num = str(input('Digite um número inteiro entre 0 e 9999: '))
print('Unidade: {}\n'
      'Dezena : {}\n'
      'Centena: {}\n'
      'Milhar : {}'.format(num[0:1], num[1:2], num[2:3], num[3:4]))




#   Versão em int
import math
num2 = int(input('Digite outro número inteiro entre 0 e 9999: '))
#vamos por parte
x = num2 // 1
y = x % 10
num2u = num2 // 1 % 10
#un = num2
#dez = num2
#cen = num2
#mil = num2
print(y)
#print('Unidade: {}\n'
#      'Dezena : {}\n'
#      'Centena: {}\n'
#      'Milhar : {}'.format(un, dez, cen, mil))

conta = 100 % 13
print(conta)

#   num = 1234
#   u = num // 1 % 10
#	d = num // 10 % 10
#	c = num // 100 % 10
#	m = num // 1000 % 10
#	print('{u}\n{d}\n{c}\n{m}')
