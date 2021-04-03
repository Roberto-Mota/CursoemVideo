# Desafio 097 -> Crie um programa que tenha uma função chamada escreva() que receba textos quaisquer
#                   como parâmetro
#                   e mostre uma msg com tamanho adaptável (com os ---- do mesmo tamanho)

def escreva(txt):
    print('-' * (len(txt)))
    print(txt)
    print('-' * (len(txt)))

while True:
    texto = str(input('Digite o texto: '))
    escreva(texto)
    # tambem pode escrever direto no "escreva(texto qqr aqui)"
