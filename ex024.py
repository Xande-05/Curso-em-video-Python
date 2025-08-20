c= str (input ('Digite o nome da sua cidade: ')).strip()
c= c. split()[0]
print ('O nome da sua cidade começa com "Santo": {}'.format('santo' in c.lower()))
