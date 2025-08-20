from random import randint
n= randint(0,5)
print ('Seu computador escolheu um número entre 0 e 5, tente advinhar qual é: ')
nu= int (input ('Digite seu número entre 0 e 5: '))
if nu == n:
    print ('O número correto é o "{}", e você acertou!'.format (n))
else:
    print ('O número correto é o "{}", e você errou!'.format (n))
