# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que
# permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

char1 = []
char1.append('Paulo')
char1.append('23')
print(f'Char1 depois do append:{char1}')

print('-=-'*10)
char2 = []
char2.append(char1[:]) #se eu copiar char1 seguido de [:], o resultado é diferente
print(f'Char1 depois do char2.append(char1): {char1}\n'
      f'Char2 depois do char2.append(char1): {char2}')
print('-=-'*10)

char1[0] = 'Thaty'
char1[1] = 22
print(f'char1 depois de atribuir Thaty / 22 pra char1[0] e char1[1]: {char1}\n'
      f'char2 depois de atribuir Thaty / 22 para char1[0] e char1[1]: {char2}')
print('-=-'*10)

char2.append(char1[:]) #se eu copiar char1 seguido de [:], o resultado é diferente
print(f'Char1 depois do char2.append(char1[:]): {char1}\n'
      f'Char2 depois do char2.append(char1[:]): {char2}')