#Desafio 008 -> Escreva um programa que leia um valor em metros
#               e o exiba convertido em centímetros e milímetros

metro = float(input('Qual a metragem que deve ser convertida?'))
centimetro = metro * 100
milimetro = centimetro * 10
print('O valor convertido em centímetros é {} \nJá em milímetros é {}'.format(centimetro, milimetro))

# Ou sem variável