# Desafio 086 -> C. um programa que crie uma matriz de dimensão 3x3 (jogo da velha)
#                e preencha com valores lidos pelo teclado.
#                No final, mostre a matriz na tela, com a formatação correta
posição = [[], [], []]
linha = 0
coluna = 0
for pos, valor in enumerate(range(0, 9)):
    if pos % 3 == 0:
        linha = 0
    linha += 1
    valor = int(input(f'Digite um valor para a Coluna ({coluna+1}), Linha ({linha}):'))
    if 0 <= pos <= 2:
        posição[0].append(valor)
        if pos == 2:
            coluna = 1
    elif 3 <= pos <= 5:
        posição[1].append(valor)
        if pos == 5:
            coluna = 2
    elif 6 <= pos <= 8:
        posição[2].append(valor)

print(f'.____.____.____.\n'
      f'|{posição[0][0]:^4}|{posição[0][1]:^4}|{posição[0][2]:^4}|\n'
      f'|____|____|____|\n'
      f'|{posição[1][0]:^4}|{posição[1][1]:^4}|{posição[1][2]:^4}|\n'
      f'|____|____|____|\n'
      f'|{posição[2][0]:^4}|{posição[2][1]:^4}|{posição[2][2]:^4}|\n'
      f'|____|____|____|\n')

print('-=-'*10)
#Jeito do professor

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{c},{l}]: '))
print('-=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
