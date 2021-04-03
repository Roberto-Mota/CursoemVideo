# Desafio 044 -> Elabore um programa que calcule o valor a ser pago por um produto,
#                   considerando o seu preço normal e condição de pagamento:
#               -  valor do produto
#               -  à vista dinheiro/cheque: 10% de desconto
#               -  à vista no cartão: 5% de desconto
#               -  em até 2x no cartão: preço normal
#               -  3x ou mais no cartão? 20% de juros
from time import sleep
import sys
vpro = float(input('Insira o valor do produto: R$'))
sleep(1)
print('Formas de pagamento:'
      '\nInsira \033[1;32m1\033[m para "À vista no dinheiro/cheque: 10% de desconto"'
      '\nInsira \033[1;32m2\033[m para "À vista no cartão: 5% de desconto"'
      '\nInsira \033[1;32m3\033[m para "Em até 2x no cartão: preço normal"'
      '\nInsira \033[1;32m4\033[m para "3x ou mais no cartão: 20% de juros"')
sleep(1)
fpag = int(input('Insira a forma de pagamento: '))

if fpag == 1:
    print('O produto à vista no dinheiro ou cheque terá um valor de R${:.2f}'.format(vpro * 0.90))
elif fpag == 2:
    print('O produto à vista no cartão terá um valor de R${:.2f}'.format(vpro * 0.95))
elif fpag == 3:
    print('O produto em até 2x no cartão terá parcelas de R${:.2f}, somando um valor de R${:.2f}'.format(vpro / 2, vpro))
elif fpag == 4:
    par = int(input('Em quantas parcelas? '))
    print('O produto em {}x no cartão terá parcelas de R${:.2f} e um valor total de R${:.2f}'.format(par, vpro / par, vpro * 1.20))
else:
    print('\033[1;33mEscolha inválida.')

