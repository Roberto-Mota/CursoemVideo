# Desafio 085 -> C. um programa onde o usuário possa digitar 7 valores numericos e cadastre-os em uma lista única
#                   que mantenha separados os valores pares e impares (duas listas, uma pra par e outra pra impar).
#                   No final, mostre os valores pares e impares em ordem crescente
lista = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor numérico: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('Os valores pares são:', end=' ')
for pos, valor in enumerate(lista[0]):
    if pos + 1 == len(lista[0]):
        print(f'{valor}.')
    else:
        print(valor, end=', ')
print('Os valores ímpares são:', end=' ')
for pos, valor in enumerate(lista[1]):
    if pos + 1 == len(lista[1]):
        print(f'{valor}.')
    else:
        print(valor, end=', ')
