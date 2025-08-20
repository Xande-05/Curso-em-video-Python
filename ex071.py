print ('CAIXA ELETRÔNICO, BEM VINDO')
print ('-='*20)
saque = int (input ('Qual é o valor do saque em Reais: '))
cédula50 = saque // 50
cédula20 = (saque - (50 * cédula50)) // 20
cédula10 = ((saque - (50 * cédula50)) - (20 * cédula20)) //10
cédula1 = saque % 10
if cédula50 > 0:
    print (f'Total de {cédula50} cédulas de 50 reais.')
if cédula20 > 0:
    print (f'Total de {cédula20} cédulas de 20 Reais.')
if cédula10 > 0:
    print (f'Total de {cédula10} cédulas de 10 reais.')
if cédula1 > 0:
    print (f'Total de {cédula1} cédulas de 1 Real.')
print ('Fim do programa')