d= int (input ('Quantos dias o carro foi alugado? '))
k= int (input ('Quantos KMs o carro rodou? '))
a= (d * 60) + (k * 0.15)
print ('O aluguel do carro será de R${:.2f}'.format(a))