# Desafio 070 -> Faça um pgr. que leia o nome e o preço de vários produtos.
#                o programa deverá perguntar se o usuário vai continuar.
#                No final mostre:
#                A) Qual é o total gasto na compra
#                B) Quantos produtos custam mais de R$1000
#                C)Qual é o nome do produto mais barato
# noinspection NonAsciiCharacters
reqa = reqb = reqc = maior = menor = 0
continuar = 's'
print('°º°' * 5, 'Loja Roseark', 'º°º' * 5)
while continuar == 's':
    nome = str(input('Digite o nome do produto: '))
    preço: float = float(input('Digite o preço do produto: R$'))
    reqa += preço
    if menor <= 0 or preço < menor:
        menor = preço
        reqc = nome
    if preço > 1000:
        reqb += 1
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Informação inválida, por favor tente novamente.\n'
                              'Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        print('Muito obrigado por comprar na Loja Roseark, volte sempre. Aqui está sua nota fiscal:')
print(f'O total de gasto na compra foi de R${reqa}.\n'
      f'{reqb} produtos custam mais de R$1000,00 reais.\n'
      f'{reqc} é o produto mais barato da sua lista de compras.')
