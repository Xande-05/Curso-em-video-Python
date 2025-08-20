from datetime import datetime
ano_atual = datetime.now().year
dados = dict()
dados['Nome'] = input('Nome: ')
Ano = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - Ano
trabalho = int(input('Carteira de trabalho ("0" caso não tenha): '))
if trabalho == 0:
    dados['Carteira'] = ('Não possui')
else:
    dados['Carteira'] = trabalho
if dados['Carteira'] == ('Não possui'):
    dados['Contratação'] = ('Não foi contratado ainda')
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
if dados['Carteira'] == ('Não possui'):
    dados['Salário'] = ('Ainda não possui um salário')
else:
    dados['Salário'] = int(input('Salário: R$ '))
if dados['Carteira'] == ('Não possui'):
    dados['Aposentadoria'] = (f'Caso assine carteira ainda esse ano, irá se aposentar com {dados['idade']+35} anos de idade')
else:
    dados['Aposentadoria'] = (f'Aposentadoria com {(dados['Contratação'] - Ano) + 35} anos de idade')
for c in dados.items():
    print (f'{c[0]}: {c[1]}')
