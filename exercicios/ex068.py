# Desafio 068 -> Faça um pgr. que jogue par ou impar com o pc.
#                O jogo só para quando o grupo perder
#                Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
#                primeiro pede o numero, depois se impar ou par
import random
cont = numj = 0
brk = False
while numj >= 0 and brk is not True:
    numj = int(input('Escolha um número entre 0 e 5: '))
    while numj < 0 or numj > 5:
        numj = int(input('Valor inválido, por favor insira um número inteiro entre 0 e 5:'))
    nump = random.randint(0, 5)
    ioup = str(input('Você quer par ou ímpar? [I/P]')).strip().lower()[0]
    while ioup not in 'ip':
        ioup = input('Digito inválido, por favor tente novamente. [I/P]').strip().lower()[0]
    if ioup == 'i':
        if (numj + nump) % 2 == 0:
            print(f'\033[1;31mVocê perdeu\033[m, pois você jogou {numj} e o PC jogou {nump}')
            brk = True
            break
        else:
            print(f'\033[1;32mDeu impar\033[m, pois você jogou {numj} e o PC jogou {nump}')
            numj = 0
            ioup = 'f'
            cont += 1
    if ioup == 'p':
        if (numj + nump) % 2 == 0:
            print(f'\033[1;32mDeu par\033[m, pois você jogou {numj} e o PC jogou {nump}')
            numj = 0
            ioup = 'f'
            cont += 1
        else:
            print(f'\033[1;31mVocê perdeu\033[m, pois você jogou {numj} e o PC jogou {nump}')
            brk = True
            break
if cont == 0:
    print('Você ainda \033[1;31mperdeu de primeira\033[m, puts!')
if cont == 1:
    print(f'Seu jogo só durou 1 round')
elif cont > 0:
    print(f'Seu jogo durou {cont} rounds')
