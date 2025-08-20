valores = []
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        print ('Valor adicionado!')
        valores.append(v)
    else:
        print ('Valor duplicado, não vou adicionar...')
    desejo = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while desejo not in 'SN':
        desejo = str(input('Opçãoi inválida. Deseja continuar? [S/N] ')).upper()[0]
    if desejo in 'Nn':
        break
print (sorted(valores))
print ('Fim ')