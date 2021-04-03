# Desafio 062 -> Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais
#                alguns termos (quantos o usuario quiser)
#                O programa deve encerrar quando o usuário disser que quer mostrar 0 termos

ter1 = int(input('Digite o valor do termo: '))
raz = int(input('Digite o valor da razão: '))
dec = ter1 + (10 - 1) * raz
#for unid in range(ter1, dec + raz, raz):
#    print('{}'.format(unid), end=' -> ')

resul = 0
vzs = 1
cont = 1
while vzs != 0:
    cont = 1
    vzs = int(input('Digite a quantidade de termos que quer ver (0 para parar): '))
    while cont < vzs:
        if cont == 1:
            print(ter1, '-> ', end='')
        resul = ter1 + raz
        ter1 = resul
        cont += 1
        print(resul, '-> ', end='')
print('P.A completa.')

#essa porra ficou muito bootleg, mas acho que preferi com for