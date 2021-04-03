# Desafio 112 -> Dentro do pacote utilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
#                chamada leiadinheiro() que seja capaz de funcionar como a função input(),
#                mas com uma validação de dados para aceitar apenas valores que sejam monetários

from utilidade import coindo
from utilidade import dados

valor = dados.valor('Digite a quantidade de CP: ')
coindo.resumo(valor, 10, 20)