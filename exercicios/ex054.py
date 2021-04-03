# Desafio 054 -> Crie um programa que leia o ano de nascimento de sete pessoas.
#                   No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
pig = 0
dmeno = 0
hj = date.today().year
for pes in range(1, 8, 1):
    anon = int(input('Digite seu ano de nascimento: '))
    if (hj - anon) > 21:
        pig += 1
    elif (hj - anon) <= 21:
        dmeno += 1
print('{} pessoas já atingiram a maior idade de 21 anos, enquanto {} não atingiram.'.format(pig, dmeno))
