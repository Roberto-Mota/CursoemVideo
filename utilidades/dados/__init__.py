def valor(msg): #Produz erro ainda quando há digitos tem letras e virgulas.
    ok = False
    while True:
        coindo = input(msg).strip()
        if str(coindo).isnumeric():
            coindo = int(coindo)
            break
        elif not str(coindo).isnumeric():
            try:
                coindo = float(coindo)
                break
            except ValueError:
                coindo = str(coindo)
                if coindo.isalpha():
                    print('\033[1;31mDigito inválido, por favor tente novamente.\033[m')
                elif ',' in coindo:
                    coindo = coindo.replace(',', '.')
                    try:
                        coindo = float(coindo)
                    except ValueError:
                        print('\033[1;31mDigito inválido, por favor tente novamente.\033[m')
                    break
                else:
                    print('\033[1;31mDigito inválido, por favor tente novamente.\033[m')
    return coindo


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!\033[m Digite um número inteiro válido.')
        if ok:
            break
    return valor


def leiafloat(msg):
    while True:
        f = e = input(msg)
        try:
            e = float(f)
        except ValueError:
            print('\033[1;31mDigito inválido!\033[m Tente novamente.')
        else:
            try:
                e = int(f)
            except ValueError:
                break
            else:
                print('\033[1;31mNúmero inteiro!\033[m Tente novamente.')
    return float(f)


def cadastrar(arq, nome='unknown', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um err na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de registrar os dados')
        else:
            print(f'Registro de {nome} adicionado.')
            a.close()