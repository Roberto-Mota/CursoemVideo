# Desafio 036 -> Escreva um programa para aprovar o empréstimo bancário para
#                   a compra de uma casa. O programa vai perguntar o valor da
#                   casa, o salário do comprador e em quantos anos ele vai pagar.

#                Calcular o valor da prestação mensal, sabendo que ela não pode
#                exceder 30% do salário ou então o empréstimo será negado

valor = int(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
age = int(input('Em quantos anos você pretende pagar? '))
emp = valor / (age * 12)
if emp > (sal*0.30):
    print('Seu empréstimo foi negado pois as parcelas de R${:.2f} não foram aceitas devido ao seu salário'.format(emp))
elif emp <= (sal*0.30):
    print('Seu empréstimo foi aceito e terá uma parcela de R${:.2f}, durante o período de {} anos'.format(emp, age))
