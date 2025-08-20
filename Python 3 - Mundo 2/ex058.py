from random import randint
resposta = randint(0, 10)
print ('digite um número entre 0 e 10 e veja se consegue advinhar o que o PC está pensando.')
palpite = 0
tentativa = False
while not tentativa:
    jogador = int (input ('Qual a sua jogada? : '))
    if jogador == resposta:
        tentativa = True
    else:
        if jogador > resposta:
            print ('É menos que isso')
        elif jogador < resposta:
            print ('É mais que isso')
    palpite += 1
print ('A resposta correta é {} e você acertou com {} palpites!'.format (resposta, palpite))