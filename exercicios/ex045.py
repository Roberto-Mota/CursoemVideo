# Desafio 045 -> crie um programa que faça o computador jogar jokenpo com vc (pedra papel ou tesoura)
from random import choice
from time import sleep
from sys import exit
lista = ['pedra', 'papel', 'tesoura']
jk = str(input('Pedra, papel ou tesoura?'))
jkp = jk.strip().lower()
jkppc = choice(lista)
if jkp == 'pedra' or jkp == 'papel' or jkp == 'tesoura':
    print('Tudo bem, vamos lá!')
elif jkp != 'pedra' or jkp != 'papel' or jkp != 'tesoura':
    print('Acho que estamos jogando jogos diferentes, quer tentar novamente?')
    exit()
sleep(1)
print('\033[31;1mJo\033[m...')
sleep(1)
print('...\033[31;1mKen\033[m...')
sleep(1)
print('    ...\033[31;1mPô\033[m!')
sleep(1)
if jkp == 'pedra' and jkppc == 'pedra' or jkp == 'papel' and jkppc == 'papel' or jkp == 'tesoura' and jkppc == 'tesoura':
    res = ('Deu empate')
if jkp == 'pedra' and jkppc == 'tesoura' or jkp == 'papel' and jkppc == 'pedra' or jkp == 'tesoura' and jkppc == 'papel':
    res = ('Você ganhou')
if jkp == 'pedra' and jkppc == 'papel' or jkp == 'papel' and jkppc == 'tesoura' or jkp == 'tesoura' and jkppc == 'pedra':
    res = ('Você perdeu')
print('{}, pois você escolheu \033[1;32m{}\033[m e o \033[1mPython\033[m escolheu \033[33;1m{}\033[m!'.format(res, jkp, jkppc))
print('debug: {}'.format(jkppc))
