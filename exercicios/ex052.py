# Desafio 052 -> Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

# sem 'for', só consegui assim, faltou um pouco de conhecimento em for

unid = int(input('Digite um valor: '))
if unid == 2 or unid == 3 or unid == 5 or unid == 7:
    print('{} é numero primo.'.format(unid))
elif unid % 3 == 0 or unid % 2 == 0 or unid % 5 == 0 or unid % 7 == 0:
    print('{} não é número primo. elif'.format(unid))
else:
    print('{} é número primo. else'.format(unid))

numin = int(input('Digite outro valor: '))
porco = 0
for unidade in range(1, numin + 1):
    if numin % unidade == 0:
        porco += 1
if porco == 2:
    print('{} é primo'.format(numin))
else:
    print('{} não é primo, pois ele é divisível por {} números'.format(numin, porco))