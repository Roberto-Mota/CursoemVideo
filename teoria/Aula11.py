# ANSI
# escape sequence
# \033[style(tipo de fonte) text(cor do texto) back(cor do fundo)m
# \033[0;33;44m
# Style mais comuns 0(padrão) 1(bold:negrito) 4(underline:sublinhar) 7(negativo:troca com o fundo)
# Text basicão 30 31 32 33 34 35 36 37
# Back basicão 40 41 42 43 44 45 46 47
nome = input('Qual seu nome? ')
print('\033[0;33;0mOlá\033[m')
print('Prazer em te conhecer, {}{}{}!'.format('\033[1;32m', nome, '\033[m'))
    #pode simplificar as cores
cores = {'vermelho':'\033[31m',
         'azul':    '\033[34m',
         'amarelo': '\033[33m',
         'branco':  '\033[30m',
         'roxo':    '\033[35m',
         'verde':   '\033[32m',
         'ciano':   '\033[36m',
         'limpa':   '\033[m',
         'bandw.':  '\033[7;30;m',
    #cores em negrito
         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',
    # cores sublinhadas
        'vermelho sublinhado': '\033[4;31m',
        'azul sublinhado': '\033[4;34m',
        'amarelo sublinhado': '\033[4;33m',
        'branco sublinhado': '\033[4;30m',
        'roxo sublinhado': '\033[4;35m',
        'verde sublinhado': '\033[4;32m',
        'ciano sublinhado': '\033[4;36m'}

#branco = 0
#vermelho = 1
#verde = 2
#amarelo = 3
#azul = 4
#roxo = 5
#azulclaro = 6
#cinta = 7
#cores = {  # cores normais

    #         'vermelho':'\033[31m',
    #         'azul':    '\033[34m',
    #         'amarelo': '\033[33m',
    #         'branco':  '\033[30m',
    #         'roxo':    '\033[35m',
    #         'verde':   '\033[32m',
    #         'ciano':   '\033[36m',
    #         'limpa':   '\033[m',
    #         'bandw.':  '\033[7;30;m',

    # cores em negrito
    #
    #         'vermelho em negrito':'\033[1;31m',
    #         'azul em negrito':'\033[1;34m' ,
    #         'amarelo em negrito':'\033[1;33m' ,
    #         'branco em negrito':'\033[1;30m',
    #         'roxo em negrito':'\033[1;35m',
    #         'verde em negrito':'\033[1;32m',
    #         'ciano em negrito':'\033[1;36m',

    # cores sublinhadas

    #    'vermelho sublinhado': '\033[4;31m',
    #    'azul sublinhado': '\033[4;34m',
    #    'amarelo sublinhado': '\033[4;33m',
    #    'branco sublinhado': '\033[4;30m',
    #    'roxo sublinhado': '\033[4;35m',
    #    'verde sublinhado': '\033[4;32m',
    #    'ciano sublinhado': '\033[4;36m'
