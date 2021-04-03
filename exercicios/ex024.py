# Desafio 024 -> Crie um programa que leia o nome de uma cidade e diga se ela
#                   começa ou não com o nome "Santo"

nc = input('Qual o nome da sua cidade? ')
fnc = nc.find('Santo')
print('Caso aparecer -1, a cidade não possui Santo, caso apareça 0, possui: {}'.format(fnc))
print('-'*80)
#outra forma
inc = 'Santo' in nc
print('Your city starts with "Santo": {}'.format(inc))
print('-'*80)
#outra forma
snc = nc.split()
print('A sua cidade começa com {}'.format(snc[0]))
print('-'*80)

#outra forma

print('A sua cidade começa com Santo: {}'.format(nc[:5].upper() == 'SANTO'))


#import re
#teste = re.match('Santo', nc)
#print(re.match().string(teste))
#<re.Match object; span=(0, 5), match='Santo'>