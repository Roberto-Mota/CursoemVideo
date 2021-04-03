#Desafio 012 -> Faça um algoritmo que leia o preço de um produto
#               e mostre seu novo preço,com 5% de desconto
preco = float(input('Quanto custa o produto?'))
desconto = preco / 20
pdesconto = preco - desconto
print('Com um desconto de 5%, o novo valor do produto passa a ser R${}'.format(pdesconto))

#Outra forma

preco2 = float(input('Quanto custa o produto?'))
print('Com um desconto de 5%, o novo valor do produto passa a ser R${}'.format(preco2*0.95))