# Desafio 084 -> C. um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#               A) Quantas pessoas foram cadastradas
#               B) Uma listagem com as pessoas mais pesadas. (apenas com o maior peso)
#               C) Uma listagem com as pessoas mais leves. (apenas com o menor numero)
continuar = 's'
contador = maior = menor = 0
ind = []
indg = []
indp = []
dados = []
while continuar == 's':
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    ind.append(dados[:])
    dados.clear()
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    if continuar == 'n':
        break
    while continuar != 's':
        continuar = str(input('Digito inválido, por favor tente novamente.\n'
                         'Deseja continuar? [S/N]')).lower().strip()[0]
        if continuar == 'n':
            break
print(type(ind[0][1]))
for pos, c in enumerate(ind):
    print('o c é: ', c)
    if pos == 0:
        maior = menor = ind[0][1]
        indg.append(ind[pos][0])
        indp.append(ind[pos][0])
    elif ind[pos][1] > maior:
        maior = ind[pos][1]
        indg.clear()
        indg.append(ind[pos][0])
    elif ind[pos][1] == maior:
        indg.append(ind[pos][0])
    elif ind[pos][1] < menor:
        menor = ind[pos][1]
        indp.clear()
        indp.append(ind[pos][0])
    elif ind[pos][1] == menor:
        indp.append(ind[pos][0])
print(f'Tivemos um total de {contador} pessoas cadastradas sendo que:') #ou len(lista)
print(f'O maior peso registrado foi de {maior}Kg, com', end=' ')
if len(indg) == 1:
    print('(o/a)', end=' ')
else:
    print('as pessoas:', end=' ')
for pos, cada in enumerate(indg):
    if pos == len(indg) or len(indg) == 1:
        print(indg[pos], '.')
    elif pos == len(indg) - 1:
        print(indg[pos], end='.')
    else:
        print(indg[pos], end=', ')
print(f'\nO menor peso registrado foi de {menor}Kg, com', end=' ')
if len(indp) == 1:
    print('(o/a)', end=' ')
else:
    print('as pessoas:', end=' ')
for pos, cada in enumerate(indp):
    if pos == len(indp) or len(indp) == 1:
        print(indp[pos], end='.')
    elif pos == len(indp) - 1:
        print(indp[pos], end='.')
    else:
        print(indp[pos], end=', ')
print('\n\/'*20)
