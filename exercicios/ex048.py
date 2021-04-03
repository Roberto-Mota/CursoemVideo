# Desafio 048 -> Faça um programa que calcule a soma entre os numeros impares que são múltiplos de três
#                  e que se encontrem no intervalo de 1 até 500

bode = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        bode += c
print(bode)

# economizando processador (ñ fica verificando se o numero é par ou não, só pula o par)

porco = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        porco += num
print(porco)
