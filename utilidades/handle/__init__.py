from utilidades import estruturas


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarq(nome):
    try:
        a = open(nome, 'wt+') #write, text, se não tiver cria um (+)
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado.')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        estruturas.cabe('PESSOAS CADASTRADAS')
        for linha in a: #readlines() le as paradas por linha, podendo fazer tupla ou lista
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
