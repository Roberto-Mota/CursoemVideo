# Desafio 083 -> C. um programa onde o usuario digite uma expressão qualquer que use parênteses.
#                   Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
#                   e fechados na ordem correta
#                   Ex:((a+b) * c) - da bom
#                   ex: ((a+b) * c)) - deu merda (tem parenteses a mais, tambem podendo ser a menos)

lista = []
exp = str(input('Type a expression: ')).split()
print(exp)
for p in exp:
    for l in p:
        print(l, end="-")
        lista.append(l, )
qesq = lista.count('(')
qesq2 = lista.count('[')
qesq3 = lista.count('{')
qdir = lista.count(')')
qdir2 = lista.count(']')
qdir3 = lista.count('}')
if qesq != qdir or qesq2 != qdir2 or qesq2 != qdir2:
    print('The quantity of brackets is no equivalent, because:')
if '(' in lista or ')' in lista:
    print('There are parentheses,', end=' ')
    if qesq == qdir:
        sesqdir = []
        print('the quantity is equivalent,', end=' ')
        for num, e in enumerate(lista):
            if e == '(':
                sesqdir.append(e)
            elif e == ')' and len(sesqdir) > 0:
                sesqdir.pop()
            else:
                error1 = True
                break
        if len(sesqdir) == 0:
            print('and the order is right!')
        elif error1 or len(sesqdir) != 0:
            print('but the order is not right!')
        # a soma da quantidade de (( tem que ser sempre menor que )), portanto que a quantidade seja igual
    else:
        print('but the quantity is not equivalent.')
if '[' in lista or ']' in lista:
    print('There are brackets', end=' ')
    if qesq2 == qdir2:
        sesqdir2 = []
        print('the quantity is equivalent', end=' ')
        for num, e in enumerate(lista):
            if e == '[':
                sesqdir2.append(e)
            if e == ']' and len(sesqdir2) > 0:
                sesqdir2.pop()
            else:
                error2 = True
                #talvez tbm poderia colocar o print de ordem not right aqui
                break
        if len(sesqdir2) == 0:
            print('an the order is right!')
        elif len(sesqdir2) != 0 or error2:
            print('but the order is not right!')
    else:
        print('but the quantity is not equivalent.')
if '{' in lista or '}' in lista:
    print('There are bracers', end=' ')
    if qesq3 == qdir3:
        print('the quantity is equivalent', end=' ')
        sesqdir3 = []
        for pos, e in enumerate(lista):
            if e == '{':
                sesqdir3.append(e)
            elif e == '}' and len(sesqdir3) > 0:
                sesqdir3.pop()
            else:
                error3 = True
        if len(sesqdir3) == 0:
            print('and the order is right!')
        elif len(sesqdir3) != 0 or error3:
            print('but the order is not right!')
    else:
        print('but the quantity is no equivalent.')
