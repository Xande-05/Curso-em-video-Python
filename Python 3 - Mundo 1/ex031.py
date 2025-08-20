d= int (input ('Digite a distância da sua viagem em km: '))
if d <= 200:
    p= d * 0.50
else:
    p= d * 0.45
print ('Sua viagem irá custar {} Reais!'.format(p))