# Desafio 041 -> A confederação nacional de natação precisa de um programa que
#                   leia o ano de nasciemnto de um atleta
#                   e mostre sua categoria, de acordo com a idade

#               - Até 9 anos: mirim
#               - Até 14 anos: infantil
#               - Até 19 anos: junior
#               - Até 25 anos: sênior
#               - Acima: Master

from datetime import date
anoa = date.today().year
anou = int(input('Em que ano você nasceu? '))
age = anoa - anou
print('Com a idade de {} anos do inscrito, sua'.format(age), end=' ')
if age <= 9:
    print('categoria será \033[1;31mMirim')
elif age <= 14:
    print('categoria será \033[1;32mInfantil')
elif age <= 19:
    print('categoria será \033[1;33mJunior')
elif age <= 25:
    print('categoria será \033[1;34mSênior')
else:
    print('Categoria será \033[1;35mMaster')