sexo = str(input('Qual seu sexo? [M/F]')).lower().strip()[0]
while sexo not in 'fm':
    sexo = input('Digito inválido, por favor digite F (feminino) ou M (masculino):').lower().strip()[0]
if sexo == 'm':
    print('Seja Bem vindo!')
elif sexo == 'f':
    print('Seja Bem vinda!')
else:
    print('Tá, né.')

def linhas(nome):
    print('-=' * 10)
    print(f' Seja bem vindo {nome}')
    print('-=' * 10)


nome = input('Qual o seu nome? ')
linhas(nome)