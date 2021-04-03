from datetime import date
cadastro = {'Nome': input('Digite o nome: ')}
ann = int(input('Data de nascimento: '))
cadastro['Idade'] = idade = date.today().year - ann
tct = input('Possui carteira de trabalho? [S/N]').lower().strip()[0]
if tct in 'n':
    print('Cadastro realizado com sucesso.', '-='*10)
    for k, v in cadastro.items():
        print(f'{k:.<6}: {v}\n')
else:
    cadastro['CTPS'] = input('N° Carteira de Trabalho:')
    cadastro['Ano_de_Contratação'] = int(input('Ano de contratação:'))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (cadastro['Ano_de_Contratação'] - date.today().year))
    print('Cadastro realizado com sucesso.', '-='*10)
    for k, v in cadastro.items():
        if k == 'Ano_de_Contratação':
            print(f'Ano de contratação: {v}')
        else:
            print(f'{k:.<6}: {v}')

# Desafio 092 -> REFAZEEEEEEEEEEEEER
# C. um programa que leia o nome, ano de nascimento e carteira de trabalho
#                e cadastre-os (com idade) em um dicionário se por acaso a carteira for diferente de ZERO,
#                o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
#                além da idade, com quantos anos a pessoa vai se aposentar (aposenta depois de 35 anos de contribuição)
# Nome: Input
# Ano de nascimento: Input
# Carteira de trabalho (0 não tem): Input (se não tem pula contratação e salário)
# Ano de contratação: Input
# Salário: R$Input
