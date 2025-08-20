lista = [[], [], []]
somapar = somaterceira = maxsegunda = 0
for c in range (0,3):
    for v in range(0,3):
        valor = int(input(f'Digite um valor para a posição [{c},{v}]: '))
        if c == 0:
            lista[0].append(valor)
        elif c == 1:
            lista[1].append(valor)
        else:
            lista[2].append(valor)
        if valor % 2 == 0:
            somapar += valor
        if v == 2:
            somaterceira += valor
print ('*'*20)
print (lista[0])
print (lista[1])
print (lista[2])
print ('*'*20)
print (f'A soma dos valores pares é igual a: {somapar}')
print (f'A soma dos valores da terceira coluna é igual a: {somaterceira}')
print (f'O maior valor da segunda linha é igual a: {max(lista[1])}')
