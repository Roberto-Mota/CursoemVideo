# Desafio 056 -> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre
#                A media de idade do grupo.
#                Qual o nome do homem mais velho.
#                Quantas mulheres têm menos de 20 anos.
somid = 0
m20 = 0
ageh = 0
nomehv = ''
for registro in range(1, 5):
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    somid += age
    sex = int(input('Sexo (1F) e 2(M): '))
    if registro == 1 and sex == 2:
        ageh = age
        nomehv = name
    if sex == 2 and age > ageh: #### Qual o nome do homem mais velho.
        ageh = age
        nomehv = name
    if sex == 1 and age < 20: ## Quantas mulheres tem menos de 20 anos.
        m20 += 1

print('A media de idade do grupo é {}.'.format(somid/4))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomehv, ageh))
if m20 > 2:
    print('{} mulheres têm menos de 20 anos.'.format(m20))
else:
    print('{} mulher têm menos de 20 anos.'.format(m20))
