# Desafio 081 -> C. um programa que vai ler varios numeros e colocar em uma lista
#                   Depois disso, mostrar:
#                   A)quantos numeros foram digitados
#                   B)a lista de valores, ordenada de forma decrescente.
#                   C)Se o valor 5 foi digitado e está ou não na lista
lista = []
reqa = reqb = reqc = 0
cont = 's'
while cont == 's':
    lista.append(int(input('Digite um número: ')))
    cont = input('Deseja continuar? [S/N]')
    while cont not in 'sn':
        cont = input('Digito inválido, por favor, tente novamente.\n'
                     'Deseja continuar? [S/N]')

print(f'{len(lista)} números foram digitados', end=' ')
lista.sort(reverse=True)
print(f', sendo que a lista dos valores de forma descrescente é: {lista}')

if 5 in lista:
    print(f'E o valor 5 foi digitado.')
else:
    print(f'E o valor 5 não foi inserido na lista.')
