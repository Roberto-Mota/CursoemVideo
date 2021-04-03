# Desafio 077 -> C. um programa que tenha uma tupla com várias palavras (ñ usar acentos).
#                Depois disso, você deve mostrar, para cada palavra, quais são as sua vogais
tupnom = ()
print(dir(tupnom))
print('-=-'*5, 'Encontro das Vogais', '-=-'*5)
for unit in range(0, 5):
    tupnomin = input(f'Digite a {unit+1}° palavra: ').lower().strip()
    tupnom += (tupnomin,)
print(tupnom)
for palavra in tupnom:
    print(f'\nNa palavra {palavra.capitalize()} temos ->', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
