# Desafio 101 -> Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#                de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO
#                OPCIONAL ou OBRIGATÓRIO nas eleições
idade = 0


def voto():
    from datetime import datetime
    idade = datetime.today().year - nasc
    if idade < 16:
        print('-=' * 13)
        return 'Você ainda não pode votar.'
    elif 16 <= idade < 18 or idade >= 65:
        return 'Seu voto é opcional'
    else:
        return 'Seu voto é obrigatório'


while True:
    nasc = int(input('Digite sua data de nascimento: '))
    print(voto())
