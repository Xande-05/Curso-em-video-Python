v= int (input ('Digite a velocidade do seu carro em km/h: '))
if v > 80:
    e= v - 80
    m= e * 7
    print ('Você ultrapassou a velocidade máxima e será multado em {} Reais! '.format(m))
else:
    print ('Nada de multa, tudo certo por aqui! ')