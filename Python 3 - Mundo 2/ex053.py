f = input ('Digite uma frase: ').strip().upper()
p = f.split ()
j = ''.join (p)
i = ''
for l in range (len(j) -1, -1, -1):
    i += (j [l])
    print
print (i, j)
if i == j:
    print ('Temos um palíndromo')
else:
    print ('Não temos um palíndromo')