# Desafio 093 -> Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#               O programa vai ler o nome do jogador e quantas partidas ele jogou.
#               Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#               será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
time = []
registro = {}
listgols = []
registro['jogador'] = str(input('Nome do jogador: '))
registro['partidas'] = partidas = int(input(f'Quantas partidas {registro["jogador"]} jogou? '))
totgols = 0
for p in range(0, partidas):
    gols = (int(input(f'Quantos gols {registro["jogador"]} fez na {p+1} partida?')))
    listgols.append(gols)
    totgols += gols
registro['gols'] = listgols
registro['totgols'] = totgols
time.append(registro.copy())
#output
for t in range(0, len(time)):
    print(f'Cadastro do {t + 1}° jogador')
    print(f'Cod | Nome | Gols | Total de Gols')
    print(f'Cod: {t:<4}|\n'
          f'Nome: {registro["jogador"]}|\n'
          f'Gols: {registro["gols"]}|\n'
          f'Total de gols: {registro["totgols"]}')
for a in range(0, len(listgols)):
    print(f'Na partida {a+1}, {registro["jogador"]} fez {listgols[a]} gols.')

#jeito do professor

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(f'Quantas partidas {jogador["nome"]} jogou? ')
for c in range(0, tot):
    partidas.append(int(input(f'    Quantas gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')