valores = []
for v in range(1, 6):
    valores.append(int(input(f'Digite o {v}º valor: ')))
posmax = valores.index(max(valores))
posmin = valores.index(min(valores))
print (f'O maior valor digitado foi o {max(valores)} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == max(valores):
        print (f'[{i}]', end = '')
print (f'\nO menor valor digitado foi o {min(valores)} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == min(valores):
        print (f'[{i}]', end = '')