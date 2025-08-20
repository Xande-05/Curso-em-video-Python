d = 0
n = int(input('Digite um valor: '))
for c in range (1, n+1):
    if n % c == 0:
        d += 1
if d == 2:
    print ('O número {} é primo'.format (n))
else:
    print ('O número {} não é primo'.format (n))