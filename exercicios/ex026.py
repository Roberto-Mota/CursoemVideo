# Desafio 026 -> Faça um programa que leia uma frase pelo teclado e mostre:
#                  Quantas vezes aparece a letra "A"
#                  Em que posição ela aparece a primeira vez
#                  Em que posição ela aparece na última vez

frase = str(input('Escreva qualquer frase: ')).lower().strip()

#quantas vezes aparece a letra A
frasec = frase.count('a')
print('A letra "A" aparece {} vezes'.format(frasec))
#Em que posição aparece pela primeira vez
frasef = frase.find('a')
print('A primeira vez que a letra "A" aparece é no {}° caracter'.format(frasef + 1))
#Em que posição aparece pela última vez
fraserf = frase.rfind('a')
print('A posição em que ela aparece pela última vez é: {}' .format(fraserf + 1)
      .format(frasef,frasef))

#não consegui resolver esse, resolução:


