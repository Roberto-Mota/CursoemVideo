# Desafio 020 -> o mesmo professor do desafio anterior quer sortear a ordem
#                de apresentação de trabalhos dos alunos. Faça um programa
#                que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
aluno1 = input('Qual o primeiro aluno? ')
aluno2 = input('Qual o segundo aluno? ')
aluno3 = input('Qual o terceiro aluno? ')
aluno4 = input('Qual o quarto aluno? ')
aluno5 = input('Qual o quinto e último aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
#ordem1 = random.sample(lista, k=5)
random.shuffle(lista)
print('A ordem das apresentações será dada na seguinte sequência:\n{}, {}, {}, {} e {}'.format(lista[0], lista[1], lista[2], lista[3], lista[4]))
# ou printa ordem1 depois de fazer o sample contado

