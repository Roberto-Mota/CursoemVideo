# Desafio 078 -> C. um programa que leia 5 valores numericos e guarde numa lista
#                   No final, mostre qual foi o menor e maior valor digitado e as suas respectivas posições na lista
lista = []
max = min =  0
#listamm = lista[:]
for v in range(0, 5):
    lista.append(int(input(f'Digite o {v+1}° valor: ')))
#listamm = lista[:]
#listamm.sort()
#max = listamm[-1]
#min = listamm[0]
for pos, v in enumerate(lista):
    if pos == 0:
        max = min = lista[pos]
        minp = pos
        maxp = pos
    else:
        if v > max:
            max = v
        if v < min:
            min = v
print(f'Dentre os valores digitados, o maior foi {max} nas posições', end=' ')
for pos, v in enumerate(lista):
    if max == v:
        print(f'{pos}... ', end='')
print(f'\nE o menor foi {min} nas posições', end=' ')
for pos, v in enumerate(lista):
    if min == v:
        print(f'{pos}...', end=' ')

