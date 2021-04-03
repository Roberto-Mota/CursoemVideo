# Desafio 066 ->  Crie um prgrma que leia varios numeros inteiros pelo teclado.
#                 O programa só vai aprar quando ler a flag 999. no final mostrar quantos numeros foram digitados
#                 e qual foi a soma entre eles (desconsidrenado a flag)
num = cont = nums = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    nums += num
    cont += 1
print(f'Você digitou um total de {cont} valores que somados ao todo equivale a {nums}.')
