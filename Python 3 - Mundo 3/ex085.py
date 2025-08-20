lista = [[], []]
print ('Preciso que digite pa mim 7 valores!')
for c in range (1,8):
    valor = int(input(f'Digite o {c}° numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print (f'Os valores pares em ordem crescente foram: {sorted(lista[0])}')
print (f'Os valores ímpares em ordem crescente foram: {sorted(lista[1])}')