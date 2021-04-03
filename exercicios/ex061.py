# Desafio 061 -> Refaça o desafio 051 lendo o primeiro termo e a razão de uma PA,
#                mostrando os 10 primeiros termos da PA usando While
print('Desafio 61')
#acho que nao entendi o que pediu no enunciado mas fiz uma PA que inclusive deixa medir o segundo termo

#num1 = int(input('Digite o valor do primeiro termo: '))
#num2 = int(input('Digite o valor do segundo termo: '))
#num3 = int(input('Digite o valor da constante: '))
#for pa in range(num1, num2, num3):
#    print('{}'.format(pa), end=' -> ')
#print('P.A completa.')

# confome o desafio feito

ter1 = int(input('Digite o valor do termo: '))
raz = int(input('Digite o valor da razão: '))
#dec = ter1 + (10 - 1) * raz
#for unid in range(ter1, dec + raz, raz):
#    print('{}'.format(unid), end=' -> ')
resul = 0
vzs = 1
cont = 1
while vzs != 0:
    cont = 1
    vzs = int(input('Digite a quantidade de vezes que quer (0 para parar): '))
    while cont < vzs:
        if cont == 1:
            print(ter1, '-> ', end='')
        resul = ter1 + raz
        ter1 = resul
        cont += 1
        print(resul, '-> ', end='')

print('P.A completa.')