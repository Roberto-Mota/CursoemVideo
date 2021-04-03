# Aula 16 ->
# EM python existem três tipos de variaveis compostas,
# são as tuplas, listas e dicionarios (isso no python)
# As tuplas são imutáveis
# lanche = (tupla, pode ser sem parênteses) [lista] {dicionário}

amigos = 'Léo', 'Amanda', 'Rafael', 'Wellington', 'Thaty'

print('-=-'*10)
for cada in range(0, len(amigos)):
    print(amigos[cada])

print('-=-'*10)
for each in amigos:
    print(f'{each} é um(a) grande amigo(a)')

print('-=-'*10)
for unidade, pessoa in enumerate(amigos):
    print(f'Eu vou sair com com o(a) {pessoa} no {unidade+1}° dia')
