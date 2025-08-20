mi = 0
h = 0
nh = ''
m = 0
for c in range(1, 5):
    print ('-------- {} PESSOA --------'.format(c))
    s = input ('Digite o sexo [M/F]: ').strip (). upper()
    n = input ('Digite o nome: ').strip (). upper()
    i = int (input('Digite o idade: '))
    mi += i
    if i > h and s == 'M':
            h = i
            nh = n
    if i < 20 and s == 'F':
        m += 1
print ('A média de idade é de: {}'.format(mi/4))
print ('O homem mais velho tem {} anos e se chama: {}'. format (h, nh))
print ('Temos aqui {} mulheres abaixo de 20 anos'. format (m))