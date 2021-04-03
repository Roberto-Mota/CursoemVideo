qtda = 0
turma = []
aluno = []
notas = []
print(dir(turma))
while True:
    aluno.append(input('Nome do aluno: '))
    notas.append(float(input('Nota no 1° bimestre: ')))
    notas.append(float(input('Nota no 2° bimestre: ')))
    aluno.append(notas[:])
    aluno.append((notas[0] + notas[1]) / 2)
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    qtda += 1
    print(f'Turma: {turma}')
    continuar = input('Deseja continuar? [S/N]').lower().strip()[0]
    if continuar == 'n':
        break
    elif continuar not in 'ns':
        continuar = input('Digito inválido, por favor tente novamente\n'
                          'Deseja continuar? [S/N]').lower().strip()[0]
print('.____________________.\n|N°| Aluno    |Média |')
for i, a in enumerate(turma):
    print(f'|{i+1} |{turma[i][0]:<10}|{turma[i][2]:<.2f}  |')
print('|____________________|')
while True:
    indice = int(input('Você deseja ver a nota de que aluno? (999 para encerrar)'))
    if indice > len(turma) and indice != 999:
        indice = int(input('Digito inválido. Por favor tente novamente.'
                           'Você deseja ver a nota de que aluno? (999 para encerrar)'))
    if indice == 999:
        break
    print(f'As notas do(a) {turma[indice-1][0]} são {turma[indice-1][1]:}')

# Desafio 088 -> C. um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista oomposta.
#                No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
#                as notas de cada aluno individualmente
# Jeito do professor
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=')
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('Programa finalizado')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
