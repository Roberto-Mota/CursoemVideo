# Desafio 038 -> Escreva um programa que leia dois números inteiros e compare-os,
#                mostrando na tela uma mensagem

#               - O primeiro valor é maior
#               - O segundo valor é menor
#               - Não existe valor maior, os dois são iguais
print('Vamos descobrir qual valor é maior?')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 == num2:
    print('Não existe valor maior, os dois são iguais')
if num1 > num2:
    print('O {} é maior que {}'.format(num1, num2))
if num1 < num2:
    print('O {} é menor que {}'.format(num1, num2))
