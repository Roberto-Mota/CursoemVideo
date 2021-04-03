# Desafio 017 -> Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente
#                 de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
# o quadrado da hipotenusa é igual a soma dos quadrados dos catetos

#h²=(c²)+(c²)

import math
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hip = math.hypot(co, ca)
hip2 = math.sqrt(co*co + ca*ca)
print('{:.2f} ou {:.2f}'.format(hip, hip2))