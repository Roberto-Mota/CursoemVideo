# Desafio 059 -> Crie um programa que leia dois valores e mostre um menu na tela:
#                [1]somar
#                [2]multiplixar
#                [3]maior
#                [4]novos números
#                [5]sair do programa
#                Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
calc = '4'
while calc in '4':
    print('-=-'*5, 'Calculadora Básica', '-=-'*5)
    print(' '*15, 'Digite dois valores', ' '*5)
    num1 = float(input('1° valor: '))
    num2 = float(input('2° Valor: '))
    etapa2 = '00'
    while etapa2 == '00':
        etapa2 = '01'
        sleep(1.5)
        print('-=-'*20,
              '\n[\033[1;32m1\033[m]somar\n'
              '[\033[1;32m2\033[m]multiplicar\n'
              '[\033[1;32m3\033[m]maior\n'
              '[\033[1;32m4\033[m]novos números\n'
              '[\033[1;32m5\033[m]sair do programa')
        calc = input('Digite a operação que deseja fazer com os valores: ')
        if calc == '1':
            res = num1 + num2
            print('{} + {} = {}'.format(num1, num2, res))
            etapa2 = '00'
        elif calc == '2':
            res = num1 * num2
            print('{} x {} = {}'.format(num1, num2, res))
            etapa2 = '00'
        elif calc == '3':
            if num1 > num2:
                print('{} é maior que {}.'.format(num1, num2))
            elif num1 < num2:
                print('{} é maior que {}.'.format(num2, num1))
            else:
                (print('Os valores são iguais.'))
            etapa2 = '00'
        elif calc == '4':
            pass
        elif calc == '5':
            opc5 = ''
            while opc5 != 's' and opc5 != 'n':
                opc5 = input('Tem certeza que deseja sair do programa? [S/N]').strip().lower()[0]
                if opc5 == 's':
                    print('-=-'*5, 'EXIT', '-=-'*5)
                    break
                elif opc5 == 'n':
                    etapa2 = '00'
                else:
                    print('Digito inválido, por favor tente novamente')
        else:
            print('Digito inválido, por favor tente novamente')
            etapa2 = '00'

