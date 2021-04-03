#Desafio 013 -> Faça um algortimo que leia um salário de um funcionário e mostre
#               seu novo salário, com 15% de aumento

salario = int(input('Qual seu salário? R$:'))
umparaumento = salario/100
nsalario = (umparaumento*15) + salario
print('Parabéns, com um aumento de 15% do seu salário, agora você recebe R${:.2f}'.format(nsalario))

#Outra forma, com menos variáveis

sal = float(input('Qual seu atual salário? '))
print('Parabéns, com um aumento de 15% do seu salário, agora você recebe R${:.2f}'.format(sal*1.15))