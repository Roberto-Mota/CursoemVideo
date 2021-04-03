aluno0 = {'Nome': str(input('Digite o nome do aluno: ')).strip().capitalize()}
nota1 = float(input(f'Digite a nota do {aluno0["Nome"]} no 1° bimestre: '))
nota2 = float(input(f'Digite a nota do {aluno0["Nome"]} no 2° bimestre: '))
aluno0['Media'] = (nota1 + nota2) / 2
if aluno0['Media'] < 5:
    aluno0['Situação'] = 'Reprovado'
elif 5 <= aluno0['Media'] < 6:
    aluno0['Situação'] = 'Recuperação'
else:
    aluno0['Situação'] = 'Aprovado'
for k, v in aluno0.items():
    print(f'{k}: {v}')

    # Jeito do professor é praticamente a mesma coisa
# Desafio 090 -> C. um programa que leia nome e média de um aluno,
#               guardando também a situação (reprovado ou aprovado) em um dicionário.
#               No final mostre o conteúdo da estrutura na tela
# Nome: input
# Média de (Nome): input (vamos fazer com 6)
# output:
# Nome:
# Média:
# Situação: reprovado (ou) aprovado