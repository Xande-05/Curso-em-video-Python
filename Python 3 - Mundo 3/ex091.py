from random import randint
from time import sleep
ranking = dict()
lista= dict()
jogadas = dict()
print ('JOGADAS')
for c in range (1, 5):
    jogada = randint(1, 6)
    print (f'Jogador {c}: ', jogada)
    lista[f'jogador {c}'] = jogada
    sleep (1)

ranking = sorted(lista.items(), key=lambda x: x[1], reverse=True)
print ('RANKING DOS JOGADORES!')
for c in range (len(ranking)):
    print (f'Em {c+1}° lugar temos o {ranking[c][0]} com {ranking[c][1]} ')
