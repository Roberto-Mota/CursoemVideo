# Desafio 075 -> C. um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#                A) Quantas vezes apareceu o valor 9
#                B) Em que posição foi digitado o primeiro valor 3
#                C) Quais foram os números pares
cont = reqb = contpar = 0
tupla1 = tuplapar = ()
for vzs in range(0, 4):
    value = int(input(f'Type the {vzs+1}° value: '))
    tupla1 += (value,)
print(f'The typed values were:', end=' ')
for unit in range(0, len(tupla1)):
    print(f'{tupla1[unit]}', end=' ')
for position, unit in enumerate(tupla1):
    if unit % 2 == 0:
        tuplapar += (unit,)
    if unit == 9:
        cont += 1
    if unit == 3:
        if reqb != 0:
            pass
        else:
            reqb = (position) + 1
print(f'\nThe number 9 showed {cont} times')
if reqb != 0:
    print(f'The firt value 3 was typed on the {reqb}° position')
else:
    print("The value 3 wasn't typed in any moment")
print('The even numbers were:', end=' ')
for each in tuplapar:
    print(each, end=' ')

#caralho, era só usar tupla1.index(3) pra achar o primeiro tres e tupla1.count(9) pra achar quantos 9 tinha