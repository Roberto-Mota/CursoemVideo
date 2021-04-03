# Desafio 034 -> Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#                    Para salários superiores a R$1.250,00, calculer um aumento de 10%
#                    Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Qual seu salário? '))
if sal > 1250.00:
    print('Parabéns seu salário, após o aumento, agora será de R${:.2f}, pois o aumento foi de R${:.2f}'
          .format(sal + (sal * 0.10), (sal*0.10)))
else:
    print('Parabéns seu salário, após o aumento, agora será de R${:.2f}, pois o aumento foi de R${:.2f}'
          .format(sal + (sal * 0.15), (sal*0.15)))
