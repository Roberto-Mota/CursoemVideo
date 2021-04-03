#Desafio 006 -> Crie um algoritmo que leia um número e mostre
#               o seu dobro, triplo e raiz quadrada

numero = float(input('Digite um valor: '))
dobro = numero + numero
triplo = numero * 3
raizq = numero ** 0.5
print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(dobro, triplo, raizq))

# Ou de forma mais eficiente, sem salvar variáveis:

nnumero = float(input('Digite um novo valor: '))
print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(nnumero*2,nnumero*3,nnumero**0.5))