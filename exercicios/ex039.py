# Desafio 039 -> Faça um programa que leia o ano de nascimento de um jovem e informe,
#                  de acordo com sua idade:

#               - Se ele ainda vai se alistar ao serviço militar
#               - Se é a hora de se alistar
#               - Se já passou do tempo de alistamento

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


from datetime import date
ano = int(input('Ano de nascimento: '))
anoa = date.today().year
age = anoa - ano
dife = -(age - 18)
if ano <= 1921:
    print('Você, no mínimo, é veterano da 2° Guerra Mundial.')
if age == 18:
    print('Está em seu período de alistamento, procure o site para mais informações.')
elif age > 18:
    print('Já passou da sua época de se alistar, você está {} ano(s) atrasado, procure se regularizar o quanto antes.'.format(dife))
elif age < 18 and dife == 1:
    print('Ainda falta um ano para você se alistar, procure-nos em {}'.format(anoa+1))
elif age < 18 and dife != 1:
    print('Ainda falta tempo para você se alistar, procure-nos dentro de {} anos'.format(-dife))
print(dife, age)
print('\033[1;32m-=-'*50)
print('\033[1;32mExército brasileiro\033[m, você não tem escolha, é \033[1mobrigatório\033[m.')
print('\033[1;32m-=-'*50)
