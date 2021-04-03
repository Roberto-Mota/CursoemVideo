# Desafio 046 -> Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#                   indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
cont = 10
for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
print('FOGOS \033[1;31mPEW \033[1;32mPEW \033[1;33mPEW \033[1;34mPEW \033[1;35mPEW \033[1;36mPEW \033[1;37mPEW'
      ' \033[1;38mPEW \033[1;39mPEW \033[1;36mPEW \033[1;34mPEW \033[1;32mPEW ')
