# Desafio 091 -> C. um programa onde 4 jogadores jogue um dado e tenha resultados aleatorios.
#                Guarde esses resultados em um dicionario.
#                No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
# (Não tem input)
# o jogadorx tirou y (isso 4x) com sleep se pá
# Ranking dos jogadores:
# z° lugar: jogadorx com y (isso até o 4° lugar)
from random import randint
from time import sleep
from operator import itemgetter
dici = {}
grupo = []
ranking = {}
for j in range(1, 5):
    dici['jogador'] = j
    dici['dados'] = randint(1, 6)
    grupo.append(dici.copy())
print()
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True)
print('ranking: ', ranking)

print('____Jogo dos dados____')
for d in grupo:
    print(f" O {d['jogador']}° jogador lançou {d['dados']}") #se repetir dici['key'], vai printar só o ultimo registro

# Jeito do professor
print('Jeito do professor:\n')
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES  ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.8)
