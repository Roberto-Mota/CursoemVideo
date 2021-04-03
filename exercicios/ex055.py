# Desafio 055 -> Faça um programa que leia o peso de cinco pessoas.
#                 n No final, mostre qual foi o maior e o menor peso lidos
lista = []
for pes in range(1, 6, 1):
    peso = float(input('Digite seu peso: '))
    lista.append(peso)
ordem = sorted(lista)
print('A pessoa mais leve tem {}Kg, enquanto a mais pesada tem {}Kg'.format(ordem[0], ordem[-1]))
