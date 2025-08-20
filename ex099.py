from random import randint
contagem1= list()
contagem2= list()
contagem3= list()
contagem4= list()
def lista(num):
    print (num)
    if num == 0:
        print (f'Foram analisados {num} valores ao todo e o maior deles é  {num}')
    else:
        print (f'Foram analisados {len(num)} números e o maior deles foi o {max(num)}')



print ('=-'*30)
print ('Analisando os valores passados...')
for c in range (0, 6):
    contagem1.append (randint (0, 10))
lista (contagem1)
for c in range (0, 3):
    contagem2.append (randint (0, 10))
lista (contagem2)
for c in range (0, 2):
    contagem3.append (randint (0, 10))
lista (contagem3)
for c in range (0, 1):
    contagem4.append (randint (0, 10))
lista (contagem4)
lista (0)