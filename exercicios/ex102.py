# Desafio 102 -> Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros:
#                o primeiro que indique o número a calcular e o outro chamado show, que será um valor
#                (opcional) indicando se será mostrado ou não na tela o processo de cálculo fatorial
#   print(fatorial(5, show=False)


def fatorial(n=0, show=bool):
    if show:
        for num in range(n+1, 1, -1):
            if num == 2:
                print(f'{num-1} =', end=' ')
            else:
                print(f'{num-1} x', end=' ')
    else:
        pass
    for num in range(n-1, 1, -1):
        n *= num
    print(n)


fatorial(7, show=True)
