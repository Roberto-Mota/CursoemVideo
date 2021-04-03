# Desafio 079 -> C. um programa onde o usuario possa digitar valrios valores numéricos e cadastre-os em uma lista.
#                   Caso o número já exista lá dentro, ele não será adicionado.
#                   No final, serão exibidos todos os valores únicos digitados, em ordem crescente
lista = []
cont = 's'
while cont == 's':
    entrada = int(input('Digite um número: '))
    if entrada in lista:
        print('Valor já se encontra na lista.')
    else:
        lista.append(entrada)
    cont = input('Deseja continuar? [S/N]').lower().strip()[0]
    while cont not in 'sn':
        cont = input('Digito inválido, tente novamente.\nDeseja continuar? [S/N]').lower().strip()[0]
    if cont == 'n':
        break
lista.sort()
print(f'A lista em ordem crescente dos valores que você digitou é: {lista}')
