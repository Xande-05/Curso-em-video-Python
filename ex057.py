r = str(input('Digite aqui o seu sexo [M/F]: ')).lower().strip()[0]
while r not in 'mf':
    print ('Opção inválida.')
    r = str (input ('Tente novamente: ')).lower().strip()[0]
print ('Obrigado!')
