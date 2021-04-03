# Desafio 105 -> Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar
#                a palavra 'FIM', o programa se encerrará.
#                OBS: Use cores
from time import sleep


def syspyhelp(msg):
    while True:
        print('\033[1;32m')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Sistema de ajuda interativa')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        sleep(0.5)
        print('\033[1;31m')
        aju = input(msg)
        print('\033[1;33m')
        sleep(0.5)
        if aju == 'FIM':
            print('~~~~~~~~~~~~~~~~~~')
            print('Sistema finalizado')
            print('~~~~~~~~~~~~~~~~~~')
            break
        print(help(aju))
        print('\033[m')


syspyhelp('Biblioteca ou Função => ')


# Jeito do professor
c = ('\033[1;31m',  # 0 - vermelho em negrito
     '\033[1;34m',  # 1 - azul em negrito
     '\033[1;33m',  # 2 - amarelo em negrito'
     '\033[1;30m',  # 3 - branco em negrito'
     '\033[1;35m',  # 4 - roxo em negrito'
     '\033[1;32m',  # 5 - verde em negrito'
     '\033[1;36m',  # 6 - ciano em negrito'
     '\033[m'       # 7 - Apaga
     )


def titulo(msg, cor=0):
    tam = (len(msg) + 4)
    print(c[cor], end='')
    print('-' * tam)
    print(f'| {msg} |')
    print('-' * tam)
    print(c[7], end='')
    sleep(0.8)



def syshelprof(com):
    titulo(f'Acessando o manual do comando \"{com}\"', 4)
    print(c[1], end='')
    help(com)
    print(c[7], end='')
    sleep(1.5)


# Programa Principal
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input("Função ou Biblioteca => "))
    if comando.upper() == 'FIM':
        break
    else:
        syshelprof(comando)
titulo('Até logo', 1)

syspyhelp('Função ou Biblioteca => ')
