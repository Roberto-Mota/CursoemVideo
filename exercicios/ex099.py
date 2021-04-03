# Desafio 099 -> Crie um programa que tenha uma funcção maior(),
#               que receba vários parâmetros com valores inteiros.
#               Seu programa tem que analisar todos os valores e dizer qual deles é maior


def maior(* num):
    maior = menor = 0
    for l in num:
        for i, u in enumerate(l):
            if i == 0:
                maior = u
                menor = u
            if u > maior:
                maior = u
            if u < menor:
                menor = u
    print(f'O menor falor da lista é {menor} e o maior é {maior}')


cont = 0
lista = []
continuar = 's'
while continuar == 's':
    lista.append(int(input('Digite um número: ')))
    cont += 1
    if cont == 5:
        continuar = input('Deseja continuar? [S/N]').lower().strip()[0]
        while continuar not in 'sn':
            continuar = input('Erro. Deseja continuar? [S/N]').lower().strip()[0]
        if continuar == 'n':
            break
        if continuar == 's':
            cont = 0
maior(lista)

#jeito do professor


#def maior2():

