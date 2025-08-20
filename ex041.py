from datetime import date
a= int (input('Digite o ano de nascimento: '))
i= date.today().year - a
if i < 9:
    print ('Sua sua idade é de {} anos e sua categoria é "Mirim"'.format(i))
elif 9 < i <= 14:
    print ('Sua idade é de {} anos e sua categoria é "Infantil"'.format(i))
elif 14 < i <= 19:
    print ('Sua idade é de {} anos e sua categoria é "Junior"'.format(i))
elif 19 < i <= 20:
    print ('Sua idade é de {} anos e sua categoria é "Senior"'.format(i))
else:
    print ('Sua idade é de {} anos e sua categoria é "Master"'.format(i))