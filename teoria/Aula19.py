# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves literais.
#
Dicionários = {}
print()
print('Dicionários:\n')
dados = {'nome': 'Paulo', 'idade': '23'}
print('Nome: ', dados['nome'])
print('Idade: ', dados['idade'])
dados['sexo'] = 'Masculino'
dados = {'nome': 'Paulo', 'idade': '23', 'sexo': 'Masculino'}  # ele vira isso depois da linha 10
print('Values: ', dados.values())
print('Keys: ', dados.keys())
print('Items: ', dados.items())
print('-=-' * 10, '\n')
print('Estrutura de loop:\n')
for k, v in dados.items():
    print(f'O {k} : {v}')
dados['profissão'] = 'N/A'
del dados['profissão']
# da pra colocar dicionarios dentro de listas tipo na lista turma-> print(turma[0]['nome'] -> output: Pedro
print('-=-' * 10, '\n')
print('Dicionários dentro de listas:\n')
brasil = []
estado1 = {'uf': 'Distrito Federal', 'sigla': 'DF'}
estado2 = {'uf': 'Pará', 'sigla': 'PA'}
brasil.append(estado1)
brasil.append(estado2)
print('A sigla do estado do Distrito Federal é: ', brasil[0]['sigla'])

pessoa = {}
amigos = []
for c in range(0, 3):
    pessoa['nome'] = str(input('Nome da pessoa: '))
    pessoa['idade'] = int(input('Idade: '))
    # amigos.append(pessoa[:]) ---- como usava antigamente não rola pq dicionario nao permite fatiamento
    amigos.append(pessoa.copy())
    continuar = input('Deseja continuar?')
    if continuar == 'n':
        break
for p in amigos:
    print(p)
