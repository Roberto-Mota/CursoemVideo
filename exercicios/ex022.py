# Desafio 022 -> Crie um programa que leia o nome completo de uma pessoa e mostre:
#                  O nome com todas as letras maiúsculas
#                  O nome com todas minúsculas
#                  Quantas letras ao to do (sem considerar espaços).
#                  quantas letras tem o primeiro nome

nco = (input('Digite seu nome completo: ')).strip()
ncou = nco.upper()
ncol = nco.lower()
ncose = nco.count(' ')
ncoc = len(nco) - ncose
ncosp = nco.split()
#tambem pode procurar o primeiro espaço, que vai jogar o valor do tamanho do nome completo
# ncosp = nco.find(' ') daí print(ncosp)
print('O nome com todas as letras maiúscula: {}\n'
      'O nome com todas as letras minúsculas: {}\n'
      'A quantidade de letras ao todo: {}\n'
      'A quantidade de letras do primeiro nome ({}) : {}'.format(ncou, ncol, ncoc, ncosp[0],  len(ncosp[0])))
