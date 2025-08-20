print ('O funcionário receberá um aumento ')
s= float (input ('Digite aqui o salário do funcionário: '))
if s >= 1250:
    ns= s * 1.1
    print ('Seu novo salário será de R$ {:.2f}'.format(ns))
else :
    ns= s * 1.15
    print ('Seu novo salário será de R$ {:.2f}'.format(ns))