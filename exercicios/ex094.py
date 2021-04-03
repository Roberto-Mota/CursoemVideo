continuar = 's'
sid = mid = 0
grupo = []
grupof = []
grupos = []
registro = {}
while continuar == 's':
    registro['nome'] = input('Nome: ')
    registro['sexo'] = input('Sexo: ').lower().strip()[0]
    registro['idade'] = idade = int(input('Idade: '))
    sid += idade
    grupo.append(registro.copy())
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Digito inválido, por favor tente novamente.\nDeseja continuar? [S/N]'))
    if continuar == 'n':
        break
registro.clear()
print(f'Um total de {len(grupo)} pessoas foram registradas.')
reqb = mid = sid / len(grupo)
print(f'A média de idade entre os cadastrados é de {reqb:<.2f} anos')
for r in grupo:
    if r['sexo'] == 'f':
        grupof.append(r['nome'])
    if r['idade'] > mid:
        grupos.append(r['nome'])
print('\nLista de pessoas registradas do sexo feminino:')
for u in grupof:
    print(u, end=' ')
print()
print('\nLista de pessoas registradas com idade acima da média:')
for u in grupos:
    print(u, end=' ')

#Jeito do professor
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
# Desafio 094 -> Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#           A) Quantas pessoas cadastradas.
#           B) A média de idade.
#           C) Uma lista com mulheres.
#           D) Uma lista com idade acima da média.

# Nome: Input
# Sexo [M/F]: Input
# Idade: Input
# Quer continuar? [S/N]
# output:
# O grupo tem x pessoas
# a média de idade é de w anos.
# As mulheres cadastradas foram: Inputs
# Lista das pessoas que estão acima da média: