# Desafio 040 -> Crie um programa que leia duas notas de um aluno e calculer sua média,
# mostrando uma msg no final, de acordo com a média atingida:

#               -  abaixo de 5.0 = REPROVADO
#               -  média entre 5.0 e 6.9 = RECUPERAÇÃO
#               -  média 7.0 ou superior = APROVADO

nota1 = float(input('Qual sua nota no primeiro bimestre? '))
nota2 = float(input('Qual sua nota no segundo bimestre? '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média: {} \033[1;31mREPROVADO'.format(media))
if 5.0 <= media <= 6.9:
    print('Média: {} \033[1;33mRECUPERAÇÃO'.format(media))
if media > 6.9:
    print('Média: {} \033[1;32mAPROVADO'.format(media))
