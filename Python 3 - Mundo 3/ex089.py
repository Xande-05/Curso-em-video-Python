lista = list()
listanota = list()
media = list()
dados = list()
c = 0
while True:
    nome = (input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    listanota.append([nota1])
    listanota.append([nota2])
    dados.append(nome)
    dados.append(listanota[:])
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    listanota.clear()
    desejo = (input('Deseja continuar? [S/N] : '))
    if desejo in 'Nn':
        break
    elif desejo not in 'SsNn':
        while desejo not in 'NnSs':
            desejo = (input ('Resposta incorreta. Deseja continuar? [S/N] '))
print (f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('='*30)
for i, v in enumerate(lista):
    print (f'{i:<4}{v[0]:<10}{v[2]:>8}')
while True:
    print ('='*30)
    opção = int(input('Deseja ver a nota de qual aluno pelo número? (999) para encerrar o programa: '))
    if opção == 999:
        print ('FINALIZANDO...')
        break
    if opção >= len(lista):
        while opção >= len(lista):
            opção = int(input('Opção inválida. Digite o número de um aluno presente na lista ou 999 para encerrar o programa: '))
            if opção == 999:
                print('FINALIZANDO...')
                break
    if opção < len(lista):
        print (f'As notas de {lista[opção][0]} são {lista[opção][2]}')
print('Fim do programa!')
