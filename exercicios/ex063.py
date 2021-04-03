# Desafio 063 -> Escreva um pgr que leia um numero N inteiro qlqer
#                e mostre na tela os N primeiros elementos de uma sequência de Fibonnacci
#                Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#                   Os números seguintes são sempre a soma dos dois números anteriores
#
num1 = 0
num2 = 1
vzs = int(input('Digite a quantidade de elementos da sequência de Fibonnacci: '))
while vzs != 0:
    vzs -= 1
    nums = num1 + num2
    print('{:^2} + {:^2} = {:^2}'.format(num1, num2, nums))
    num1 = num2
    num2 = nums
