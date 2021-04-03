# Desafio 050 -> desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#                   Se o valor digitado for impar, desconsidere-o
porco = 0
for valor in range(1, 7):
    num = int(input('Digite {}° valor: '.format(valor)))
    if num % 2 == 0:
        porco = porco + num  # ou porco += num
print('A soma apenas dos números pares é: {}'.format(porco))
