# Desafio 115 -> Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome
#                   e idade em um arquivo de texto simples.
#                O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from utilidades import dados
from utilidades import cores
# Menu
while True:
    print('-' * 32)
    print(f'{"MENU PRINCIPAL":^32}')
    print(f'-' * 32)
    print('1 - \033[34;1mLista de pessoas cadastradas\033[m\n'
          '2 - \033[34;1mCadastrar uma nova pessoa\033[m\n'
          '3 - \033[34;1mSair do menu\033[m')
    print('-' * 32)
    sele = dados.leiaint('Sua opção: ')
    while True:
        if 1 <= sele <= 3:
            if sele == 1:                               # Ver a lista
                print('-' * 32)
                print(f'{" LISTA DE CADASTRADOS ":^32}')
                print('-' * 32)
                with open("teste.txt", 'r') as f:
                    conteudo = f.read()
                    print(conteudo)
                    sair = input('Aperte enter para voltaro ao menu principal.')
                    break
            elif sele == 2:                             # Cadastrar na lista
                print(' ', '-' * 32)
                print(f'{" CADASTRO DE USUÁRIOS ":^32}')
                print(f' ', '-' * 32)
                with open("teste.txt", 'a') as f:
                    while True:
                        nome = input('Digite o nome: ')
                        idade = dados.leiaint('Idade: ')
                        while True:                      # Confirmação de cadastro
                            conf = input('Confirmar cadastro? [S/N]').lower().strip()[0]
                            if conf not in 'sn':
                                print('Opção inválida, tente novamente.')
                            elif conf == 'n':
                                break
                            else:
                                f.write(f'\n{nome} {idade}')
                                print('Usuário cadastrado com sucesso!')
                                break
                        break
                    f.close()
                    break
            elif sele == 3:
                print(' ', '-' * 32)
                print(f'{" ENCERRAR PROGRAMA ":^32}')
                print(f' ', '-' * 32)
                break

            print('Blz')
        else:
            while True:
                print('Opcão inválida')
                sele = dados.leiaint('Sua opção: ')
                if 1 <= sele <= 3:
                    break


#Ver a lista

#Cadastrar uma nova pessoa
#with open("teste.txt", 'w') as f:
#    f.write(f'{nome} {idade}')






#Sair do programa
