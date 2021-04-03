# laço c no intervalo(1,10):
#    x passo
#    x if alguma coisa:
#         x da um pulo carpado
#    x identação
#pega
# for c in range(1,10):
#    x passo
#    x identação
#pega

print('oi')
print('oi')
print('oi')
print('oi')
print('-=-'*11)
for x in range(1, 5):
    print('oi')
print('-=-'*11)
for y in range(5, 0, -1):
    print(y)
print('-=-'*11)
for z in range(0, 5, 2):
    print(z)
print('-=-'*11)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for passo in range(i, f+1, p):
    print(passo)
print('-=-'*11)
s = 0
for teste in range(0, 5):
    num = int(input('Valor: '))
    s += num #equivale a  (s = s + n)
print('Soma dos valores: {}'.format(s))
print('-=-'*11)
