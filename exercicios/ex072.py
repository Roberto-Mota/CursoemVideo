# Desafio 072 -> C. um pro. que tenha uma tupla totalmente preenchida com uma contagem por extenso
#                de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    cont = int(input('Digite um número inteiro entre 0 e 20: '))
    print(f'Você digitou o número {a[cont]}.')
