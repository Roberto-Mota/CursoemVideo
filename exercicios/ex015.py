#Desafio 014 -> Escreva um programa que pergunte a quantidade de Km percorridos por
#               um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
#               preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmper = float(input('Quantos Km você andou com o carro? '))
qdias = int(input('Por quantos dias você usou o carro? '))
pkm = kmper*0.15
pqdias = qdias*60
pfinal = pkm+pqdias
print('O preço que você deverá pagar pelo aluguel do carro é de R${:.2f}'.format(pfinal))

# Forma com menos variável

print('-'*50)
kmper = float(input('Quantos Km você andou com o carro? '))
qdias = int(input('Por quantos dias você usou o carro? '))
print('O preço que você deverá pagar pelo aluguel do carro é de R${:.2f}'.format((kmper*0.15)+(qdias*60)))