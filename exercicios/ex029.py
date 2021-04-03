# Desafio 029 -> Escreva um programa que leia a velocidade de um carro.
#                   Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#                   A multa vai custar R$7,00 por cada Km acima do limite

vel = (float(input('A quantos KM/h você estava ao passar no pardal? ')))
if vel > 80:
    #multa = (vel - 80) * 7
    print('Vacilou em? Agora vai ter que pagar uma multa de R${:.2f}'.format((vel - 80) * 7))
if vel == 80:
    print('O limite da via é justamente 80 KM/h, quase em?')
else:
    print('Você não tomou multa, mas fica esperto na próxima!')