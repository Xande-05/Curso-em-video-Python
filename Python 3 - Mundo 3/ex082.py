lista = list()
listapar = list()
listaimpar = list()
while True:
    lista.append (int(input('Digite um valor: ')))
    desejo = input('Quer continuar? [S/N] ').upper()[0]
    if desejo not in 'NnSs':
        while desejo not in 'NnSs':
            desejo = input('Opção inválida, deseja continuar? [S/N] ').upper()[0]
    elif desejo in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print (f'Os valores digitados foram: {lista}')
print (f'Os valores pares digitados foram {listapar}')
print (f'Os valores ímpares digitados foram: {listaimpar}')