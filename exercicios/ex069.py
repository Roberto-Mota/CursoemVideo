# Desafio 069 -> Faça um pgr. que leia a idade e o sexo de varias pessoas. a cada pessoa cadastarada
#                o programa, o programa deverá perguntar se o usuário quer continuar. no final mostre:
#                A) Quantas pessoas tem mais de 18 anos
#                B) Quantos homens foram cadastrados
#                C) Quantas mulheres têm menos de 20 anos
reqa = reqb = reqc = contseks = 0
continuar = 's'
while continuar == 's':
    idade = int(input('Digite a idade da pessoa cadastrada: '))
    if idade >= 18:
        reqa += 1
    sexo = str(input('Digite o sexo da pessoa cadastrada [F/M]: ')).lower().strip()[0]
    while sexo not in 'mf':
        sexo = str(input('Informação inválida, por favor tente novamente\n'
                         'Digite o sexo da pessoa cadastrada [F/M]: ')).lower().strip()[0]
    if sexo == 'm':
        reqb += 1
    if sexo == 'f' and idade < 20:
        reqc += 1
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Informação inválida, por favor tente novamente.\n'
                              'Deseja continuar? [S/N] ')).lower().strip()[0]
print(f'Analisando os dados das pessoas cadastradas podemos concluir que:\n'
      f'Um total de {reqa} pessoa(s) tem mais de 18 anos\n'
      f'{reqb} homens foram cadastrados ao todo\n'
      f'{reqc} mulheres têm menos de 20 anos')
