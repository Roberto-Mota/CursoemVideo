# Desafio 035 -> Desenvolva um programa que leia o cumprimeto de tres retas
#                e diga ao usuário se ela podem ou não formar um triangulo
#
#                principio matematico
#                Para fazer o cálculo do perímetro de um triângulo basta fazer
#                a soma da medida de todos os lados, a soma dos ângulos internos é sempre 180º
#O triângulo pode ser classificado segundo a medida do seu lado.
#Triângulo escaleno: Todos os lados e ângulos são diferentes.
#Triângulos isósceles: dois lados iguais e os ângulos opostos a esses lados iguais.
#Triângulo equilátero: Todos os lados e ângulos iguais. Concluímos que seus ângulos serão de 60°.
# se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo

from sys import exit

a = float(input('Qual o cumprimento da 1° reta? '))
b = float(input('Qual o cumprimento da 2° reta? '))
c = float(input('Qual o cumprimento da 3° reta? '))
if (a+b) > c and (a+c) > b and (b+c) > a:
    print('Esses seguimentos são capazes de formar um triângulo', end=' ')
    if a != b and a != c and b != c:
        print('e esse triângulo é um Triângulo Escaleno')
    elif a == b and a == c and c == b:
        print('e esse triângulo é um Triângulo Equilátero')
    elif a == b or a == c and b == c:
        print('e esse triângulo é um Triângulo Isósceles')
else:
    print('Esses seguimentos que você apresentou não são capazes de formar um triângulo.')
    exit()













# Olha onde eu fui parar
#cosa = math.degrees(math.acos(((b * b) + (c * c) - (a * a)) / (2 * b * c)))
#cosb = math.degrees(math.acos(((c * c) + (a * a) - (b * b)) / (2 * c * a)))
#cosc = math.degrees(math.acos(((a * a) + (b * b) - (c * c)) / (2 * c * a)))
#if (cosa + cosb + cosc == 180):
#    print('é triangulo porra')
#print(cosa, cosb, cosc)

# copiei da internet fodase mermao
#
#def angle (a, b, c):
#    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
#
#angA = angle(a,b,c)
#angB = angle(b,c,a)
#angC = angle(c,a,b)

#assert angA + angB + angC == 180.0

#print(angA, angB, angC)


