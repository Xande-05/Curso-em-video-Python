lista = list()
dados = dict()
mulheres = list()
velhos = list()
pessoas = idade = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
    if dados['Sexo'] not in ('M', 'F'):
        while dados['Sexo'] not in ('M', 'F'):
            dados['Sexo'] = str(input('Sexo inválido. Digite um sexo [M/F]: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    idade += dados['Idade']
    if dados['Idade'] < 0:
        while dados['Idade'] < 0:
            dados['Idade'] = int (input('Não existem idades negativas, por favor digite uma idade válida: '))
    pessoas += 1
    lista.append(dados.copy())
    desejo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if desejo not in 'SN':
        while desejo not in 'SN':
            desejo = str(input('Opção inváida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if desejo in 'N':
        break
media = idade / pessoas
for c in lista:
    if c['Idade'] > media:
        velhos.append(c['Nome'])
print ('=-'*40)
print (lista)
print ('=-'*40)
print (f'A - Foram cadastradas {pessoas} pessoas')
print (f'B - A média de idade das pessoas cadastradas é de {media:.1f} anos')
print (f'C - As mulheres cadastradas foram {mulheres}')
print (f'D - As pessoas acima da média de idade foram {velhos}')
print ('FIM DO PROGRAMA!')