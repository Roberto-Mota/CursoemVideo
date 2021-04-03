
def formatada(coindo, form='CP'):
    coindo = f'{form} {float(coindo):.2f}'.replace('.', ',')
    return coindo


def aumentar(coindo, porc=10, form=True):
    res = coindo + (coindo * porc / 100)
    if form:
        res = formatada(res)
    return res


def diminuir(coindo, porc=10, form=True):
    res = coindo - (coindo * porc / 100)
    if form:
        res = formatada(res)
    return res


def dobro(coindo, form=True):
    res = coindo * 2
    if form:
        res = formatada(res)
    return res


def metade(coindo, form=True):
    res = coindo / 2
    if form:
        res = formatada(res)
    return res


def resumo(valor, dim=0, aum=0):
    print('-' * 30)
    print(f'{"CARTEIRA":^30}')
    print('-' * 30)
    print(f'CP na carteira: \t{formatada(valor):>13}')
    print(f'Metade da carteira: \t{metade(valor):>8}')
    print(f'Dobro da carteira:  \t{dobro(valor):>10}')
    print(f'{dim}% de redução: \t\t{diminuir(valor, dim)}')
    print(f'{aum}% de aumento: \t\t{aumentar(valor, aum)}')
    print('-' * 30)

