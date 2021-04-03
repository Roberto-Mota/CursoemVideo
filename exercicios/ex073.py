# Desafio 073 -> C. uma tupla com os 20 primeiros colocados da tabela do Brasileirão,
#                na ordem de colocação. depois mostre:
#                A) Apenas os 5 primeiros colocados
#                B) Os últimos 4 colocados da tabela.
#                C) Uma lista com os times em ordem alfabética.
#                D) Em que posição na tabela está o time do Chapecoense
times = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Cotinthians',
         'Flamengo', 'Atletico Mineiro', 'Athletico Paranaense',
         'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo',
         'Fluminese', 'Vasco', 'Bahia', 'Sport', 'Vitória', 'Ponte Preta',
         'América', 'Coritiba')
print('-=-'*20)
print(f'A ordem de colocação é:\n'
      f'{times}')
print('-=-'*20)
print(f'A) Apenas os 5 primeiros colocados:\n'
      f'{times[:5]}')
print('-=-'*20)
print(f'B) Os últimos 4 colocados da tabela:\n'
      f'{times[-4:]}')
print('-=-'*20)
print(f'C) Uma lista com os times em ordem alfabética:\n'
      f'{sorted(times)}')
print('-=-'*20)

print(f'D) Em que posição na tabela está o time do Chapecoense:')

#método index
print(f"{times.index('Chapecoense')}° posição")

#método com for (pode jogar um "if not", fazendo um programa mais redondinho
#for posição, time in enumerate(times):
#    if 'Chapecoense' in time:
#        print(f'{posição + 1}° posição')
