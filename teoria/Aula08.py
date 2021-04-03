import math
numero = int(input('Digite um valor inteiro: '))
raizq = math.sqrt(numero)
print('A raiz quadrada do {} é igual {}'.format(numero, raizq))

numero2 = int(input('Digite um outro valor para arredondar para cima: '))
raizq2 = math.sqrt(numero2)
print('A raiz quadrada de {} é igual a {} (arredondado para cima)'.format(numero2, math.ceil(raizq2)))

# se eu puxar apenas um pedaço, eu nao preciso usar o 'math.algumacoisa', posso usar direto o sqrt

import random
num = random.random()
print(num)
# aqui ele puxa um numero float aleatorio entre 0 e 1
num2 = random.randint(1, 1000)
print(num2)

import emoji
print(emoji.emojize('Python is :thumbs_up:'))

print(emoji.emojize('Python is :thumbsup:', use_aliases=True))

print(emoji.demojize('Python is 👍'))

print(emoji.emojize("Python is fun :red_heart:"))

print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
#red heart, not black heart