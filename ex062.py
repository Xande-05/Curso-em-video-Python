print ('Vamos fazer uma progressão aritmética com a quantidade de termos que você definir')
termo = 1
c = 0
while c != termo:
    primeiro = int(input('Primeiro termo: '))
    c = 0
    razao =int(input('Razao: '))
    termo =int(input('Quantos termos: '))
    while c < termo:
        print (primeiro, end = ' ')
        primeiro += razao
        c += 1
print ('FIM')