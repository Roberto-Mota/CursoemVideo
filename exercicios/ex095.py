# Desafio 095 -> Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.
#
# Nome do grupo: Input
# Quantas partidas (nome) jogou? Input
# Quantos gols na partida (input) ? (Isso X vzs por partida)
# Quer continuar? [S/N]
#
# gols:[lista]
# Output:
# Um tabela de Cod / Nome / Gols / Total de Gols
# depois
# Mostrar dados de qual jogador? Input
time = []
registro = {}
listgols = []
continuar = 's'
while continuar == 's':
    registro['jogador'] = debug = str(input('Nome do jogador: '))
    if debug == '000':
        break
    registro['partidas'] = partidas = int(input(f'Quantas partidas {registro["jogador"]} jogou? '))
    totgols = 0
    for p in range(0, partidas):
        gols = (int(input(f'Quantos gols {registro["jogador"]} fez na {p+1} partida?')))
        listgols.append(gols)
        totgols += gols
    registro['gols'] = listgols[:]
    registro['totgols'] = totgols
    time.append(registro.copy())
    listgols.clear()
    totgols = 0
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar not in 'sn':
        continuar = str(input('Digito inválido, tente novamente.\nDeseja continuar? [S/N]'))
    if continuar == 'n':
        break
#output
continuar = 's'
print(f'Cadastro dos {len(time)} jogadores')
print(f'Cod | Nome | Gols | Total de Gols')
hx = 1
for r in time:
    print(f'{hx:<4}|{r["jogador"]}|{r["gols"]}|{r["totgols"]}')
    hx += 1
while True:
    if continuar == 'n':
        break
    if debug == '000':
        break
    var = int(input('Mostrar dados de qual jogador?'))
    print(f'Aproveitamendo do jogador:')
    registro = time[var - 1]
    listgols = registro["gols"]
    for k in registro.keys():
        if k == 'gols':
            for g in range(0, len(registro['gols'])):
                print(f'    => Na partida {g + 1}, {registro["jogador"]} fez {listgols[g]} gols.')
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
        if continuar in 'sn':
            break
        print('Erro, digito inválido, por favor digite S ou N')

# jeito do professor
time2 = list()
jogador2 = dict()
partidas2 = list()
while True:
    jogador2.clear()
    jogador2['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador2["nome"]} jogou? '))
    partidas2.clear()
    for c in range(0, tot):
        partidas2.append(int(input(f'    Quantas gols na partida {c+1}?')))
    jogador2['gols'] = partidas2[:]
    jogador2['total'] = sum(partidas2)
    time.append(jogador2.copy)
    while True:
        resp = str(input('Que continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador2.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time2):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
#copia nao terminada mas foda-se