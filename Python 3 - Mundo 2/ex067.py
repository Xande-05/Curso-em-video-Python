while True:
    n = int(input('Digite aqui um número para saber sua tabuada (números negativos encerrarão o programa): '))
    c = 1
    if n < 0:
        break
    for c in range(1, 11):
        print (f'{n} * {c} = {n * c}')
print ('Prgrama finalizado!')