c = float (input ('Digite aqui o valor da casa em Reais: '))
s= float (input ('Digite aqui o valor do seu salário tambem em Reais: '))
a= int (input ('Em quanto anos você pretende pagar pela casa: '))
p= (c / a) / 12
if p < (s * 0.3):
    print ('Você irá pagar {:.2f} Reais por mês em prestacões e o empréstimo será feito!'.format(p))
else:
    print ('Você irá pagar {:.2f} Reais por mês em prestações e não será possível realizar o empréstimo. '.format(p))