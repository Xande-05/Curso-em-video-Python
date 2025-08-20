def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    from ex113 import leiaint
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print (linha())
    opc = leiaint('Sua opção: ')