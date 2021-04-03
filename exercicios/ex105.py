# Desafio 105 -> Crie um programa que tenha uma função chamada notas() que pode receber várias notas de alunos
#                e vai retornar um dicionário com as seguintes informações:
#                - Quantidade de notas
#                - A maior nota
#                - A menor nota
#                - A média da Turma
#                - A situação (opcional)
#                Faça também as docstrings da função
#                ex: resp = notas(5.5, 9.5, 10, 6, sit=True)
ndic = {}
maior = menor = contador = media = 0


def notas(*ns, sit=bool):
    """
    :param ns: Recebe N quantidades de Floats e Int
    :param sit: (opcional) Mostra a situação da média
    :return: retorna dicionário completo
    """
    global maior, menor, contador, media
    for pos, num in enumerate(ns):
        contador += 1
        if pos == 0:
            maior = menor = num
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num
        media += num
    media = media / contador
    ndic['Quantidade'] = contador
    ndic['Maior'] = maior
    ndic['Menor'] = menor
    ndic['Media'] = media
    if media < 5:
        ndic['Situação'] = 'Reprovado'
    elif 5 <= media <= 6:
        ndic['Situação'] = 'Recuperação'
    else:
        ndic['Situação'] = 'Aprovado'
    for k, v in ndic.items():
        if k == 'Situação' and sit:
            print(f'{k}: {v}')
            break
        elif k == 'Situação' and not sit:
            break
        print(f'{k}: {v}')
    return ndic


#programa principal
resp = notas(5.5, 9.5, 10, 6, sit=True)
print(resp)

# Jeito do Professor


def notas2(*n, sit=False):
    """"
        :param ns: Recebe N quantidades de Floats e Int
        :param sit: (opcional) Mostra a situação da média
        :return: retorna dicionário completo
        """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] < 5:
            r['Situação'] = 'Reprovado'
        elif 5 <= r['media'] <= 6:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'Aprovado'


# Programa Principal
resp = notas2(5.5, 2.5, 9, 8.5)
print(resp)
help(notas2)
