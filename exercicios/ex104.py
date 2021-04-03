# Desafio 104 -> Crie um programa que tenha uma função chamada leiaint(), que vai funcionar de forma semelhante
#                a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#                ex: n = leiaint('Digite um número: ')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!\033[m Digite um número inteiro válido.')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


val = leiaint('Digite um número: ')
