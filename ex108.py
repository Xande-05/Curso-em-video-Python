import moeda

n= int(input('Digite o preço: '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é igual a {moeda.dobro(n)}')
print(f'Aumentando 10% de {n} temos: {moeda.aumenta(n, 10)}')
print(f'Reduzindo 13% de {n} temos: {moeda.diminui(n, 13)}')