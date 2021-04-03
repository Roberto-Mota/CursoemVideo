from utilidades import dados
from utilidades import estruturas
from time import sleep


arq = 'tab_nom_ida.txt'
if dados.arqexiste(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
if dados.criarq(arq):
    print('Arquivo criado.')
else:
    print('Arquivo não foi criado.')

while True:
    resposta = estruturas.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        estruturas.cabe('Opção 1')
    elif resposta == 2:
        estruturas.cabe('NOVO CADASTRO')
        nome = str('Nome: ')
        idade = dados.leiaint('Idade: ')
    elif resposta == 3:
        estruturas.cabe('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31;1mErro!\033[m Digite um número válido')
    sleep(1.5)
