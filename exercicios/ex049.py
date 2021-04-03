# Desafio 049 -> Refaça o desafio 09 (tabuada),
#                 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numi = int(input('Digite um número para aparecer sua tabuada: '))
numc = 0
for tab in range(0, 10):
    numc += 1
    por = numi * numc
    print('| {:^2} x {:^2} = {:^2} |'.format(numi, numc, por))

# outra forma com o laço sem porco
numin = int(input('Digite um número para aparecer sua tabuada: '))
for unid in range(1, 11):
    print('| {:^2} x {:^2} = {:^2} |'.format(numin, unid, numin*unid))
