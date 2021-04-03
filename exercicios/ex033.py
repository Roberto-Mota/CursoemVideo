# Desafio 033 -> Faça um programa que leia três número e mostre qual é o maior e qual é o menor

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))
lista = [num1, num2, num3]
lista.sort()
print('O número mais baixo é {}\n'
      'O número do meio é {}\n'
      'O número mais alto é {}'.format(lista[0], lista[1], lista[2]))
