from datetime import date
mai = 0
men = 0
for c in range(0, 7):
    i = int(input('Qual digite um ano de nascimento: '))
    if date.today().year - i >= 21:
        mai += 1
    else:
        men += 1
print ('{} pessoas ainda não atingiram a maioridade enquanto {} já atingiram a maioridade'.format(men, mai))
