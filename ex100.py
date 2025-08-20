from random import randint
from time import sleep
numeros= list()
def par(valor):
    soma = 0
    print ('Somando os valores pares da lista...')
    sleep(1)
    print ('Os valores pares são: ', end='')
    for c in valor:
        if c % 2 == 0 and c != 1:
            soma += c
            print(f'{c} - ', end='')
    print (f'A soma de todos esses valores é igual a: {soma}')


def sorteio():
    print ('Sorteando 5 valores...')
    sleep(1)
    for c in range(0,5):
        numeros.append(randint(1,10))
    print(numeros, 'Está feito!')
    par(numeros)

sorteio()
print ('FIM DO PROGRAMA!')