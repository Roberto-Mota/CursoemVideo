# Desafio 076 -> C. um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#                No final mostre uma listagem de preços, organizando os dados em forma tabular
# -----------------
# Lista de preços
# _________________------
# Produto1......R$  1.90
# prod2.........R$ 14.00
# ------------------------
tpp = tprod = ()
produto = 0
continuar = 's'
while continuar == 's':
    prod = input('Digite o \033[1mnome\033[m do produto: ')
    price = float(input('Digite o \033[1mpreço\033[m do produto: '))
    tpp += (prod, price,)
    produto += 1
    continuar = input('Deseja continuar? [S/N]').strip().lower()[0]
    if continuar == 'n':
        break
    while continuar != 's' and continuar != 'n':
        continuar = input('Digito inválido, por favor tente novamente.\nDeseja continuar? [S/N]').strip().lower()[0]
print(tpp)
print('{:=^40}'.format('Nota Fiscal'))
for unidade in range(0, len(tpp), 2):
    print('{:.<30}R${:.2f}'.format(tpp[unidade], tpp[unidade+1]))
print('='*51)
