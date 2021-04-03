# Desafio 064 -> Faça um programa que leia vários números int pelo teclado.
#                o programa só vai parar quando o usuário digitar 999
#                No final, mostre quantos números foram digitados e qual foi a soma entre eles
#                (desconsiderando o flag)
vzs = 0
entrada = 0
total = 0
# ou vzs = entrada = total = 0
while entrada != 999:
    entrada = float(input('Digite o {}° número: '.format(vzs+1)))
    if entrada == 999:
        pass
    else:
        vzs += 1
        total = entrada + total
print('Você digitou {} números e a soma de todos eles equivale à {}.'.format(vzs, total))
