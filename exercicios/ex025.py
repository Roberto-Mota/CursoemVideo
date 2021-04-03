# Desafio 025 -> Crie um programa que leia o nome de uma pessoa
#                   e diga se ela tem "Silva" no nome
nc = (input('Qual o seu nome? '))
ncs = nc.strip()
print(ncs)

#1° método
ncsf = ncs.find('Silva')
#if ncsf == 1:
#    print('Você é um Silva')
#if ncsf == -1:
#    print('Você não é um Silva')
print('1° método\nCaso aparecer -1, seu nome não possui Silva, caso apareça qualquer outro valor, possui: {}'.format(ncsf))
print('-'*50)
#2° método
inncs = 'Silva' in ncs
print('2° método\nYour name has "Silva" in it: {}'.format(inncs))
print('-'*50)


