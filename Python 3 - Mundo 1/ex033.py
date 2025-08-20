n1= int (input ('Digite o primeiro número: '))
n2= int (input ('Digite o segundo número: '))
n3= int (input ('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    max= n1
if n2 > n3 and n2 > n1:
    max= n2
if n3 > n1 and n3 > n2:
    max = n3

if n1 < n2 and n1 < n3:
    min= n1
if n2 < n3 and n2 < n1:
    min= n2
if n3 < n1 and n3 < n2:
    min = n3
print ('O maior número é o {}'.format(max))
print ('O menor número é o {}'.format(min))