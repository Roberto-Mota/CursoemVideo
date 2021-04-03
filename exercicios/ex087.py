# Desafio 087 -> Aprimore o desafio anterior, mostrando no final:
#                A) A soma de todos os valores pares digitados.
#                B)A soma dos valores da terceira coluna
#                C)O maior valor da segunda coluna

posição = [[], [], []]
linha = 0
coluna = 0
soma_par = 0
soma_coluna3 = 0
maior_coluna2 = 0
for pos, valor in enumerate(range(0, 9)):
    if pos % 3 == 0:
        linha = 0
    linha += 1
    valor = int(input(f'Digite um valor para a Coluna ({coluna+1}), Linha ({linha}):'))
    if valor % 2 == 0:
        soma_par += valor
    if pos == 1:
        maior_coluna2 = valor
    if pos == 4 or pos == 7 and valor > maior_coluna2:
        maior_coluna2 = valor
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
soma_coluna3 = posição[0][2] + posição[1][2] + posição[2][2]

print(f'.____.____.____.\n'
      f'|{posição[0][0]:^4}|{posição[0][1]:^4}|{posição[0][2]:^4}|\n'
      f'|____|____|____|\n'
      f'|{posição[1][0]:^4}|{posição[1][1]:^4}|{posição[1][2]:^4}|\n'
      f'|____|____|____|\n'
      f'|{posição[2][0]:^4}|{posição[2][1]:^4}|{posição[2][2]:^4}|\n'
      f'|____|____|____|\n')
print('-=-'*10)
print(f'A soma de todos os valores pares digitados: {soma_par}.\n'
      f'A soma dos valores da terceira coluna: {soma_coluna3}\n'
      f'O maior valor da segunda coluna: {maior_coluna2}')

#Jeito do professor

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{c},{l}]: '))
print('-=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos pares é: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {scol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')