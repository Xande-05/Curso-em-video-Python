r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triangulo:', end='')
    if r1 == r2 == r3:
        print (' Equilátero')
    elif r1 != r2 != r3 != r1:
        print (' Escaleno')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print (' Isósceles')
else:
    print('Não forma um triangulo')
