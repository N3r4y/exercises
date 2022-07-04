def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n0\33[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def line(tam = 42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lista):
    header('MENU PRINCIPAL')
    count = 1
    for item in lista:
        print(f'\033[33m{count}\033[m - \033[34m{item}\033[m')
        count += 1
    print(line())
    opc = readInt('\033[33mDigite a opção desejada: \033[m')
    return opc