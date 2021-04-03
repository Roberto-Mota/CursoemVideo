# Desafio 028 -> Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#                 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
#                 O progrmaa deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep
print('Vamos jogar um jogo onde você descobre no que estou pensando?')
sleep(0.5)
denovo = 's'
while denovo == 's':
    sequencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    numr = random.choice(sequencia)
    nume = int(input('Escolha um número entre 0 e 10 e direi se você acertou: '))
    print('\033[1;32mHmmm...\033[m')
    sleep(1)

    tentar = input('Quer tentar adivinhar que número eu pensei? [S/N]').strip().lower()
    while tentar != 's' and tentar != 'n':
        tentar = str(input('Acho que não entendi, quer tentar adivinhar o número que pensei? [S/N]')).strip().lower()
    if tentar == 's':
        chute = 11
        palpites = 0
        while numr != chute:
            chute = int(input('Qual número você acha que eu pensei? '))
            palpites += 1
            if numr == chute:
                if palpites == 1:
                    print('Caraca! Você acertou de primeira, como conseguiu?')
                elif palpites < 4:
                    print('Boa, mas você precisou de {} palpites pra acertar.'.format(palpites))
                else:
                    print('É.. você acertou, mas depois de {} palpites fica fácil!'.format(palpites))
            elif numr > chute:
                print('Mais...', end=' ')
            elif numr < chute:
                print('Menos...', end=' ')
    elif tentar == 'n':
        sleep(0.5)
        print('Tudo bem.')
        sleep(1)
        if nume > 10:
            print('Muito engraçadinho, escolha entre 0 e 10 apenas, não me venha com números maiores que 10!')
        elif nume < 0:
            print('Número \033[7mnegativo\033[m pra que? Pedi para escolher de 0 a 10!')
        elif numr == nume:
            print('Você \033[1;32macertou\033[m, como você conseguiu adivinhar?')
        else:
            print('Eu sabia que você ia \033[1;31merrar\033[m, eu pensei no número {}!'.format(numr))
    denovo = input('Você quer jogar denovo? [S/N]').strip().lower()
    if denovo == 'n':
        print('Tudo bem, tenha um bom dia!')
