# Desafio 027 -> Faça um programa que leia o nome completo de uma pessoa,
#                   mostrando em seguida o primeiro e o útlimo nome separadamente
#                   Ex: Paulo Roberto Ramos Mota
#                   Primeiro = Paulo
#                   Último = Mota

nc = input('Qual o seu nome completo? ')
ncs = nc.split()
print('Primeiro: {}\n'
      'último: {}'.format(ncs[0], ncs[-1]))

# Praconta da esquerda pra direita: 0, 1, 2, 3, 4, 5, 6, 7...
#Pra contar da direita pra esquerda: ...-7, -6, -5, -4, -3, -2, -1.

#se eu imprimir o join pra frente da o último nome
#cprintada = int(nc.rfind(' '))
#print('Seu último nome é: {}'.format[cprintada:])


#import random
#random.
