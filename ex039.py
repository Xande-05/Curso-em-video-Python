from datetime import date
a= int (input ('Digite aqui seu ano de nascimento: '))
i= date.today().year - a
if i > 18:
    t= i - 18
    print ('Você tem {} anos e já passaram {} anos da época de alistamento militar!'.format(i, t))
    print ('Seu alistamento miliar foi (ou deveria ter sido) em {}'.format (a + 18))
elif i < 18:
    t= 18 - i
    print ('Você tem {} anos e ainda faltam {} anos para a época de alistamento militar!'.format(i, t))
    print ('Seu alistamento militar será em {}'.format(a + 18))
else:
    print ('Você tem {} anos e deve se alistar ainda esse ano! '.format(i))
