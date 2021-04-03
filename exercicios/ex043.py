# Desafio 043 -> Desenvolva uma logica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#               -  Abaixo de 18.5 : abaixo do peso
#               -  entre 18.5 e 25: peso ideal
#               -  25 até 30: sobre peso
#               -  30 até 40: obesidade
#               -  acima de 40: obesidade mórbida
# IMC = Peso ÷ (Altura × Altura)

alt = float(input('Qual sua altura em Metros e Cm? '))
kg = float(input('Qual seu peso em Kg? '))
imc = kg / (alt * alt)
print('Seu IMC é {:.2f}, o que define'.format(imc), end=' ')

if 18.5 > imc:
    print('peso abaixo do ideal')
elif 18.5 <= imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobre peso')
elif 30 < imc <= 40:
    print('obesidade')
elif 40 < imc:
    print('obesidade mórbida')
