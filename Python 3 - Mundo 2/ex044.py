p= float (input ('Digite aqui o valor a ser pago pelo produto: '))
print (''' [1] à vista no dinheiro (10% de desconto)
 [2] à vista no cartão (5% de desconto)
 [3] em até 2X no cartão
 [4] 3X ou mais no cartão (20% de juros)''')
c= int ( input ('E qual será sua forma de pagamento:'))

if c == 1:
    pf= p - (p * 0.1)
    print ('O valor do produto será R$ {:.2f}'.format(pf))
elif c == 2:
    pf= p - (p * 0.05)
    print ('O valor do produto será R$ {:.2f}'.format(pf))
elif c == 3:
    pf= p / 2
    print ('O valor do produto será pago em duas parcelas de R$ {:.2f}'.format(pf))
elif c == 4:
    ps= int (input ('Digite aqui a quantidade de parcelas a serem pagas: '))
    pf= p + (p * 0.2)
    pp= pf / ps
    print ('O valor do produto será pago em {} parcelas de R$ {:.2f}'.format(ps, pp))
else:
    print ('Opção inválida de pagamento')
