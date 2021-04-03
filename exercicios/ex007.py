#Desafio 007 -> Desenvolva um programa que leia as duas notas de um aluno,
#               calcule e mostre sua média

nota1 = float(input('Quanto você tirou no primeiro bimestre? '))
nota2 = float(input('Quanto você tirou no segundo bimestre? '))
media12 = (nota1 + nota2)/2
print('Sua média entre as duas notas é de {}'.format(media12))

# Ou de forma mais eficiente, sem salvar variáveis:

nota3 = float(input('Quanto você tirou no terceiro bimestre? '))
nota4 = float(input('Quanto você tirou no quarto bimestre? '))
print('Sua média entre as duas notas é de {}'.format((nota3 + nota4)/2))

print('Sua média final na matéria é {}'.format((media12+nota3+nota4)/3))