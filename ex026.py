f= str (input('Digite uma frase: ')).strip ().lower()
print ('A letra "a" aparece {} vezes na frase '.format (f.count('a')))
print ('A letra "a" aparece pela primeira vez na posição {}'.format(f.find('a')+1))
print ('A letra "a" aparece pela última vez na posição {}'.format(f.rfind('a')+1))
