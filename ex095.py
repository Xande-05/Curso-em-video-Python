time = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados['Nome'] = input('Nome do jogador: ')
    dados['Partidas'] = (int(input('Quantidade de partidas jogadas: ')))
    for c in range(dados['Partidas']):
        partidas.append(int(input(f'Quantos gols {dados['Nome']} fez na parida {c+1}: ')))
    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    partidas.clear()
    time.append(dados.copy())
    desejo= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if desejo not in 'SN':
        desejo = str(input('Opção inválida. Deseja continuar? [S/N] '))
    if desejo in 'N':
        break
print('-' * 40)
print ('cod/', end='')
for i in dados.keys():
    print (f'{i:<15}', end='')
print ()
print ('=-'*40)
for k, v in enumerate(time):
    print (f'{k+1:>4} ', end='')
    for d in v.values():
        print (f'{str(d):<15}', end='')
    print ()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time)+1:
        print ('Não existe nenhum jogador com essa numereação. Tente novamente.')
    else:
        print (f'-- levantamento do jogador {time[busca-1]["Nome"]}: ')
        for i, g in enumerate(time[busca-1]['Gols']):
            print (f'   No jogo {i+1}, fez {g} gols: ')
    print ('=-'*40)
print ('fim do programa!!')