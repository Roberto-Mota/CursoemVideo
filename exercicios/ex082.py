# Desafio 082 -> C. um programa que vai ler varios numeros e colocar em uma lista
#                   Depois disso, crie duas listas extras que vão conter apenas os valores pares e impares digitados
#                   Ao final, mostre o conteudo das tres listas geradas
lista = []
listapar = []
listaimpar = []
cont = 's'
while cont == 's':
    v = int(input('Digite um número: '))
    lista.append(v)
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
    cont = input('Deseja continuar? [S/N]')
    while cont not in 'sn':
        cont = input('Digito inválido, por favor, tente novamente.\n'
                     'Deseja continuar? [S/N]').lower().strip()[0]
print(f'Sua lista inteira é: {lista}.\n'
      f'Os números pares da lista são: {listapar}.\n'
      f'Os números ímpares da lista são: {listaimpar}.')
