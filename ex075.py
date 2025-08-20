num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')),)
print (f'A - o número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print (f'B - o primeiro valor 3 foi digitado na posição {num.index(3)+1}')
else:
    print ('B - não foi digitado nenhum número 3')
print (f'C - os números pares foram...', end= ' ')
for n in num:
    if (n % 2 == 0) >= 1:
        print (n, end=' ')
print ('Fim do programa')
