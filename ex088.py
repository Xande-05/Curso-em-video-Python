from random import randint
from time import sleep
print ('='*30)
print ('JOGO NA MEGA SENA')
print ('='*30)
valor = int(input('Quantos jogos você quer que eu sorteie? '))
lista = list()
resultado = 0
print (f'SORTEANDO {valor} JOGADAS...')
sleep(1)
for c in range(1, valor+1):
    print (f'\nJogo {c}...', end='')
    for v in range(1, 7):
        resultado = randint(1, 60)
        if resultado not in lista:
            lista.append(resultado)
        else:
            lista.append(randint(1, 60))
    print (sorted(lista), end=' ')
    sleep(1)
    lista.clear()
print ('\nFim do programa!')
