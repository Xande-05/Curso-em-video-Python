n= int (input ('Digite aqui um número: '))
print ('[1] Para converter para binário')
print ('[2] Para converter para octal')
print ('[3] Para hexadecimal digite')
e= int (input ('Escolha uma das opções acima: '))
if e == 1:
    print ('{} convertido para binário fica {}'.format(n, bin(n)[2:]))
elif e == 2:
    print ('{} convertido para octal fica {}'.format(n, oct(n)[2:]))
elif e == 3:
    print ('{} convertido para hexadecimal fica {}'.format(n, hex(n)[2:]))
else:
    print ('Você não escolheu uma opção válida')