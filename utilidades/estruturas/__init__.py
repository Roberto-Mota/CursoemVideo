from utilidades import dados

def titulo1(titulo):
    print((' ', '-' * len(titulo)), ' ')
    print(' ', f'{titulo}', ' ')
    print((' ', '-' * len(titulo)), ' ')


def linha(tam=42):
    return '-' * tam


def cabe(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabe('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;35m{c}\033[m - \033[38m{item}\033[m')
        c += 1
    print(linha())
    opc = dados.leiaint('\033[36mSua opção:\033[m ')
    return opc
