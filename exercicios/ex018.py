# Desafio 018 -> Faça um programa que leia um ângulo qualquer e mostre na tela
#                o valor do seno, cosseno e tangente desse ângulo
import math
valor = int(input('Digite um ângulo qualquer: '))
print('O Seno do ângulo {}° é {:.2f}, seu Cosseno é {:.2f} e sua Tangente é {:.2f}'.format(valor,math.sin(valor),math.cos(valor),math.tan(valor)))

# Eu fiz errado :c (O valor x de tan, sin e cos tem que ser em "radians"
# com a conversão de math.degrees(x) pra math.radians(x), sendo que o input vinha no valor diferente

valor2 = int(input('Digite outro ângulo que deseja: '))
seno = (math.sin(math.radians(valor2)))
cosseno = (math.cos(math.radians(valor2)))
tangente = (math.tan(math.radians(valor2)))
print('Seno é: {:.2f}\nCosseno é: {:.2f}\nTangente é: {:.2f}'.format(seno,cosseno,tangente))
