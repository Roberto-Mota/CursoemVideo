# Desafio 071 -> Faça um pgr. que simule o funcionamento de um caixa eletrônico.
#                No início, pergunte ao usuário qual será o valor a ser sacado (num int)
#                E o programa vai informar quantas cédulas de cada valor serão entregues
#                OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
print('º°º'*5, 'Banco Roseark', '°º°'*5)
saque = 1
nota1 = nota10 = nota20 = nota50 = 0
saque = int(input('Digite o valor que deseja sacar: R$'))
saquei = saque
while saque != -1:
    if saque == 0:
        break
    while saque >= 50:
        nota50 += 1
        saque -= 50
    while saque >= 20:
        nota20 += 1
        saque -= 20
    while saque >= 10:
        nota10 += 1
        saque -= 10
    while saque < 10 and saque != 0:
        nota1 += 1
        saque -= 1
    if saque <= 0:
        break
print('Você solicitou um saque de R${}. Você receberá {} cédula(s) de R$50, {} de R$20, {} de R$10 e {} de R$1.'.format(saquei, nota50, nota20, nota10, nota1))
