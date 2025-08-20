n1= float (input ('Digite aqui sua primeira nota: '))
n2= float (input ('Digite aqui sua segunda nota: '))
m= (n1 + n2) / 2
if 11 > m >= 7:
    print ('Sua média foi de {:.1f} e você está aprovado!'.format(m))
elif 7 > m >= 5:
    print ('Sua média foi de {:.1f} e você está de recuperação!'.format(m))
elif 5 > m:
    print ('Sua média foi de {:.1f} e você está reprovado!'.format(m))
else:
    print ('Você tem uma média inválida!')