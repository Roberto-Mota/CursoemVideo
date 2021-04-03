# Desafio 019 -> Um professor que sortear um dos seus quatro alunos para apagar
#                o quadro. Faça um programa que ajude ele, lendo o nome deles e
#                escrevendo o nome do escolhido

import random
aluno1 = input('Qual o primeiro aluno? ')
aluno2 = input('Qual o segundo aluno? ')
aluno3 = input('Qual o terceiro aluno? ')
aluno4 = input('Qual o quarto e último aluno? ')
alunoazarado = random.choice((aluno1, aluno2, aluno3, aluno4))
print('Dentre os alunos {}, {}, {} e {}, o escolhido para apagar o quadro foi o(a) {}'.format(aluno1,aluno2,aluno3,aluno4,alunoazarado))
