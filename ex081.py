lista = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    desejo = input('Deseja continuar? [S/N] ')
    if desejo not in 'SsNn':
        while desejo not in 'SsNn':
            desejo = input('Opção inválida, deseja continuar? [S/N] ')
    elif desejo in 'Nn':
        break
print (lista)
print (f'A = Ao todo foram digitador {len(lista)} elementos.')
lista.sort(reverse=True)
print (f'B = De forma decrescente, a lista fica: {lista}')
if 5 in lista:
    print (f'C = O valor 5 está na lista na posição {lista.index(5)+1}')
else:
    print ('C = O valor 5 não se encontra na lista')
print ('Fim do programa!')
