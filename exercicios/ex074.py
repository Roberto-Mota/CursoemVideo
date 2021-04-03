# Desafio 074 -> C. um pro. que vai gerar cinco números aleatórios e colocar em uma tupla.
#                Depois disso, mostre a listagem de números gerados e também indique o menor e maror valor na tupla
from random import randint
tupla = ()
for cont in range(0, 5):
    num = randint(0, 9)
    tupla += (num,)
print(f'A tupla gerada foi {tupla}, sendo que o menor valor foi {min(tupla)} e o maior foi {max(tupla)}')
