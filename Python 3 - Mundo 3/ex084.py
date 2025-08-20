pessoas = []
dados = []
nomemax = []
nomemin = []
max = min = 0
while True:
    dados.append (str(input('Digite o nome: ')))
    dados.append (float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    desejo = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if desejo in 'Nn':
        break
    while desejo not in 'SsNn':
        desejo = input('Opção inválida, deseja continuar? [S/N] ').strip().upper()[0]
for p in pessoas:
    if p[1] >= max:
        max = p[1]
        nomemax.append(p[0])
    if min == 0 or p[1] < min:
        min.append(p[1])
        nomemin = p[0]
print (f'A pessoa mais pesada tem {max} kilos e se chama {nomemax}.')
print (f'A pessoa mais leve tem {min} kilos e se chama {nomemin} .')
print (f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print (pessoas)
print ('Fim do programa.')
