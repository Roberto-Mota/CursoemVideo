# Desafio 057 -> Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'
#                Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Qual seu sexo? [M/F]').strip().lower()[0] #[0] pega só a primeira letra, dica boa
if sexo == 'm' or sexo == 'f':
    print('Obrigado.')
while sexo != 'm' and sexo != 'f':
    print('"{}" não é uma resposta válida, por favor, tente novamente.'.format(sexo))
    sexo = input('Qual seu sexo? [M/F]').strip().lower()
    if sexo == 'm' or sexo == 'f':
        print('Obrigado.')

