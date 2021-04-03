# int= () 7, -7, -4, 0, 9875, 42
# float= () 4.2, 0.076, -15.223, 7.0
# bool= () True, False (com o Caps na primeira letra)
# str= () 'Olá', "7.5", ''
#print('Página 01')
#n1 = int(input('Vamos fazer uma soma, qual o primeiro valor?'))
#n2 = int(input('Qual o segundo valor?'))
#soma = n1+n2
#print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
#print(type(n1))
print('#========================================================================================#')
#========================================================================================#
print('Página 02')

# Desafio 04 -> Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ela
# == sinal de igualade != sinal de diferença

# print(n.isnumeric()) serve para mostrar se o input é algo,
# esse exemplo é pra saber se é numérico, existem vários 'is'

variavel = (input('Digite algo:'))
print(type(variavel))
print("It's a numeric?", variavel.isnumeric())
print("It's an alpha numeric?", variavel.isalnum())
print("It's an alpha?", variavel.isalpha())
print("It's a ascii?", variavel.isascii())
print("It's a digit?", variavel.isdigit())
print("It's a decimal?", variavel.isdecimal())
print("It's a identifier", variavel.isidentifier())
print("It's a lower?", variavel.islower())
print("It's a printable?", variavel.isprintable())
print("It's a space?", variavel.isspace())
print("It's a title?", variavel.istitle())
print("It's upper?", variavel.isupper())


print('#========================================================================================#')
#========================================================================================#
print('Página 03')

# Fase 07 (Operações Aritméticas) ->
#
# (== dois iguais serve para testar se uma coisa é igual a outra)

# 5+2==7
# 5-2==3
# 5*2==10
# 5/2==2.5
# 5**2==25(cinco ao quadrado)
# 5//2==2 (divisão inteira sem usar virgula quebrada na matematica normal lá que a gente faz)
# 5%2==1 (resto da divisão de cima)

# Ordem de precedência (quem vem primeiro):
# ()
# **
# * / // %
# + -
#
# Pra quebrar linha no print usa /n e pra não quebrar usa end=' '
# (pode ser, no lugar de vazio, qualquer sinal que queria que apareça no meio)
#
#========================================================================================#
print('Aula 08')
#Aula 8 -> Utilizando módulos

#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos
# import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar
# vários recursos adicionais nos seus programas utilizando módulos built-in e módulos
# externos, oferecidos no Pypi.

#   pra puxar alguma coisa de biblioteca/módulo -> import'grupo'
#   pra importar apenas alguma coisa apenas, sendo mais específico -> from'grupo'import'algumacoisa'

# math é um biblioteca (module) de matemática
# ceil -> funcionalidade que arredonda pra cima
# floor -> funcionalidade que arredonda pra baixo
# trunc ->
# pow ->
# sqrt ->
# factorial ->
# importmath
#importação otimizada -> from math import sqrt,ceil