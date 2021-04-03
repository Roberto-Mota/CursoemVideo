# Desafio 080 -> C. um programa onde o usuario possa digitar 5 valores numericos e cadastre-os em uma lista
#                   já na posição correta de inserção (sem usar o sort()).
#                   No final, mostre a lista ordenada na tela
lista = []
for v in range(0, 5):
    nums = int(input(f'Digite o {v+1}° número:'))
    if v == 0 or nums > lista[-1]:
        lista.append(nums)
    else:
        pos = 0
        while pos < len(lista):
            if nums <= lista[pos]:
                lista.insert(pos, nums)
                break
            pos += 1

print(lista)


