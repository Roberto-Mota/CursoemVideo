# Desafio 103 -> Crie um programa que tenha uma função chamada ficha(), que receba dois parametros
#                opcionais: o nome de um jogador e quantos gols ele marcou.
#                O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
#                sido informado corretamente.


def ficha(nome='unknown', gols=0):
    if gols == '':
        gols = 0
    if nome == '':
        nome = 'unknown'
    print(f'O {nome} fez {gols} gols.')


nome = str(input('Nome do jogador: '))
gols = str(input(f'Quantos gols {nome} fez?'))
ficha(nome, gols)

#Ficou bootleg pracarai
#Jeito do professor:


def ficha2(jog='unknown', gol=0):
    print('O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input(f'Quantos gols {n} fez?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)