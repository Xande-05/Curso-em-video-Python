print ('Bem vindo a nossa loja.')
valfinal = caros = pbarato = 0
nbarato = ''
while True:
    print ('-'*30)
    nome = input ('Qual é o nome do produto: ')
    preço = float(input('Qual é o preço do produto em Reais: '))
    if preço < pbarato or pbarato == 0:
        nbarato = nome
        pbarato = preço

    if preço > 1000:
        caros += 1
    valfinal += preço
    desejo = input ('Deseja continuar? [S/N] ').upper()[0]
    while desejo not in 'SN':
        desejo = input ('Opção inválida, deseja continuar? [S/N] ').upper()[0]
    if desejo == 'N':
        break
print (f'A - o somatório de toda a compra foi de {valfinal} reais.')
print (f'B - {caros} produtos ultrapassaram o valor de 1000 R')
print (f'C - {nbarato} é o nome do produto mais barato que custa {pbarato} Reais.')