#Desafio 005 -> Faça um programa que leia um número inteiro e mostre
#               na tela o seu sucessor e seu antecessor

numero = int(input('Digite o número inteiro:'))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor do número inteiro é {} e o antecessor é {}'.format(sucessor, antecessor))

# Ou de forma mais eficiente

snumero = int(input('Digite o número inteiro: '))
print('Como o valor é {}, o sucessor do número é {} e o antecessor é {}'.format(numero, (numero+1), (numero-1)))