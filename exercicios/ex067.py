# Desafio 067 -> Faça um programa que mostre a tabuada de vários números, um de cada vez,
#                para cada valor digitado pelo usuário.
#                O programa será interrompido quando o número solicitado for negativo
mult = resul = num = 1
while True:
    num = int(input('Digite o número que deseja visualizar a tabuada: '))
    print('~' * 12)
    mult = 0
    while num >= 0 and mult < 10:
        mult += 1
        resul = num * mult
        print(f'{num:>2} * {mult:>2} = {resul:>2}')
    print('~'*12)
    if num < 0:
        break
