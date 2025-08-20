print ('Vamos fazer uma sequência de fibonacci')
n = int(input('Quantos termos você gostaria de ver da sequência: '))
c = 3
n1 = 0
n2 = 1
n3 = 1
print (0, 1, end = ' ')
while c < n:
    n3 = n1 + n2
    print (n3, end = ' ')
    n1 = n2
    n2 = n3
    c += 1