def metade(num):
    res = (f'R${num / 2:>.2f}'.replace('.', ','))
    return res

def dobro(num):
    res = (f'R${num * 2:>.2f}'.replace('.', ','))
    return res

def aumenta(num, taxa=1):
    res = (f'R${num+(num*taxa/100):>.2f}'.replace('.', ','))
    return res

def diminui(num, taxa=1):
    res = (f'R${num-(num*taxa/100):>.2f}'.replace('.', ','))
    return res

def resumo(num=0, ta=10, tr=20):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \tR${num:.2f}'.replace('.', ','))
    print(f'Dobro do valor: \t{dobro(num)}')
    print(f'Metade do valor: \t{metade(num)}')
    print(f'{ta}% de aumento: \t{aumenta(num, taxa=tr)}')
    print(f'{tr}% de redução: \t{diminui(num, taxa=tr)}')
    print('-'*30)

def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print ('Preço inválido.')
        else:
            válido = True
            return float(entrada)