from datetime import date
a= int (input ('Digite um ano para saber se ele é bissexto e digite "0" para saber sobre o ano atual: '))
if a== 0:
    a= date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print ('O ano de {} é bissexto!'.format(a))
else:
    print ('O ano de {} não é bissexto!'.format(a))
