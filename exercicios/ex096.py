# Desafio 096 -> C. um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
#                   retangular (largura e comprimento) e mostre a área do terreno

def área(a, b):
    c = a * b
    print(f'-' * 31)
    print(f'A área de {a} x {b} é igual a {c}²')
    print(f'-' * 31)


while True:
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    área(largura, comprimento)
