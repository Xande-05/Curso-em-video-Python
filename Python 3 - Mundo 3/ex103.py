def ficha(jogador='desconhecido', gols=0):
    return (f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


atleta= (str(input('Nome do jogador: ')))
marcações= (str(input('Quantos gols foram feitos? ')))
if marcações.isalpha():
    while marcações.isalpha():
        marcações= (str(input('Por favor digite um número para a quantidade de gols:')))
if atleta == '' and marcações == '':
    print(ficha())
elif atleta == '':
    print(ficha(gols=marcações))
elif marcações == '':
    print(ficha(atleta))
else:
    print(ficha(atleta, marcações))