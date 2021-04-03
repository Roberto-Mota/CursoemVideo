# Desafio 032 -> Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
anoq = int(input('Que ano você quer saber se é bissexto? (Digite 0 para saber seu ano atual) '))
if anoq == 0:
    anoq = date.today().year
if (anoq % 400) == 0 or (anoq % 4) == 0:
    print('É ano bissexto')
elif (anoq % 100) == 0:
    print('Não é ano bissexto')
else:
    print('Não é ano bissexto')

    # peguei do wiki

ano = int(input('Wikipedia pergunta que ano você quer saber: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')