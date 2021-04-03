# Desafio 031 -> Desenvolva um programa que pergunte a distância de uma viagem em Km.
#                Calcule o preço da passagem do ônibus, cobrando R$0,50 po km para viagens de até 200km
#                                                              e R$0.45 para viagens mais longas

dist = int(input("De quantos Km's será sua viagem de ônibus? "))
if dist >= 200:
    print('Sua viagem custará R${:.2f}'.format(dist * 0.45))
else:
    print('Sua viagem custará R${:.2f}'.format(dist * 0.50))

# if simplicado
# preco = dist * 0.45 if dist >= 200 else dist * 0.50