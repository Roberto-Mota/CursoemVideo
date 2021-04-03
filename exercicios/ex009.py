#Desafio 009 -> Faça um programa que leia um número inteiro qualquer
#               e mostre na tela a sua tabuada

numint = int(input('Digite um número para aparecer sua tabuada: \n'))
aa = numint*1
bb = numint*2
cc = numint*3
dd = numint*4
ff = numint*5
gg = numint*6
hh = numint*7
ii = numint*8
jj = numint*9
kk = numint*10
print('{:^4} {:^4} {:^4} {:^4} {:^4}\n{:^4} {:^4} {:^4} {:^4} {:^4}'.format(aa,bb,cc,dd,ff,gg,hh,ii,jj,kk))

# Bem formatada

print('__________\n{:2} x 1 = {:2}\n{:2} x 2 = {:2}\n{:2} x 3 = {:2}\n{:2} x 4 = {:2}\n'
      '{:2} x 5 = {:2}\n{:2} x 6 = {:2}\n{:2} x 7 = {:2}\n{:2} x 8 = {:2}\n{:2} x 9 = {:2}\n{:2} x 10 = {:2}'
      '\n___________'.format(numint, (numint*1), numint, (numint*2), numint, (numint*3), numint, (numint*4), numint, (numint*5), numint, (numint*6), numint, (numint*7), numint, (numint*8), numint, (numint*9), numint, (numint*10)))