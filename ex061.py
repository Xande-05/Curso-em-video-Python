print ('Faremos uma progressão aritmética com os 10 primeiros trmos')
p= int (input('Digite o primeiro termo da PA: '))
r= int (input('Digite a razão da PA: '))
c = 1
while c < 11:
    print (p, end = ' - ')
    p = p + r
    p += r
    c += 1