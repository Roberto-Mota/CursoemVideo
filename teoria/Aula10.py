# Fase 10 -> Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas
#            nos seus programas em Python.
# objeto.metodo()
# carro.siga()
# carro.esquerda()
#   if carro.esquerda():
#       x bloco _v_ True
#       x identação
#       x identação
#       x identação
#   else:
#       x carro.direita():
#       x bloco_F_ False
#       x identação
#       x
#       x
#   carro.pare()
#
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('carro velho')
print('--Condições Simplificadas:--')
#
# Condições simplificadas da mesma situação
#
print('carro novo' if tempo <= 3 else 'carro velho')
#
print('-' * 50)
nome = str(input('Qual seu nome? '))
if nome == 'Paulo':
    print('Olá novamente, como você está?')
else:
    print('Bom dia {}'.format(nome))

print('-' * 50)