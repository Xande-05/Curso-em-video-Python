dados = dict()
partidas = list()
dados['Nome'] = input('Nome do jogador: ')
dados['Partidas'] = (int(input('Quantidade de partidas jogadas: ')))
for c in range(dados['Partidas']):
    partidas.append(int(input(f'Quantos gols {dados['Nome']} fez na parida {c+1}: ')))
dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print ('=-'*40)
print (dados)
print ('=-'*40)
for c in dados.items():
    print (f'O campo {c[0]} tem o valor {c[1]}')
print ('=-'*40)
print (f'O jogador {dados['Nome']} jogou {dados["Partidas"]} partidas.')
for c in range(dados['Partidas']):
    print (f'==> Na partida {c+1}, fez {dados["Gols"][c]}.')
print (f'O total de gols foi de {dados["Total"]} gols.')
print ('fim do programa!!')