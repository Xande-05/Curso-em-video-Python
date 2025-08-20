print ('Vamos jogar pedra, papel e tesoura! ')
from random import choice
from time import sleep
o= ['pedra', 'papel', 'tesoura']
e= input ('Escolha uma opção entre pedra, papel ou tesoura: ').strip().lower()
m= choice(o)
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')
sleep(1)
print ('Sua escolha: {}'.format (e))
print ('Escolha do computador: {}'.format (m))
if e == 'pedra':
    if m == 'pedra':
        print ('Jogo empatado')
    elif m == 'papel':
        print ('O computador ganhou!')
    elif m == 'tesoura':
        print ('Você ganhou!')
elif e == 'papel':
    if m == 'pedra':
        print ('Você ganhou!')
    elif m == 'papel':
        print ('Jogo empatado')
    elif m == 'tesoura':
        print ('O computador ganhou!')
elif e == 'tesoura':
    if m == 'pedra':
        print ('O computador ganhou!')
    elif m == 'papel':
        print ('Você ganhou!')
    elif m == 'tesoura':
        print ('Jogo empatado')
else:
    print ('Jogada inválida')