lista = [[], [], []]
for c in range (0,3):
    for v in range(0,3):
        valor = int(input(f'Digite um valor para a posição [{c},{v}]: '))
        if c == 0:
            lista[0].append(valor)
        elif c == 1:
            lista[1].append(valor)
        else:
            lista[2].append(valor)
print (lista[0])
print (lista[1])
print (lista[2])