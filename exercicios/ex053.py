# Desafio 053 -> Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#                   Ex de palindromo = apos a sopa / arara / a sacada da casa /
#                                       a torre da derrota / o lobo ama o bolo / anotaram a data da maratona



frase = str(input('Escreva um palíndromo: '))
frase.strip().replace(' ', '').lower()
if frase[::-1] == frase:
    print('{} é um palíndromo'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))





# com loop for:

frase2 = str(input('Escreva outra frase: ')).lower().strip().split()
grudada = ''.join(frase2)
inverso = '' #?
print('Gruda:',len(grudada), grudada)
for letra in range(len(grudada) -1, -1, -1):
    inverso = inverso + grudada[letra]
print(grudada, inverso)

#que lógica bizarra