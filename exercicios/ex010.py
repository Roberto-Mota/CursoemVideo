#Desafio 010 -> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#               e mostre quantos dólares ela pode comprar (Considere US$1.00 = R$3.27)

money = float(input('Quantos reais você tem em sua carteira? '))
conversao = money/3.27
print('Você pode comprar U${:.2f} com os reais que tem em sua carteira'.format(conversao))