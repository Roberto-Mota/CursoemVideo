#Desafio 014 -> Escreva um programa que converta uma temperatura em °C para °F
c = float(input('Qual a temperatura em Celsius que você deseja converter? '))
f = (c * 9/5) + 32
print("{:.2f}°C equivale a {:.2f}°F".format(c, f))
