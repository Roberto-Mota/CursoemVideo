#Desafio 011 -> Faça um progrma que leia a largura e a altura de uma parede em metros,
#               calcule a sua área e a quantidade de tinta necessária para pintá-la,
#               sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
mquad = largura*altura
ltinta = mquad/2
print('Você precisará de {} litros de tinta para pintar sua parede, pois ela possui {}m²'.format(ltinta,mquad))