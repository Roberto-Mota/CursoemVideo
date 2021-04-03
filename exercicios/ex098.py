# Desafio 098 -> Crie um programa que que tenha uma função chamada contador() que receba três parâmetros:
#                   Início, fim e passo e realize a contagem.
#               Seu programa tem que realizar três contagens através da função criada.
#                a) de um até 10 de 1 em 1
#                b) de 10 até 0, de 2 em 2
#                c) Uma contagem personalizada
from time import sleep
def contador(a, b, c):
    if a < b and c != 0:
        print('-' * 10)
        if c < 0:
            c = -c
        for u in range(a, b, c):
            print(u, end=' ')
            sleep(0.5)
            if (u + c) == b:
                sleep(0.5)
                print(b, 'Fim.')
    if b < a and c != 0:
        if c < 0:
            c = -c
        for u in range(a, b, -c):
            sleep(0.5)
            print(u, end=' ')
            if (u - c) == b:
                sleep(0.5)
                print(b, 'Fim.')
    if b == a or c == 0:
        print('Ai não rola, né meu brother!?')
    for l in range(0, 19):
        print('-' * 1, end='')
        sleep(0.1)
    print('-')


print('A)', end=' ')
contador(1, 10, 1)
print('B)', end=' ')
contador(10, 0, 2)
a = int(input('Digite o início da contagem: '))
b = int(input('Digite o fim da contagem: '))
c = int(input('Digite o passo da contagem: '))
contador(a, b, c)
